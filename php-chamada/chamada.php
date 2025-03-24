<?php
require 'conexao.php';

$dia_id = $_GET['dia'] ?? null;
if (!$dia_id) {
    die("Dia letivo não informado.");
}

// Buscar os alunos e suas presenças para o dia escolhido
$sql = "SELECT A.id, A.nome, A.dataNascimento, DATE_FORMAT(D.data, '%d/%m/%Y') AS data_formatada, P.aula, COALESCE(P.presente, false) as presente
        FROM Aluno A
		JOIN DiaLetivo D ON d.id = ?
        LEFT JOIN Presenca P ON A.id = P.aluno_id AND P.dia_letivo_id = ?
        ORDER BY A.nome ASC";
$stmt = $conn->prepare($sql);
$stmt->bind_param("ii", $dia_id, $dia_id);
$stmt->execute();
$result = $stmt->get_result();

$hoje = new DateTime();
$menor_idade = 18;
$alunos = [];
$data_formatada = new DateTime();
while ($row = $result->fetch_assoc()) {
	$data_formatada = $row['data_formatada'];
    $dataNascimento = new DateTime($row['dataNascimento']);
    $idade = $hoje->diff($dataNascimento)->y;
    $row['menor'] = $idade < $menor_idade;
    $alunos[$row['id']]['nome'] = $row['nome'];
    $alunos[$row['id']]['menor'] = $row['menor'];
    $alunos[$row['id']]['presencas'][$row['aula']] = $row['presente'];
}
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chamada</title>
	<style>
	body { font-family: Arial, sans-serif; background-color: #f4f4f4; }
	h2 { position: sticky; top: 0; background: #f4f4f4; padding: 10px; margin: 0; z-index: 100; text-align: center }
	.table-container { max-height: 85vh; overflow-y: auto; margin: auto; width: 50vw; background: white; border-radius: 5px; }
	table { width: 100%; border-collapse: collapse; }
	th, td { border: 1px solid #ddd; padding: 8px 10px; }
	th { background: #007BFF; color: white; position: sticky; top: 0; z-index: 99; }
	.menor { font-size: 12px; color: gray; }
	.datatable-center { text-align: center; vertical-align: middle; }
	.button-container { padding: 10px; background: #f4f4f4; position: sticky; bottom: 0; z-index: 100; text-align: center }
	button { margin: 5px; padding: 10px; cursor: pointer; }
	</style>
</head>
<body>
    <h2>Chamada - Dia Letivo <?= $data_formatada ?></h2>
    <form method="POST" action="salvar_chamada.php">
        <input type="hidden" name="dia_id" value="<?= $dia_id?>">
		<div class="table-container">
        <table>
            <tr>
                <th>Aluno</th>
                <?php for ($i = 1; $i <= 4; $i++): ?>
                    <th class='datatable-center'>
                        Aula <?= $i ?><br>
                        <input type="checkbox" onclick="toggleColumn(<?= $i ?>)">
                    </th>
                <?php endfor; ?>
            </tr>
            <?php foreach ($alunos as $id => $aluno): ?>
                <tr>
                    <td>
                        <?= htmlspecialchars($aluno['nome']) ?>
                        <?php if ($aluno['menor']): ?>
                            <span class="menor">(menor)</span>
                        <?php endif; ?>
                    </td>
                    <?php for ($i = 1; $i <= 4; $i++): ?>
                        <td class='datatable-center'>
                            <input type="checkbox" name="presenca[<?= $id ?>][<?= $i ?>]" value="1" <?= (isset($aluno['presencas'][$i]) && $aluno['presencas'][$i]) ? 'checked' : '' ?>>
                        </td>
                    <?php endfor; ?>
                </tr>
            <?php endforeach; ?>
        </table>
		</div>
        <div class="button-container">
            <button type="button" onclick="history.back()">Voltar</button>
            <button type="button" onclick="limparTudo()">Limpar</button>
            <button type="button" onclick="replicarPrimeiraColuna()">Replicar</button>
            <button type="submit">Enviar</button>
        </div>
    </form>

    <script>
        function toggleColumn(col) {
            document.querySelectorAll(`input[name^='presenca'][name$='[${col}]']`).forEach(cb => {
                cb.checked = event.target.checked;
            });
        }

        function limparTudo() {
            if (confirm("Tem certeza que deseja limpar a chamada?")) {
                document.querySelectorAll("input[type=checkbox]").forEach(cb => cb.checked = false);
            }
        }

        function replicarPrimeiraColuna() {
            let primeiraColuna = document.querySelectorAll("input[name^='presenca'][name$='[1]']");
            primeiraColuna.forEach((cb, index) => {
                let marcado = cb.checked;
                for (let i = 2; i <= 4; i++) {
                    document.querySelector(`input[name='presenca[${cb.name.match(/\d+/)[0]}][${i}]']`).checked = marcado;
                }
            });
        }
    </script>
</body>
</html>
