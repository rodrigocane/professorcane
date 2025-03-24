<?php
include 'conexao.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $login = $_POST["login"];
    $password = $_POST["password"];
    $hash = password_hash($password, PASSWORD_BCRYPT);
    $sql = "SELECT id, nome, login, email, hash FROM usuarios WHERE login = ?";
    $result = $conn->execute_query($sql, [$login]);
    if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();
        if (password_verify($password, $row["hash"])) {
            session_start();
            $_SESSION["login"] = $login;
            $_SESSION["nome"] = $row["nome"];
            $_SESSION["id_usuario"] = $row["id"];
            $_SESSION["email"] = $row["email"];

            header('Location: balanco.php');
            exit;
        }
    }
    $erro = true;
}

?>

<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
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
    </style>
</head>

<body>
    <h2>Login</h2>
    <?php if (isset($erro) && $erro) { ?>
        <h2>Usuário ou senha inválidos</h2>
    <?php } ?>

    <div class="info-box">
        <form method="post">
            <p><input type='text' name='login' placeholder="Login" required></p>
            <p><input type='password' name='password' placeholder="Senha" required></p>
            <p><button type='submit'>Logar</button></p>
        </form>
    </div>
</body>

</html>