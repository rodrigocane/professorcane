<?php
include "conexao.php";

$balanco_id = $_GET['id_balanco'];
$array_itens = [];

$sql = "SELECT p.id, p.ean, p.nome, COALESCE(bp.quantidade_aferida, 0) as quantidade_aferida
        FROM produto p
        LEFT JOIN balanco_produto bp ON bp.produto_id = p.id AND bp.balanco_id = {$balanco_id}
        ORDER BY p.nome";
$result = $conn->query($sql);

while ($row = $result->fetch_object()) {
    array_push($array_itens, $row);
}

echo json_encode($array_itens);