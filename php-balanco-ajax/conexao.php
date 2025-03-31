<?php
$servername = "localhost:3306";
$username = "root";
$password = "";
$database = "balanco";

try {
    $conn = new mysqli($servername, $username, $password, $database);
    
    // Configurar o mysqli para lançar exceções em caso de erro
    mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);    
} catch (mysqli_sql_exception $e) {
    die("Erro na conexão com o banco de dados: " . $e->getMessage());
}
?>