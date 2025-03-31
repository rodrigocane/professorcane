<?php

$conn = new mysqli("localhost:3306", "root", "", "balanco55");
if ($conn->connect_error) {
    die("Conexão falhou: " . $conn->connect_error);
}
?>