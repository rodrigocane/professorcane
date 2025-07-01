<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Quiz Municípios do Brasil</title>
  <style>
    * {
      box-sizing: border-box;
    }

    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      display: flex;
      flex-direction: column;
      min-height: 100vh;
      background: #f4f4f4;
    }

    header {
      background-color: #2c3e50;
      color: white;
      padding: 1rem;
      text-align: center;
    }

    main {
      flex: 1;
      padding: 2rem;
      max-width: 600px;
      margin: auto;
    }

    h2 {
      text-align: center;
      color: #333;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      margin: 1rem 0;
      background-color: white;
    }

    th, td {
      padding: 0.75rem;
      border: 1px solid #ccc;
      text-align: center;
    }

    form {
      display: flex;
      flex-direction: column;
      align-items: center;
      margin-top: 2rem;
    }

    input[type="text"] {
      padding: 0.5rem;
      width: 80%;
      max-width: 300px;
      font-size: 1rem;
      margin-bottom: 1rem;
    }

    button {
      padding: 0.6rem 1.2rem;
      font-size: 1rem;
      background-color: #27ae60;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }

    button:hover {
      background-color: #219150;
    }

    footer {
      background-color: #ecf0f1;
      text-align: center;
      padding: 1rem;
      font-size: 0.9rem;
      color: #555;
    }
  </style>
</head>
<body>
  <header>
    <h1>🗺️ Quiz Municípios do Brasil 🗺️</h1>
  </header>

  <main>
    <h2>Ranking</h2>
    <table>
      <thead>
        <tr>
          <th>Posição</th>
          <th>Nome</th>
          <th>Pontuação</th>
        </tr>
      </thead>
      <tbody>
        <!-- Os dados serão preenchidos via PHP -->
        <tr>
          <td>1</td>
          <td>Maria</td>
          <td>90</td>
        </tr>
        <tr>
          <td>2</td>
          <td>João</td>
          <td>80</td>
        </tr>
      </tbody>
    </table>

    <form action="jogo.php" method="POST">
      <label for="nome">Digite seu nome para jogar:</label>
      <input type="text" name="nome" id="nome" required>
      <button type="submit">🎮 JOGAR</button>
    </form>
  </main>

  <footer>
    © 2025 Nome do aluno
  </footer>
</body>
</html>
