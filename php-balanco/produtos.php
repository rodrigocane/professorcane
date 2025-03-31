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

<body>

    <h2>Listagem de produtos</h2>
    
    <table>
        <thead>
            <tr>
                <th>EAN</th>
                <th>Produto</th>
            </tr>
        </thead>
        <tbody>
            <?php
            $sql = "SELECT p.id, p.ean, p.nome
                    FROM produto p
                    ORDER BY p.nome";
            $result = $conn->query($sql);
            while ($row = $result->fetch_assoc()) {?>
                <tr>
                    <td><?= $row["ean"] ?></td>
                    <td><?= $row["nome"] ?></td>
                </tr>
            <?php } ?>
        </tbody>
    </table>

</body>

</html>