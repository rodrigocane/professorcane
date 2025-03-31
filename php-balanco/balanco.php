<?php
session_start();
if (!isset($_SESSION['id_usuario'])) {
    header('Location: index.php');
}

include 'conexao.php';
if ($_SERVER['REQUEST_METHOD'] == "POST" && isset($_POST['qtde'])) {
    if (isset($_POST['acao']) && $_POST['acao'] == "editar") {
        //Editando o balanco existente
        $qtdes = $_POST['qtde'];

        $conn->begin_transaction();
        try {
            $sql = "UPDATE balanco_produto SET quantidade_aferida = ? WHERE balanco_id = ? AND produto_id = ?";
            $stmt_update = $conn->prepare($sql);
            foreach ($qtdes as $produto_id => $qtde) {
                $stmt_update->bind_param("iii", $qtde, $_POST['balanco_id'], $produto_id);
                $stmt_update->execute();
            }
            $conn->commit();
            $sucesso = true;
            echo "<script>setTimeout(() => document.querySelector('.success-box').style.display='none', 2000);</script>";
        } catch (Exception $e) {
            $conn->rollback();
            die("Não foi possível editar o balanço. Tente novamente mais tarde.");
        }
    } else {
        //Estamos inserindo um novo balanço
        $qtdes = $_POST['qtde'];

        $conn->begin_transaction();
        try {
            $sql = "INSERT INTO balanco (data_registro) VALUES (NOW())";
            $conn->query($sql);
            $balanco_id = $conn->insert_id;

            $sql = "INSERT INTO balanco_produto (balanco_id, produto_id, 
                    quantidade_aferida) VALUES (?, ?, ?)";
            $stmt_insert = $conn->prepare($sql);
            foreach ($qtdes as $produto_id => $qtde) {
                if ($qtde > 0) {
                    $stmt_insert->bind_param("iii", $balanco_id, $produto_id, $qtde);
                    $stmt_insert->execute();
                }
            }
            $conn->commit();
            $sucesso = true;
            echo "<script>setTimeout(() => document.querySelector('.success-box').style.display='none', 2000);</script>";
        } catch (Exception $e) {
            $conn->rollback();
            die("Não foi possível salvar o balanço. Tente novamente mais tarde.");
        }
    }
}

?>

