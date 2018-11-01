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
  gameWidth: 670,
  gameHeight: 562,
  boardWidth: 362,
  boardHeight: 542,
  boardTopPadding: 10,
  boardLeftPadding: 10,
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

var gameType = 0;

var winner;

var game = new Phaser.Game(gameOptions.gameWidth, gameOptions.gameHeight, Phaser.AUTO, 'game-section', { preload: preload, create: create });

var gameType1State = {
  preload: function() {
    preload();
  },
  create: function() {
    create();
  },
  update: function() {
    game.input.onDown.add(updateGameState, this);
    updateBoard();
  }
}

game.state.add('gameType1', gameType1State);

var gameType2State = {
  preload: function() {
    preload();
  },
  create: function() {
    create();
  },
  update: function() {
    game.input.onDown.add(updateGameState, this);
    updateBoard();
  }
}

game.state.add('gameType2', gameType2State);

var gameType3State = {
  preload: function() {
    preload();
  },
  create: function() {
    create();
  },
  update: function() {
    game.input.onDown.add(updateGameState, this);
    updateBoard();
  }
}

game.state.add('gameType3', gameType3State);

var gameType4State = {
  preload: function() {
    preload();
  },
  create: function() {
    create();
  },
  update: function() {
    game.input.onDown.add(updateGameState, this);
    updateBoard();
  }
}

game.state.add('gameType4', gameType4State);

var menuState = {
  preload: function() {
    this.load.image('button', 'assets/button.png');
    game.stage.backgroundColor = gameOptions.colors[2];
  },
  create: function() {
    var menuLabel = game.add.text(42, 60, 'Chain Reaction' , { font: '40px Arial', fill: '#ffffff' });
    gameType1Button = game.add.button(((gameOptions.gameWidth/2)-95), 170, 'button', gameType1Click, this).scale.setTo(1.1, 1.1);
    gameType1ButtonLabel = game.add.text(((gameOptions.gameWidth/2)-78), 180, 'Human vs Human' , { font: '22px Arial', fill: '#000000' });
    function gameType1Click() {
      gameType = 1;
      game.state.start('gameType1');
    }
    gameType2Button = game.add.button(((gameOptions.gameWidth/2)-95), 250, 'button', gameType2Click, this);
    gameType2ButtonLabel = game.add.text(((gameOptions.gameWidth/2)-88), 258, 'Human vs Human' , { font: '22px Arial', fill: '#000000' });
    function gameType2Click() {
      gameType = 2;
      game.state.start('gameType2');
    }
    gameType3Button = game.add.button(((gameOptions.gameWidth/2)-95), 330, 'button', gameType3Click, this);
    gameType3ButtonLabel = game.add.text(((gameOptions.gameWidth/2)-88), 338, 'Human vs Human' , { font: '22px Arial', fill: '#000000' });
    function gameType3Click() {
      gameType = 3;
      game.state.start('gameType3');
    }
    gameType4Button = game.add.button(((gameOptions.gameWidth/2)-95), 410, 'button', gameType4Click, this);
    gameType4ButtonLabel = game.add.text(((gameOptions.gameWidth/2)-88), 418, 'Human vs Human' , { font: '22px Arial', fill: '#000000' });
    function gameType4Click() {
      gameType = 4;
      game.state.start('gameType4');
    }
  }
}

game.state.add('menu', menuState);
game.state.start('menu');

