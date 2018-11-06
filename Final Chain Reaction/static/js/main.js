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
  ],
  prevBoard: [
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
  burstTime: 0
}

var gameType = 0;

var turnState = 1;

var winner;

var initialState = 1;

var undoClickCount = 2;

var turnAI = 0;

var game = new Phaser.Game(gameOptions.gameWidth, gameOptions.gameHeight, Phaser.AUTO, 'game-section', { preload: preload, create: create });

var gameType1State = {
  preload: function() {
    preload();
  },
  create: function() {
    create();
    undoButton = game.add.button(((gameOptions.gameWidth/2)+61), 472, 'button', undoClick, this, 1, 0).scale.setTo(0.6, 1);
    undoButtonLabel = game.add.text(((gameOptions.gameWidth/2)+87), 480, 'UNDO' , { font: '22px Arial', fill: '#000000' });
    menuButton = game.add.button(((gameOptions.gameWidth/2)+197), 472, 'button', menuClick, this, 1, 0).scale.setTo(0.6, 1);
    menuButtonLabel = game.add.text(((gameOptions.gameWidth/2)+223), 480, 'MENU' , { font: '22px Arial', fill: '#000000' });
    gameLabel = game.add.text(((gameOptions.gameWidth/2)+88), 30, 'Chain Reaction' , { font: '28px Arial', fill: '#ffffff' });
    player1Label = game.add.text(((gameOptions.gameWidth/2)+48), 90, 'Player 1: Human 1' , { font: '20px Arial', fill: '#ffffff' });
    player2Label = game.add.text(((gameOptions.gameWidth/2)+48), 125, 'Player 2: Human 2' , { font: '20px Arial', fill: '#ffffff' });
    currentTurnLabel = game.add.text(((gameOptions.gameWidth/2)+48), 180, 'Current Turn: Human 1' , { font: '20px Arial', fill: '#ffffff' });
    game.input.onDown.add(updateGameState, this);
  },
  update: function() {
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
    undoButton = game.add.button(((gameOptions.gameWidth/2)+61), 472, 'button', undoClick, this, 1, 0).scale.setTo(0.6, 1);
    undoButtonLabel = game.add.text(((gameOptions.gameWidth/2)+87), 480, 'UNDO' , { font: '22px Arial', fill: '#000000' });
    menuButton = game.add.button(((gameOptions.gameWidth/2)+197), 472, 'button', menuClick, this, 1, 0).scale.setTo(0.6, 1);
    menuButtonLabel = game.add.text(((gameOptions.gameWidth/2)+223), 480, 'MENU' , { font: '22px Arial', fill: '#000000' });
    gameLabel = game.add.text(((gameOptions.gameWidth/2)+88), 30, 'Chain Reaction' , { font: '28px Arial', fill: '#ffffff' });
    if(turnAI==1) {
      player1Label = game.add.text(((gameOptions.gameWidth/2)+48), 90, 'Player 1: Agent 1' , { font: '20px Arial', fill: '#ffffff' });
      player2Label = game.add.text(((gameOptions.gameWidth/2)+48), 125, 'Player 2: Human' , { font: '20px Arial', fill: '#ffffff' });
      currentTurnLabel = game.add.text(((gameOptions.gameWidth/2)+48), 180, 'Current Turn: Agent 1' , { font: '20px Arial', fill: '#ffffff' });
    }
    else if(turnAI==-1) {
      player1Label = game.add.text(((gameOptions.gameWidth/2)+48), 90, 'Player 1: Human' , { font: '20px Arial', fill: '#ffffff' });
      player2Label = game.add.text(((gameOptions.gameWidth/2)+48), 125, 'Player 2: Agent 1' , { font: '20px Arial', fill: '#ffffff' });
      currentTurnLabel = game.add.text(((gameOptions.gameWidth/2)+48), 180, 'Current Turn: Human' , { font: '20px Arial', fill: '#ffffff' });
    }
    game.input.onDown.add(updateGameState, this);
    if((turnAI==1 && gameState.player==1) || (turnAI==-1 && gameState.player==-1)) {
      turnState = 0;
      $.postJSON('/', {
        player: gameState.player,
        board: gameState.board
      }, function(data) {
        console.log("success");
      });
    }
  },
  update: function() {
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
    game.load.spritesheet('button', 'static/assets/button_sprites.png', 190, 49);
    game.stage.backgroundColor = gameOptions.colors[2];
  },
  create: function() {
    var menuLabel = game.add.text(196, 60, 'Chain Reaction' , { font: '40px Arial', fill: '#ffffff' });
    gameType1Button = game.add.button(((gameOptions.gameWidth/2)-114), 170, 'button', gameType1Click, this, 1, 0).scale.setTo(1.2, 1.1);
    gameType1ButtonLabel = game.add.text(((gameOptions.gameWidth/2)-87), 180, 'Human vs Human' , { font: '22px Arial', fill: '#000000' });
    function gameType1Click() {
      gameType = 1;
      game.state.start('gameType1');
    }
    gameType2Button = game.add.button(((gameOptions.gameWidth/2)-114), 250, 'button', gameType2Click, this, 1, 0).scale.setTo(1.2, 1.1);
    gameType2ButtonLabel = game.add.text(((gameOptions.gameWidth/2)-90), 260, 'Human vs Agent 1' , { font: '22px Arial', fill: '#000000' });
    function gameType2Click() {
      gameType = 2;
      game.state.start('choosePlayer');
    }
    gameType3Button = game.add.button(((gameOptions.gameWidth/2)-114), 330, 'button', gameType3Click, this, 1, 0).scale.setTo(1.2, 1.1);
    gameType3ButtonLabel = game.add.text(((gameOptions.gameWidth/2)-90), 340, 'Human vs Agent 2' , { font: '22px Arial', fill: '#000000' });
    function gameType3Click() {
      gameType = 3;
      game.state.start('gameType3');
    }
    gameType4Button = game.add.button(((gameOptions.gameWidth/2)-114), 410, 'button', gameType4Click, this, 1, 0).scale.setTo(1.2, 1.1);
    gameType4ButtonLabel = game.add.text(((gameOptions.gameWidth/2)-92), 420, 'Agent 1 vs Agent 2' , { font: '22px Arial', fill: '#000000' });
    function gameType4Click() {
      gameType = 4;
      game.state.start('gameType4');
    }
  }
}

