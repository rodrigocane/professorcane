<?php
include "conexao.php";

if ($_SERVER['REQUEST_METHOD'] != 'POST') {
    header('Location: balanco.php');
    exit;
}

$sql = "INSERT INTO balanco (data_registro) VALUES (NOW())";
$result = $conn->query($sql);
$balanco_id = $conn->insert_id;

foreach ($_POST['qtde'] as $produto_id => $produto_qtd) {
    if ($produto_qtd != '') {
        $sql_produto = "INSERT INTO balanco_produto 
        (id, balanco_id, produto_id, quantidade_aferida) 
        VALUES 
        (NULL, '" . $balanco_id . "', '" . $produto_id . "', '" . $produto_qtd . "')";

        $result_produto = $conn->query($sql_produto);
    }
}

header('Status: 200');