<?php
include "conexao.php";

if ($_SERVER['REQUEST_METHOD'] != 'POST') {
    header('Location: balanco.php');
    exit;
}

$conn->begin_transaction();
try {
    $sql = "INSERT INTO balanco (data_registro) VALUES (NOW())";
    $conn->query($sql);
    $balanco_id = $conn->insert_id;

    $sql = "INSERT INTO balanco_produto (balanco_id, produto_id, 
                    quantidade_aferida) VALUES (?, ?, ?)";
    $stmt_insert = $conn->prepare($sql);
    $qtdes = $_POST['qtde'];
    foreach ($qtdes as $produto_id => $produto_qtd) {
        $stmt_insert->bind_param("iii", $balanco_id, $produto_id, $produto_qtd);
        $stmt_insert->execute();
    }
    
    $conn->commit();
} catch (Exception $e) {
    $conn->rollback();
    exit;
}

header('Status: 200');