game.state.add('menu', menuState);
game.state.start('menu');

var choosePlayerState = {
  create: function() {
    let choosePlayerLabel = game.add.text(205, 80, 'Player as...' , { font: '50px Arial', fill: '#ffffff' });
    player1Button = game.add.button(((gameOptions.gameWidth/2)-95), 210, 'button', player1Click, this, 1, 0);
    player1ButtonLabel = game.add.text(((gameOptions.gameWidth/2)-40), 218, 'Player 1' , { font: '22px Arial', fill: '#000000' });
    player2Button = game.add.button(((gameOptions.gameWidth/2)-95), 300, 'button', player2Click, this, 1, 0);
    player2ButtonLabel = game.add.text(((gameOptions.gameWidth/2)-40), 308, 'Player 2' , { font: '22px Arial', fill: '#000000' });
    function player1Click() {
      turnAI = -1;
      game.state.start('gameType2');
    }
    function player2Click() {
      turnAI = 1;
      game.state.start('gameType2');
    }
    backButton = game.add.button(((gameOptions.gameWidth/2)+197), 472, 'button', menuClick, this, 1, 0).scale.setTo(0.6, 1);
    backButtonLabel = game.add.text(((gameOptions.gameWidth/2)+223), 480, 'BACK' , { font: '22px Arial', fill: '#000000' });
  }
}

game.state.add('choosePlayer', choosePlayerState);

var winState = {
  create: function() {
    if(winner==1 && gameType==1) {
      let winLabel = game.add.text(176, 80, 'Player 1 wins!' , { font: '50px Arial', fill: '#ffffff' });
    }
    else if(winner==-1 && gameType==1) {
      let winLabel = game.add.text(176, 80, 'Player 2 wins!' , { font: '50px Arial', fill: '#ffffff' });
    }
    menuButton = game.add.button(((gameOptions.gameWidth/2)-95), 210, 'button', menuClick, this, 1, 0);
    menuButtonLabel = game.add.text(((gameOptions.gameWidth/2)-50), 218, 'Main Menu' , { font: '22px Arial', fill: '#000000' });
    playAgainButton = game.add.button(((gameOptions.gameWidth/2)-95), 300, 'button', playAgainClick, this, 1, 0);
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
  }
}

game.state.add('win', winState);

