<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Quiz Municípios do Brasil - Rodada X</title>
  <style>
    * {
      box-sizing: border-box;
    }

    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background: #f4f4f4;
      display: flex;
      flex-direction: column;
      min-height: 100vh;
    }

    header {
      background-color: #34495e;
      color: white;
      padding: 1rem;
      text-align: center;
    }

    main {
      flex: 1;
      padding: 1rem;
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .info-bar {
      display: flex;
      justify-content: center;
      align-items: center;
      flex-wrap: wrap;
      gap: 1.5rem;
      width: 100%;
      background: #ecf0f1;
      padding: 1rem;
      margin-bottom: 1rem;
      border-radius: 8px;
      font-size: 1.1rem;
    }

    .grid-container {
      display: grid;
      grid-template-areas:
        "top"
        "row1"
        "row2"
        "bottom";
      gap: 1rem;
      width: 100%;
      margin-top: 1rem;
    }

    .area {
      padding: 1rem;
      border-radius: 8px;
      text-align: center;
      min-height: 100px;
      font-weight: bold;
      position: relative;
    }

    .top    { grid-area: top; background-color: #a0a0a0; width: 100%; }
    .row1-1, .row2-1 {
      display: flex;
      gap: 1rem;
      justify-content: center;
    }
    .row1-1 { grid-area: row1; }
    .row2-1 { grid-area: row2; }
    .bottom { 
      grid-area: bottom;
      background-color: #f28b82;
      width: fit-content;
      margin: auto;
    }

    .dropzone {
      min-width: 150px;
      min-height: 100px;
      border: 2px dashed #aaa;
      border-radius: 8px;
      padding: 1.5rem 0.5rem 0.5rem;
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      align-items: center;
      position: relative;
    }

    .dropzone::before {
      content: attr(id);
      position: absolute;
      top: -0.8rem;
      left: 50%;
      transform: translateX(-50%);
      background: white;
      padding: 0 0.3rem;
      font-size: 0.85rem;
      color: #333;
    }

    #Norte      { background-color: #b2dfdb; }
    #Nordeste   { background-color: #bbdefb; }
    #Centro-Oeste     { background-color: #fff9c4; }
    #Sudeste    { background-color: #ffe0b2; }
    #Sul        { background-color: #ffcdd2; }

    .drag-item {
      background-color: #e0e0e0;
      padding: 0.5rem 1rem;
      margin: 0.3rem;
      border-radius: 4px;
      cursor: grab;
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
      background-color: #1e874b;
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
    <h1>🕹️ Rodada <span id="numRodada">X</span> de 10</h1>
  </header>

  <main>
    <div class="info-bar">
      <div>🏅 Pontuação: <strong id="pontuacao">0</strong></div>
      <div>⏳ Tempo: <strong id="tempo">15</strong>s</div>
      <button id="btnSalvar">💾 SALVAR</button>
    </div>

    <div class="grid-container">
      <div class="area top dropzone" id="area-???">
        <div class="drag-item" draggable="true">Município1</div>
        <div class="drag-item" draggable="true">Município2</div>
        <div class="drag-item" draggable="true">Município3</div>
        <div class="drag-item" draggable="true">Município4</div>
        <div class="drag-item" draggable="true">Município5</div>
        <div class="drag-item" draggable="true">Município6</div>
      </div>

      <div class="row1-1">
        <div class="dropzone" id="Norte"></div>
        <div class="dropzone" id="Nordeste"></div>
      </div>

      <div class="row2-1">
        <div class="dropzone" id="Centro-Oeste"></div>
        <div class="dropzone" id="Sudeste"></div>
      </div>

      <div class="area bottom dropzone" id="Sul"></div>
    </div>
  </main>

  <footer>
    © 2025 Nome do aluno
  </footer>
</body>
</html>
