<?php
include "conexao.php";

?>
<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registro de Inventário</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
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

        .actions {
            margin-top: 20px;
        }

        button {
            padding: 10px 15px;
            margin: 5px;
            cursor: pointer;
            font-size: 16px;
        }

        .quantity-box {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 5px;
            /* Adiciona um pequeno espaçamento entre os elementos */
        }

        .quantity-box button {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 35px;
            height: 35px;
            font-size: 18px;
            padding: 0;
            /* Remove qualquer espaçamento interno */
        }

        .quantity-box input {
            text-align: center;
            width: 50px;
            font-size: 16px;
        }

        .success-box {
            border: 1px solid #4CAF50;
            background-color: #f2f2f2;
            color: #4CAF50;
            margin-bottom: 15px;
            padding: 15px;
            text-align: center;
            display: none;
        }
    </style>
</head>

<body>

    <h2>Registro de Inventário</h2>
    <div class="success-box">
        <p>Balanço salvo com sucesso!</p>
    </div>
    <div class="info-box">
        <p>
            <strong>Última Aferição:</strong>
            <span class="last-check">
                <i class="fa-solid fa-spinner fa-spin"></i>
            </span>
        </p>
        <p>
            <strong>Quantidade Total Aferida:</strong>
            <span class="qtd-total-check">
                <i class="fa-solid fa-spinner fa-spin"></i>
            </span>
            peças
        </p>
        <button onclick="gerarRelatorio()"><i class="fas fa-file-alt"></i> Gerar Relatório</button>
        <br><br>
        <select class="balanco-historico">
            <option>Carregando ...</option>
        </select>
    </div>

    <form method="POST" action="salvar_balanco.php">
        <table>
            <thead>
                <tr>
                    <th>EAN</th>
                    <th>Produto</th>
                    <th>Quantidade Atual</th>
                    <th>Quantidade Nova</th>
                </tr>
            </thead>
            <tbody>
            </tbody>
        </table>
        <div class="actions">
            <button type="button" onClick="resetar()"><i class="fas fa-undo"></i> Resetar</button>
            <button type="button" onClick="salvar()"><i class="fas fa-save"></i> Salvar</button>
        </div>
    </form>

    <script class="template-item" type="text/template">
        <tr>
            <td>__EAN__</td>
            <td>__PRODUTO__</td>
            <td>__QUANTIDADE__</td>
            <td>
                <div class="quantity-box">
                    <button type="button" onclick="alterarQuantidade(this, -1)"><i class="fas fa-minus"></i></button>
                    <input type="number" min="0" name="qtde[__ID__]" value="__QUANTIDADE__">
                    <button type="button" onclick="alterarQuantidade(this, 1)"><i class="fas fa-plus"></i></button>
                </div>
            </td>
        </tr>
    </script>

    <script>
        async function loadProduct(idBalance) {
            const response = await fetch('produto-ajax.php?id_balanco=' + idBalance);
            if (!response.ok) {
                alert('Não deu boa pra noiz');
            }
            const body = await response.text();
            const infos = JSON.parse(body);
            const tableItens = document.querySelector('table tbody');

            tableItens.innerHTML = '';

            infos.forEach(element => {
                let item = document.querySelector('.template-item').innerHTML;
                item = item.replaceAll('__ID__', element.id);
                item = item.replace('__EAN__', element.ean);
                item = item.replace('__PRODUTO__', element.nome);
                item = item.replaceAll('__QUANTIDADE__', element.quantidade_aferida);


                tableItens.insertAdjacentHTML('beforeend', item);
            });
        }

        async function loadBalance() {
            const response = await fetch('balanco-ajax.php');
            if (!response.ok) {
                alert('Não deu boa pra noiz');
            }
            const body = await response.text();
            const infos = JSON.parse(body);

            loadProduct(infos.balanco.id);
            preencherHistorico(infos.historico);

            document.querySelector('.last-check').innerHTML = infos.balanco.data_formatada;
            document.querySelector('.qtd-total-check').innerHTML = infos.balanco.qtde_total;
        }
        loadBalance();

        function preencherHistorico(historico) {
            const _select = document.querySelector('.balanco-historico');
            _select.innerHTML = '';

            const _option = document.createElement('option');
            _option.text = 'Selecione o balanço';
            _select.insertAdjacentElement('beforeend', _option);

            historico.forEach(element => {
                const _option = document.createElement('option');
                _option.text = element.data_registro;
                _option.value = element.id;
                _select.insertAdjacentElement('beforeend', _option);
            });
        }


        function alterarQuantidade(botao, delta) {
            let input = botao.parentElement.querySelector('input');
            let novaQuantidade = (input.value ? parseInt(input.value) : 0) + delta;
            input.value = (novaQuantidade >= 0 && input.value) ? novaQuantidade : 0;
        }

        function resetar() {
            if (confirm("Tem certeza que deseja resetar os valores?")) {
                // Aqui é contigo!!!
            }
        }
        const successBox = document.querySelector('.success-box');

        async function salvar() {
            const form = document.querySelector('form');
            const formData = new FormData(form);

            const response = await fetch('salvar_balanco.php', {
                method: 'POST',
                body: formData
            });

            if (response.ok) {
                successBox.style.display = 'block';
                successBox.scrollIntoView();
                setTimeout(() => successBox.style.display = 'none', 2000);
                loadBalance();
            }
        }

        function gerarRelatorio() {
            window.open("relatorio.php", "_blank");
        }
    </script>

</body>

</html>