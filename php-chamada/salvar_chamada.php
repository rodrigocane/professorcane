<?php
require 'conexao.php';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
	die("Tá perdido, amigão?");
}

$dia_id = $_POST['dia_id'] ?? null;
if (!$dia_id) {
	die("Dia letivo não informado.");
}

$conn->begin_transaction();
try {
	$sql = "INSERT INTO Presenca (aluno_id, dia_letivo_id, aula, presente) 
			VALUES (?, ?, ?, ?)
			ON DUPLICATE KEY UPDATE `presente` = VALUES(`presente`)";
	$stmt_insert = $conn->prepare($sql);	
	
	foreach ($_POST['presenca'] as $aluno_id => $aulas) {
		for ($aula = 1; $aula <= 4; $aula++) {
			$presente = isset($aulas[$aula]) ? 1 : 0;
			$stmt_insert->bind_param("iiii", $aluno_id, $dia_id, $aula, $presente);
			$stmt_insert->execute();
		}
	}

	$conn->commit();
	echo "<script>alert('Chamada salva com sucesso!'); window.location.href = 'index.php';</script>";
} catch (Exception $e) {
	$conn->rollback();
	die("Erro ao salvar chamada: " . $e->getMessage());
}
?>
