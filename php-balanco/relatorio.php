<?php
session_start();
if (!isset($_SESSION['id_usuario'])) {
    header('Location: index.php');
}

include 'conexao.php';
?>

<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Relatório de Inventário</title>
    <link rel="icon" type="image/x-icon" href="supplies.ico">
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
    </style>
</head>

<body onload="window.print()">

    <h2>Relatório de Inventário</h2>
    <?php
    $sql = "SELECT b.id, DATE_FORMAT(b.data_registro, '%d/%m/%Y (%H:%i)') as 
                dt_formatada, SUM(bp.quantidade_aferida) as qtde_total
            FROM balanco b 
            JOIN balanco_produto bp ON bp.balanco_id = b.id
            GROUP BY b.id,b.data_registro
            ORDER BY b.data_registro DESC
            LIMIT 1";

    $result = $conn->query($sql);
    $row = $result->fetch_assoc();
    $balanco_id = $row["id"];
    $balanco_data = $row["dt_formatada"];
    $balanco_total = $row["qtde_total"];
    ?>
    <div class="info-box">
        <p><strong>Última Aferição:</strong> <?= $balanco_data ?></p>
        <p><strong>Quantidade Total Aferida:</strong> <?= $balanco_total ?> peças</p>
    </div>

    <table>
        <thead>
            <tr>
                <th>EAN</th>
                <th>Produto</th>
                <th>Quantidade Aferida</th>
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
            while ($row = $result->fetch_assoc()) {?>
                <tr>
                    <td><?= $row["ean"] ?></td>
                    <td><?= $row["nome"] ?></td>
                    <td><?= $row["qtde"] ?></td>
                </tr>
            <?php } ?>
        </tbody>
    </table>

</body>

</html>