var winState = {
  preload: function() {
    this.load.image('button', 'assets/button.png');
    game.stage.backgroundColor = gameOptions.colors[2];
  },
  create: function() {
    if(winner==1 && gameType==1) {
      let winLabel = game.add.text(25, 80, 'Player 1 wins!' , { font: '50px Arial', fill: '#ffffff' });
    }
    else if(winner==-1 && gameType==1) {
      let winLabel = game.add.text(25, 80, 'Player 2 wins!' , { font: '50px Arial', fill: '#ffffff' });
    }
    menuButton = game.add.button(((gameOptions.gameWidth/2)-95), 210, 'button', menuClick, this);
    menuButtonLabel = game.add.text(((gameOptions.gameWidth/2)-50), 218, 'Main Menu' , { font: '22px Arial', fill: '#000000' });
    function menuClick() {
      game.state.start('menu');
    }
    playAgainButton = game.add.button(((gameOptions.gameWidth/2)-95), 300, 'button', playAgainClick, this);
    playAgainButtonLabel = game.add.text(((gameOptions.gameWidth/2)-50), 308, 'Play Again' , { font: '22px Arial', fill: '#000000' });
    function playAgainClick() {
      if(gameType==1) {
        game.state.start('gameType1');
      }
      else if(gameType==2) {
        game.state.start('gameType2');
      }
      else if(gameType==3) {
        game.state.start('gameType3');
      }
      else if(gameType==4) {
        game.state.start('gameType4');
      }
    }
    gameState.player = 1;
    for(let rowIndex=0; rowIndex<gameState.board.length; ++rowIndex) {
      for(let colIndex=0; colIndex<gameState.board[rowIndex].length; ++colIndex) {
        gameState.board[rowIndex][colIndex] = 0;
      }
    }
  }
}

game.state.add('win', winState);

function preload() {
  winner = 0;
  game.load.image('cell', 'assets/cell.png');
  game.stage.backgroundColor = gameOptions.colors[2];
  let graphics = game.add.graphics(0, 0);
  graphics.beginFill(gameOptions.colors[0], 1);
  graphics.drawRect(gameOptions.boardLeftPadding, gameOptions.boardTopPadding, gameOptions.boardWidth, gameOptions.boardHeight);
}

function create() {
  for(let yPos=gameOptions.boardTopPadding; yPos<(gameOptions.boardTopPadding+gameOptions.boardHeight-gameOptions.cellPadding); yPos+=(gameOptions.cellPadding+gameOptions.cellSize)) {
    for(let xPos=gameOptions.boardLeftPadding; xPos<(gameOptions.boardLeftPadding+gameOptions.boardWidth-gameOptions.cellPadding); xPos+=(gameOptions.cellPadding+gameOptions.cellSize)) {
      game.add.image((xPos+gameOptions.cellPadding), (yPos+gameOptions.cellPadding), 'cell');
    }
  }
}

async function updateGameState() {
  let xClickedPos = game.input.mousePointer.x;
  let yClickedPos = game.input.mousePointer.y;
  let validFlag = -1;
  let rowIndex = 0;
  for(let yPos=gameOptions.boardTopPadding; yPos<(gameOptions.boardTopPadding+gameOptions.boardHeight-gameOptions.cellPadding); yPos+=(gameOptions.cellPadding+gameOptions.cellSize)) {
    let colIndex = 0;
    for(let xPos=gameOptions.boardLeftPadding; xPos<(gameOptions.boardLeftPadding+gameOptions.boardWidth-gameOptions.cellPadding); xPos+=(gameOptions.cellPadding+gameOptions.cellSize)) {
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
              let unstableCellIndex = unstableCells.shift();
              if(Math.abs(gameState.board[unstableCellIndex[0]][unstableCellIndex[1]])>=criticalMass(unstableCellIndex[0], unstableCellIndex[1])) {
                gameState.board[unstableCellIndex[0]][unstableCellIndex[1]] -= (gameState.player * criticalMass(unstableCellIndex[0], unstableCellIndex[1]));
                let neighbors = getNeighbors(unstableCellIndex[0], unstableCellIndex[1]);
                for(let index=0; index<neighbors.length; ++index) {
                  gameState.board[neighbors[index][0]][neighbors[index][1]] = gameState.player * (Math.abs(gameState.board[neighbors[index][0]][neighbors[index][1]]) + 1);
                  unstableCells.push(neighbors[index]);
                }
              }
              await sleep(gameOptions.burstTime);
              checkWin();
            }
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
    if(winner==0) {
      gameState.player *= -1;
    }
    let graphics = game.add.graphics(0, 0);
    if(gameState.player==1 && winner==0) {
      graphics.beginFill(gameOptions.colors[0], 1);
    }
    else if(gameState.player==-1 && winner==0) {
      graphics.beginFill(gameOptions.colors[1], 1);
    }
    graphics.drawRect(gameOptions.boardLeftPadding, gameOptions.boardTopPadding, gameOptions.boardWidth, gameOptions.boardHeight);
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
  let win;
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
    winner = win;
    game.state.start('win');
  }
}