<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registro de Inventário</title>
    <link rel="icon" type="image/x-icon" href="supplies.ico">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            text-align: center;
        }

        .info-box {
            border: 1px solid #ddd;
            padding: 10px;
            margin: 10px auto;
            width: 50%;
            background: #f9f9f9;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }

        th,
        td {
            border: 1px solid #ddd;
            padding: 10px;
            text-align: center;
        }

        th {
            background-color: #f4f4f4;
        }

        .actions {
            margin-top: 20px;
            display: flex;
            justify-content: center;
        }

        button {
            padding: 10px 15px;
            margin: 5px;
            cursor: pointer;
            font-size: 16px;
        }

        .quantity-box {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 5px;
            /* Adiciona um pequeno espaçamento entre os elementos */
        }

        .quantity-box button {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 35px;
            height: 35px;
            font-size: 18px;
            padding: 0;
            /* Remove qualquer espaçamento interno */
        }

        .quantity-box input {
            text-align: center;
            width: 50px;
            font-size: 16px;
        }

        .success-box {
            border: 1px solid #4CAF50;
            background-color: #f2f2f2;
            color: #4CAF50;
            margin-bottom: 15px;
            padding: 15px;
            text-align: center;
        }
    </style>
</head>

<body>

    <?php if (isset($sucesso)): ?>
        <div class="success-box">
            <p>Balanço salvo com sucesso!</p>
        </div>
    <?php endif; ?>

    <h2>Registro de Inventário</h2>
    <?php

    if (isset($_POST['acao']) && $_POST['acao'] == "preeditar") {
        $editando = true;
        $sql = "SELECT b.id, DATE_FORMAT(b.data_registro, '%d/%m/%Y (%H:%i)') as
                    dt_formatada, SUM(bp.quantidade_aferida) as qtde_total
                FROM balanco b 
                JOIN balanco_produto bp ON bp.balanco_id = b.id
                GROUP BY b.id,b.data_registro
                HAVING b.id = {$_POST["balanco_id"]}";
    } else {
        $sql = "SELECT b.id, DATE_FORMAT(b.data_registro, '%d/%m/%Y (%H:%i)') as
                    dt_formatada, SUM(bp.quantidade_aferida) as qtde_total
                FROM balanco b 
                JOIN balanco_produto bp ON bp.balanco_id = b.id
                GROUP BY b.id,b.data_registro
                ORDER BY b.data_registro DESC
                LIMIT 1";
    }

    $result = $conn->query($sql);
    $row = $result->fetch_assoc();
    $balanco_id = $row["id"];
    $balanco_data = $row["dt_formatada"];
    $balanco_total = $row["qtde_total"];
    ?>
    <div class="info-box">
        <p><strong>Última Aferição:</strong> <?= $balanco_data ?></p>
        <p><strong>Quantidade Total Aferida:</strong> <?= $balanco_total ?> peças</p>
        <div class="actions">
            <button onclick="window.location.href='logout.php'"><i class="fa-solid fa-power-off"></i> Logout </button>
            <button onclick="abrirLink('relatorio.php')"><i class="fas fa-file-alt"></i> Relatório</button>
            <button onclick="abrirLink('produtos.php')"><i class="fa-solid fa-warehouse"></i> Produtos</button>
            <?php
            if (isset($_SESSION['is_adm']) && $_SESSION['is_adm']) { ?>
                <form method="pOsT">
                    <input type="hidden" name="balanco_id" value="<?= $balanco_id ?>">
                    <input type="hidden" name="acao" value="preeditar">
                    <button><i class="fa-solid fa-pencil"></i> Editar</button>
                </form>
            <?php } ?>
        </div>
    </div>

    <form method="POST">
        <?php if (isset($editando)) { ?>
            <input type="hidden" name="balanco_id" value="<?= $balanco_id ?>">
            <input type="hidden" name="acao" value="editar">
        <?php } ?>
        <table>
            <thead>
                <tr>
                    <th>EAN</th>
                    <th>Produto</th>
                    <th>Quantidade Anterior</th>
                    <th>Quantidade Atual</th>
                </tr>
            </thead>
            <tbody>
                <?php
                $sql = "SELECT p.id, p.ean, p.nome, COALESCE(bp.quantidade_aferida, 0) as qtde
                    FROM produto p
                    LEFT JOIN balanco_produto bp ON bp.produto_id = p.id
                        AND bp.balanco_id = {$balanco_id}
                    ORDER BY p.nome";
                $result = $conn->query($sql);
                while ($row = $result->fetch_assoc()) {
                    ?>
                    <tr>
                        <td><?= $row["ean"] ?></td>
                        <td><?= $row["nome"] ?></td>
                        <td><?= $row["qtde"] ?></td>
                        <td>
                            <div class="quantity-box">
                                <button type="button" onclick="alterarQuantidade(this, -1)"><i
                                        class="fas fa-minus"></i></button>
                                <input type="number" class="qtde" name="qtde[<?= $row["id"] ?>]" min="0" <?= isset($editando) ? "value='{$row["qtde"]}'" : "" ?>>
                                <button type="button" onclick="alterarQuantidade(this, 1)"><i
                                        class="fas fa-plus"></i></button>
                            </div>
                        </td>
                    </tr>
                    <?php
                }
                ?>
            </tbody>
        </table>

        <div class="actions">
            <button type="button" onclick="resetar()"><i class="fas fa-undo"></i> Resetar</button>
            <button type="submit"><i class="fas fa-save"></i> Salvar</button>
        </div>
    </form>

    <script>
        function alterarQuantidade(botao, delta) {
            let input = botao.parentElement.querySelector('input');
            let novaQuantidade = (input.value ? parseInt(input.value) : 0) + delta;
            if (novaQuantidade >= 0) {
                input.value = novaQuantidade;
            }
        }

        function resetar() {
            x = 3;
            if (confirm("Tem certeza que deseja resetar os valores?")) {
                document.querySelectorAll(".qtde")
                    .forEach(input => input.value = "");
            }
        }

        function abrirLink(pagina) {
            window.open(pagina, "_blank");
        }
    </script>

</body>

</html>