function preload() {
  winner = 0;
  gameState.player = 1;
  initialState = 1;
  for(let rowIndex=0; rowIndex<gameState.board.length; ++rowIndex) {
    for(let colIndex=0; colIndex<gameState.board[rowIndex].length; ++colIndex) {
      gameState.board[rowIndex][colIndex] = 0;
    }
  }
  game.stage.backgroundColor = gameOptions.colors[2];
  let graphics = game.add.graphics(0, 0);
  graphics.beginFill(gameOptions.colors[0], 1);
  graphics.drawRect(gameOptions.boardLeftPadding, gameOptions.boardTopPadding, gameOptions.boardWidth, gameOptions.boardHeight);
  game.load.image('cell', 'static/assets/cell.png');
}

function create() {
  for(let yPos=gameOptions.boardTopPadding; yPos<(gameOptions.boardTopPadding+gameOptions.boardHeight-gameOptions.cellPadding); yPos+=(gameOptions.cellPadding+gameOptions.cellSize)) {
    for(let xPos=gameOptions.boardLeftPadding; xPos<(gameOptions.boardLeftPadding+gameOptions.boardWidth-gameOptions.cellPadding); xPos+=(gameOptions.cellPadding+gameOptions.cellSize)) {
      game.add.image((xPos+gameOptions.cellPadding), (yPos+gameOptions.cellPadding), 'cell');
    }
  }
}

async function updateGameState() {
  if(turnState==1) {
    turnState = 0;
    let xClickedPos = game.input.mousePointer.x;
    let yClickedPos = game.input.mousePointer.y;
    let validFlag = -1;
    let rowIndex = 0;
    for(let yPos=gameOptions.boardTopPadding; yPos<(gameOptions.boardTopPadding+gameOptions.boardHeight-gameOptions.cellPadding); yPos+=(gameOptions.cellPadding+gameOptions.cellSize)) {
      let colIndex = 0;
      for(let xPos=gameOptions.boardLeftPadding; xPos<(gameOptions.boardLeftPadding+gameOptions.boardWidth-gameOptions.cellPadding); xPos+=(gameOptions.cellPadding+gameOptions.cellSize)) {
        if(xClickedPos>=(xPos+gameOptions.cellPadding+1) && xClickedPos<=(xPos+gameOptions.cellPadding+gameOptions.cellSize) && yClickedPos>=(yPos+gameOptions.cellPadding+2) && yClickedPos<=(yPos+gameOptions.cellPadding+gameOptions.cellSize+1)) {
          if(gameState.player==1 && gameState.board[rowIndex][colIndex]>=0) {
            undoClickCount = 0;
            gameState.prevBoard = gameState.board.map(row => row.slice());
            gameState.board[rowIndex][colIndex]++;
            validFlag = 1;
          }
          else if(gameState.player==-1 && gameState.board[rowIndex][colIndex]<=0) {
            undoClickCount = 0;
            gameState.prevBoard = gameState.board.map(row => row.slice());
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
        currentTurnLabel.destroy();
        gameState.player *= -1;
        changeCurrentTurnLabel();
      }
      initialState = 0;
      changeBoardColor();
    }
    turnState = 1;
  }
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function undoClick() {
  if(initialState==0) {
    ++undoClickCount;
    if(undoClickCount==1) {
      gameState.board = gameState.prevBoard.map(row => row.slice());
      gameState.player *= -1;
      changeBoardColor();
    }
    currentTurnLabel.destroy();
    changeCurrentTurnLabel();
  }
}

function menuClick() {
  game.state.start('menu');
}

function changeBoardColor() {
  let graphics = game.add.graphics(0, 0);
  if(gameState.player==1 && winner==0) {
    graphics.beginFill(gameOptions.colors[0], 1);
  }
  else if(gameState.player==-1 && winner==0) {
    graphics.beginFill(gameOptions.colors[1], 1);
  }
  graphics.drawRect(gameOptions.boardLeftPadding, gameOptions.boardTopPadding, gameOptions.boardWidth, gameOptions.boardHeight);
}

function changeCurrentTurnLabel() {
  if(gameState.player==1 && gameType==1) {
    currentTurnLabel = game.add.text(((gameOptions.gameWidth/2)+48), 180, 'Current Turn: Human 1' , { font: '20px Arial', fill: '#ffffff' });
  }
  else if(gameState.player==-1 && gameType==1) {
    currentTurnLabel = game.add.text(((gameOptions.gameWidth/2)+48), 180, 'Current Turn: Human 2' , { font: '20px Arial', fill: '#ffffff' });
  }
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