function updateBoard() {
  create();
  let graphics = game.add.graphics(0, 0);
  for(let rowIndex=0; rowIndex<gameState.board.length; ++rowIndex) {
    for(let colIndex=0; colIndex<gameState.board[colIndex].length; ++colIndex) {
      if(gameState.board[rowIndex][colIndex]>0) {
        graphics.beginFill(gameOptions.colors[0], 1);
        switch(gameState.board[rowIndex][colIndex]) {
          case 4: graphics.drawCircle(gameOptions.boardLeftPadding+(gameOptions.cellPadding+gameOptions.cellSize)*(colIndex)+gameOptions.cellPadding+39, gameOptions.boardTopPadding+(gameOptions.cellPadding+gameOptions.cellSize)*(rowIndex)+gameOptions.cellPadding+39, gameOptions.orbRadius);
          case 3: graphics.drawCircle(gameOptions.boardLeftPadding+(gameOptions.cellPadding+gameOptions.cellSize)*(colIndex)+gameOptions.cellPadding+19, gameOptions.boardTopPadding+(gameOptions.cellPadding+gameOptions.cellSize)*(rowIndex)+gameOptions.cellPadding+39, gameOptions.orbRadius);
          case 2: graphics.drawCircle(gameOptions.boardLeftPadding+(gameOptions.cellPadding+gameOptions.cellSize)*(colIndex)+gameOptions.cellPadding+39, gameOptions.boardTopPadding+(gameOptions.cellPadding+gameOptions.cellSize)*(rowIndex)+gameOptions.cellPadding+19, gameOptions.orbRadius);
          case 1: graphics.drawCircle(gameOptions.boardLeftPadding+(gameOptions.cellPadding+gameOptions.cellSize)*(colIndex)+gameOptions.cellPadding+19, gameOptions.boardTopPadding+(gameOptions.cellPadding+gameOptions.cellSize)*(rowIndex)+gameOptions.cellPadding+19, gameOptions.orbRadius);
        }
      }
      else if(gameState.board[rowIndex][colIndex]<0) {
        graphics.beginFill(gameOptions.colors[1], 1);
        switch(gameState.board[rowIndex][colIndex]) {
          case -4: graphics.drawCircle(gameOptions.boardLeftPadding+(gameOptions.cellPadding+gameOptions.cellSize)*(colIndex)+gameOptions.cellPadding+39, gameOptions.boardTopPadding+(gameOptions.cellPadding+gameOptions.cellSize)*(rowIndex)+gameOptions.cellPadding+39, gameOptions.orbRadius);
          case -3: graphics.drawCircle(gameOptions.boardLeftPadding+(gameOptions.cellPadding+gameOptions.cellSize)*(colIndex)+gameOptions.cellPadding+19, gameOptions.boardTopPadding+(gameOptions.cellPadding+gameOptions.cellSize)*(rowIndex)+gameOptions.cellPadding+39, gameOptions.orbRadius);
          case -2: graphics.drawCircle(gameOptions.boardLeftPadding+(gameOptions.cellPadding+gameOptions.cellSize)*(colIndex)+gameOptions.cellPadding+39, gameOptions.boardTopPadding+(gameOptions.cellPadding+gameOptions.cellSize)*(rowIndex)+gameOptions.cellPadding+19, gameOptions.orbRadius);
          case -1: graphics.drawCircle(gameOptions.boardLeftPadding+(gameOptions.cellPadding+gameOptions.cellSize)*(colIndex)+gameOptions.cellPadding+19, gameOptions.boardTopPadding+(gameOptions.cellPadding+gameOptions.cellSize)*(rowIndex)+gameOptions.cellPadding+19, gameOptions.orbRadius);
        }
      }
    }
  }
}
