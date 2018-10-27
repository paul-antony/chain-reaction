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
  colors: [0xff0000, 0x00ff00, 0x3498db],
  burstTime: 100,
}

var win;

var gameType = 1;

var game = new Phaser.Game(gameOptions.gameWidth, gameOptions.gameHeight, Phaser.AUTO, 'game-section', { preload: preload, create: create, update: update });

var winState = {
  preload: function() {
    this.load.image('button', 'assets/button.png');
    game.stage.backgroundColor = gameOptions.colors[2];
  },
  create: function() {
    if(win==1 && gameType==1) {
      var winLabel = game.add.text(25, 80, 'Player 1 wins!' , { font: '50px Arial', fill: '#ffffff' });
    }
    else if(win==-1 && gameType==1) {
      var winLabel = game.add.text(25, 80, 'Player 2 wins!' , { font: '50px Arial', fill: '#ffffff' });
    }
    mainMenuButton = game.add.button(((gameOptions.gameWidth/2)-95), 210, 'button', mainMenuClick, this);
    mainMenuButtonLabel = game.add.text(((gameOptions.gameWidth/2)-50), 218, 'Main Menu' , { font: '22px Arial', fill: '#000000' });
    function mainMenuClick() {
      game.stage.background.visible =! game.stage.background.visible;
    }
    playAgainButton = game.add.button(((gameOptions.gameWidth/2)-95), 300, 'button', playAgainClick, this);
    playAgainButtonLabel = game.add.text(((gameOptions.gameWidth/2)-50), 308, 'Play Again' , { font: '22px Arial', fill: '#000000' });
    function playAgainClick() {
      game.stage.background.visible =! game.stage.background.visible;
    }
  }
}

game.state.add('win', winState);

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
}

function update() {
  game.input.onDown.add(updateGameState, this);
  updateBoard();
}

async function updateGameState() {
  let xClickedPos = game.input.mousePointer.x;
  let yClickedPos = game.input.mousePointer.y;
  let validFlag = -1;
  let rowIndex = 0;
  for(let yPos=0; yPos<(gameOptions.gameHeight-gameOptions.cellPadding); yPos+=(gameOptions.cellPadding+gameOptions.cellSize)) {
    let colIndex = 0;
    for(let xPos=0; xPos<(gameOptions.gameWidth-gameOptions.cellPadding); xPos+=(gameOptions.cellPadding+gameOptions.cellSize)) {
      if(xClickedPos>=(xPos+gameOptions.cellPadding+1) && xClickedPos<=(xPos+gameOptions.cellPadding+gameOptions.cellSize) && yClickedPos>=(yPos+gameOptions.cellPadding+2) && yClickedPos<=(yPos+gameOptions.cellPadding+gameOptions.cellSize+1)) {
        if(gameState.player==1 && gameState.board[rowIndex][colIndex]>=0) {
          gameState.board[rowIndex][colIndex]++;
          validFlag = 1;
        }
        else if(gameState.player==-1 && gameState.board[rowIndex][colIndex]<=0) {
          gameState.board[rowIndex][colIndex]--;
          validFlag = 1;
        }
        else {
          validFlag = 0;
        }
        if(validFlag==1) {
          if(Math.abs(gameState.board[rowIndex][colIndex])>=criticalMass(rowIndex, colIndex)) {
            let unstableCells = [];
            unstableCells.push([rowIndex, colIndex]);
            while(unstableCells.length>0) {
              await sleep(gameOptions.burstTime);
              let unstableCellIndex = unstableCells.shift();
              if(Math.abs(gameState.board[unstableCellIndex[0]][unstableCellIndex[1]])>=criticalMass(unstableCellIndex[0], unstableCellIndex[1])) {
                gameState.board[unstableCellIndex[0]][unstableCellIndex[1]] -= (gameState.player * criticalMass(unstableCellIndex[0], unstableCellIndex[1]));
                let neighbors = getNeighbors(unstableCellIndex[0], unstableCellIndex[1]);
                for(let index=0; index<neighbors.length; ++index) {
                  gameState.board[neighbors[index][0]][neighbors[index][1]] = gameState.player * (Math.abs(gameState.board[neighbors[index][0]][neighbors[index][1]]) + 1);
                  unstableCells.push(neighbors[index]);
                }
              }
            }
            checkWin();
          }
        }
        break;
      }
      colIndex++;
    }
    rowIndex++;
    if(validFlag==0 || validFlag==1) {
      break;
    }
  }
  if(validFlag==1) {
    validFlag = -1;
    gameState.player *= -1;
    if(gameState.player==1) {
      game.stage.backgroundColor = gameOptions.colors[0];
    }
    else {
      game.stage.backgroundColor = gameOptions.colors[1];
    }
  }
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function getNeighbors(rowIndex, colIndex) {
  let neighbors = [];
  if((rowIndex-1)>=0) {
    neighbors.push([rowIndex-1, colIndex]);
  }
  if((rowIndex+1)<gameState.board.length) {
    neighbors.push([rowIndex+1, colIndex]);
  }
  if((colIndex-1)>=0) {
    neighbors.push([rowIndex, colIndex-1]);
  }
  if((colIndex+1)<gameState.board[rowIndex].length) {
    neighbors.push([rowIndex, colIndex+1]);
  }
  return neighbors;
}

function criticalMass(rowIndex, colIndex) {
    if((rowIndex==0 && colIndex==0) || (rowIndex==(gameState.board.length-1) && colIndex==0) || (rowIndex==0 && colIndex==(gameState.board[rowIndex].length-1)) || (rowIndex==(gameState.board.length-1) && colIndex==(gameState.board[rowIndex].length-1))) {
      return 2;
    }
    else if(rowIndex==0 || rowIndex==(gameState.board.length-1) || colIndex==0 || colIndex==(gameState.board[rowIndex].length-1)) {
      return 3;
    }
    else {
      return 4;
    }
}

function checkWin() {
  let winChance;
  for(let rowIndex=0; rowIndex<gameState.board.length; ++rowIndex) {
    for(let colIndex=0; colIndex<gameState.board[rowIndex].length; ++colIndex) {
      if(gameState.board[rowIndex][colIndex]>0) {
        winChance = 1;
        break;
      }
      else if(gameState.board[rowIndex][colIndex]<0) {
        winChance = -1;
        break;
      }
    }
    if(winChance==1 || winChance==-1) {
      break;
    }
  }
  for(let rowIndex=0; rowIndex<gameState.board.length; ++rowIndex) {
    for(let colIndex=0; colIndex<gameState.board[rowIndex].length; ++colIndex) {
      if(gameState.board[rowIndex][colIndex]>0 && winChance==1) {
        win = 1;
      }
      else if(gameState.board[rowIndex][colIndex]<0 && winChance==-1) {
        win = -1;
      }
      else if((gameState.board[rowIndex][colIndex]>0 && winChance==-1) || (gameState.board[rowIndex][colIndex]<0 && winChance==1))  {
        win = 0;
        break;
      }
    }
    if(win==0) {
      break;
    }
  }
  if(win==1 || win==-1) {
    game.state.start('win');
  }
}

function updateBoard() {
  create();
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
