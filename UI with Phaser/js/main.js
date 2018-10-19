var gameState = {
  player: 1,
  board: [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
  ]
}

var gameOptions = {
  gameWidth: 362,
  gameHeight: 542,
  boardSize: {
    rows: 9,
    cols: 6
  },
  cellSize: 58,
  cellPadding: 2,
  orbRadius: 20,
  colors: [0xff0000, 0x00ff00]
}

var cell = [[]];

var game = new Phaser.Game(gameOptions.gameWidth, gameOptions.gameHeight, Phaser.AUTO, 'game-section', { preload: preload, create: create });

function preload() {
  this.load.image('cell', 'assets/cell.png');
  game.stage.backgroundColor = gameOptions.colors[0];
}

function create() {
  for(let yPos=0; yPos<(gameOptions.gameHeight-gameOptions.cellPadding); yPos+=(gameOptions.cellPadding+gameOptions.cellSize)) {
    for(let xPos=0; xPos<(gameOptions.gameWidth-gameOptions.cellPadding); xPos+=(gameOptions.cellPadding+gameOptions.cellSize)) {
      game.add.image((xPos+gameOptions.cellPadding), (yPos+gameOptions.cellPadding), 'cell');
    }
  }
  game.input.onDown.add(updateGameState, this);
}

function updateGameState() {
  let xClickedPos = game.input.mousePointer.x;
  let yClickedPos = game.input.mousePointer.y;
  let flag = -1;
  let rowIndex = 0;
  for(let yPos=0; yPos<(gameOptions.gameHeight-gameOptions.cellPadding); yPos+=(gameOptions.cellPadding+gameOptions.cellSize)) {
    let colIndex = 0;
    for(let xPos=0; xPos<(gameOptions.gameWidth-gameOptions.cellPadding); xPos+=(gameOptions.cellPadding+gameOptions.cellSize)) {
      if(xClickedPos>=(xPos+gameOptions.cellPadding) && xClickedPos<=(xPos+gameOptions.cellPadding+gameOptions.cellSize) && yClickedPos>=(yPos+gameOptions.cellPadding) && yClickedPos<=(yPos+gameOptions.cellPadding+gameOptions.cellSize)) {
        if(gameState.player==1 && gameState.board[rowIndex][colIndex]>=0) {
          gameState.board[rowIndex][colIndex]++;
          flag = 0;
        }
        else if(gameState.player==-1 && gameState.board[rowIndex][colIndex]<=0) {
          gameState.board[rowIndex][colIndex]--;
          flag = 0;
        }
        else {
          flag = 1;
        }
        checkBurst(rowIndex, colIndex);
      }
      colIndex++;
    }
    rowIndex++;
  }
  if(flag==0) {
      updateBoard();
      gameState.player *= -1;
      if(gameState.player==1) {
        game.stage.backgroundColor = gameOptions.colors[0];
      }
      else {
        game.stage.backgroundColor = gameOptions.colors[1];
      }
  }
  console.log(gameState.board);
}

function checkBurst(rowIndex, colIndex) {
  if(((rowIndex==0 && colIndex==0) || (rowIndex==0 && colIndex==(gameState.board[rowIndex].length-1)) || (rowIndex==(gameState.board.length-1) && colIndex==0) || (rowIndex==(gameState.board[rowIndex].length-1) && colIndex==(gameState.board.length-1))) && (gameState.board[rowIndex][colIndex]==2 || gameState.board[rowIndex][colIndex]==-2)) {

  }
  else if((rowIndex==0 || colIndex==0 || rowIndex==(gameState.board.length-1) || colIndex==(gameState.board[rowIndex].length-1)) && (gameState.board[rowIndex][colIndex]==3 || gameState.board[rowIndex][colIndex]==-3)) {

  }
  else if(gameState.board[rowIndex][colIndex]==4 || gameState.board[rowIndex][colIndex]==-4) {

  }
}

function updateBoard() {
  var graphics = game.add.graphics(0, 0);
  for(let rowIndex=0; rowIndex<gameState.board.length; ++rowIndex) {
    for(let colIndex=0; colIndex<gameState.board[colIndex].length; ++colIndex) {
      if(gameState.board[rowIndex][colIndex]>0) {
        graphics.beginFill(gameOptions.colors[0], 1);
        switch(gameState.board[rowIndex][colIndex]) {
          case 4: graphics.drawCircle((gameOptions.cellPadding+gameOptions.cellSize)*(colIndex)+gameOptions.cellPadding+39, (gameOptions.cellPadding+gameOptions.cellSize)*(rowIndex)+gameOptions.cellPadding+39, gameOptions.orbRadius);
          case 3: graphics.drawCircle((gameOptions.cellPadding+gameOptions.cellSize)*(colIndex)+gameOptions.cellPadding+19, (gameOptions.cellPadding+gameOptions.cellSize)*(rowIndex)+gameOptions.cellPadding+39, gameOptions.orbRadius);
          case 2: graphics.drawCircle((gameOptions.cellPadding+gameOptions.cellSize)*(colIndex)+gameOptions.cellPadding+39, (gameOptions.cellPadding+gameOptions.cellSize)*(rowIndex)+gameOptions.cellPadding+19, gameOptions.orbRadius);
          case 1: graphics.drawCircle((gameOptions.cellPadding+gameOptions.cellSize)*(colIndex)+gameOptions.cellPadding+19, (gameOptions.cellPadding+gameOptions.cellSize)*(rowIndex)+gameOptions.cellPadding+19, gameOptions.orbRadius);
        }
      }
      else if(gameState.board[rowIndex][colIndex]<0) {
        graphics.beginFill(gameOptions.colors[1], 1);
        switch(gameState.board[rowIndex][colIndex]) {
          case -4: graphics.drawCircle((gameOptions.cellPadding+gameOptions.cellSize)*(colIndex)+gameOptions.cellPadding+39, (gameOptions.cellPadding+gameOptions.cellSize)*(rowIndex)+gameOptions.cellPadding+39, gameOptions.orbRadius);
          case -3: graphics.drawCircle((gameOptions.cellPadding+gameOptions.cellSize)*(colIndex)+gameOptions.cellPadding+19, (gameOptions.cellPadding+gameOptions.cellSize)*(rowIndex)+gameOptions.cellPadding+39, gameOptions.orbRadius);
          case -2: graphics.drawCircle((gameOptions.cellPadding+gameOptions.cellSize)*(colIndex)+gameOptions.cellPadding+39, (gameOptions.cellPadding+gameOptions.cellSize)*(rowIndex)+gameOptions.cellPadding+19, gameOptions.orbRadius);
          case -1: graphics.drawCircle((gameOptions.cellPadding+gameOptions.cellSize)*(colIndex)+gameOptions.cellPadding+19, (gameOptions.cellPadding+gameOptions.cellSize)*(rowIndex)+gameOptions.cellPadding+19, gameOptions.orbRadius);
        }
      }
    }
  }
}
