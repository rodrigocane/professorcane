<?php
include "conexao.php";
//Alteração teste
$sql = "SELECT b.id, DATE_FORMAT(b.data_registro, '%d/%m/%Y (%H:%i)') as data_formatada, 
            SUM(bp.quantidade_aferida) as qtde_total
        FROM balanco b
        JOIN balanco_produto bp ON b.id = bp.balanco_id
        GROUP BY b.id, b.data_registro
        ORDER BY b.data_registro DESC
        LIMIT 1";

$result = $conn->query($sql);
$row = $result->fetch_object();

// *************************************************

$sql_hist = "SELECT id, DATE_FORMAT(data_registro, '%d/%m/%Y (%H:%i)') as data_registro 
             FROM balanco ORDER BY id DESC";
$result_hist = $conn->query($sql_hist);
$array_hist = [];

while ($row_hist = $result_hist->fetch_object()) {
    array_push($array_hist, $row_hist);
}

// *************************************************

$return = array(
    'balanco' => $row,
    'historico' => $array_hist
);

sleep(2);
echo json_encode($return);