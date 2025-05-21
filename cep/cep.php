<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <title>Cadastrar Pessoa</title>

    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 40px;
            background-color: #f4f7f9;
            color: #333;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        h1,
        h2 {
            text-align: center;
            color: #2c3e50;
        }

        form {
            background: #fff;
            padding: 25px 50px 25px 25px;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
        }

        label {
            font-weight: 600;
            margin-top: 12px;
            display: block;
        }

        input,
        select {
            width: 100%;
            padding: 10px;
            margin-top: 5px;
            border: 1px solid #ccc;
            border-radius: 6px;
            transition: border-color 0.3s ease;
        }

        input:focus,
        select:focus {
            border-color: #3498db;
            outline: none;
        }

        .readonly {
            background-color: #f0f0f0;
        }

        button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 10px 16px;
            font-size: 15px;
            border-radius: 6px;
            margin-top: 15px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        button:hover {
            background-color: #2980b9;
        }

        .buscar-btn i {
            margin-right: 6px;
        }
        
    </style>
</head>

<body>

    <h1><i class="fa-solid fa-user-plus"></i> Cadastrar Pessoa</h1>
    <form method="post">
        <label for="nome">Nome:</label>
        <input type="text" name="nome" required>

        <label for="cpf">CPF:</label>
        <input type="text" name="cpf" required>

        <label for="data_nascimento">Data de Nascimento:</label>
        <input type="date" name="data_nascimento" required>

        <label for="cep">CEP:</label>
        <input type="text" name="cep" id="cep" required>
        <button type="button" class="buscar-btn" onclick="buscarEndereco()">
            <i class="fa-solid fa-magnifying-glass-location"></i> Buscar Endereço
        </button>

        <label for="logradouro">Logradouro:</label>
        <input type="text" id="logradouro" name="logradouro" readonly class="readonly">

        <label for="bairro">Bairro:</label>
        <input type="text" id="bairro" name="bairro" readonly class="readonly">

        <label for="localidade">Cidade:</label>
        <input type="text" id="localidade" name="localidade" readonly class="readonly">

        <label for="uf">Estado:</label>
        <input type="text" id="uf" name="uf" readonly class="readonly">

        <label for="numero">Número:</label>
        <input type="text" name="numero" required>
        <button type="submit">Salvar</button>
    </form>


    <script>
        function buscarEndereco() {
            const cep = document.getElementById('cep').value.replace(/\D/g, '');
            if (cep.length !== 8) {
                alert('CEP inválido');
                return;
            }
            const logradouro = document.getElementById('logradouro');
            const bairro = document.getElementById('bairro');
            fetch('https://viacep.com.br/ws/' + cep + '/json/')
                .then(response => response.json())
                .then(data => {
                    if (data.erro) {
                        alert('CEP não encontrado');
                        return;
                    }

                    if (!data.logradouro && !data.bairro) {
                        logradouro.readOnly = false;
                        logradouro.classList.remove('readonly');
                        bairro.readOnly = false;
                        bairro.classList.remove('readonly');
                    } else {
                        logradouro.readOnly = true;
                        logradouro.classList.add('readonly');
                        bairro.readOnly = true;
                        bairro.classList.add('readonly');
                    }
                    logradouro.value = data.logradouro || '';
                    bairro.value = data.bairro || '';
                    document.getElementById('localidade').value = data.localidade || '';
                    document.getElementById('uf').value = data.uf || '';
                })
                .catch(() => {
                    alert('Erro ao consultar CEP');
                });
        }

    </script>
</body>

</html>
