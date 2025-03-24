<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gestão de Chamada</title>
    <link rel="stylesheet" href="styles.css">
    <script defer src="script.js"></script>
</head>
<body>
    <h2>Selecione um Dia Letivo</h2>
    <select id="diaLetivo" onchange="redirecionar()">
        <option value="">-- Escolha um dia --</option>
        <?php
		require 'conexao.php'; // Arquivo de conexão com o banco

		$sql = "SELECT id, DATE_FORMAT(data, '%d/%m/%Y') AS data_formatada FROM DiaLetivo ORDER BY data ASC";
		$result = $conn->query($sql);

		if ($result->num_rows > 0) {
			while ($row = $result->fetch_assoc()) {
				echo "<option value='" . $row['id'] . "'>" . $row['data_formatada'] . "</option>";
			}
		} else {
			echo "<option value=''>Nenhum dia disponível</option>";
		}

		$conn->close();
		?>
    </select>

    <script>
        function redirecionar() {
            const dia = document.getElementById('diaLetivo').value;
            if (dia) {
                window.location.href = `chamada.php?dia=${dia}`;
            }
        }
    </script>
</body>
</html>
