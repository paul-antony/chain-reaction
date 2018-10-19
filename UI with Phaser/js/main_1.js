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
  gameWidth: 397,
  gameHeight: 592,
  cellSize: 58,
  cellPadding: 7,
  boardSize: {
    rows: 9,
    cols: 6
  },
  orbRadius: 10,
  colors: [0xff0000, 0x00ff00]
}

var config = {
  type: Phaser.AUTO,
  width: gameOptions.gameWidth,
  height: gameOptions.gameHeight,
  parent: 'game-section',
  scene: {
    preload: preload,
    create: create
  }
}

var game = new Phaser.Game(config);

function preload() {
  this.load.image('cell', 'assets/cell.png');
}

function create() {
  for(let xPixel=0; xPixel<(gameOptions.gameWidth-gameOptions.cellPadding); xPixel+=(gameOptions.cellPadding+gameOptions.cellSize)) {
    for(let yPixel=0; yPixel<(gameOptions.gameHeight-gameOptions.cellPadding); yPixel+=(gameOptions.cellPadding+gameOptions.cellSize)) {
      this.add.image((xPixel+gameOptions.cellPadding), (yPixel+gameOptions.cellPadding), 'cell').setOrigin(0, 0).setInteractive().on('pointerdown', () => { updateGameState(this.input.activePointer.x, this.input.activePointer.y); });
    }
  }
}

function updateGameState(xClickPosition, yClickPosition) {
  let flag = 0;
  let yIndex = 0;
  for(let xPixel=0; xPixel<(gameOptions.gameWidth-gameOptions.cellPadding); xPixel+=(gameOptions.cellPadding+gameOptions.cellSize)) {
    let xIndex = 0;
    for(let yPixel=0; yPixel<(gameOptions.gameHeight-gameOptions.cellPadding); yPixel+=(gameOptions.cellPadding+gameOptions.cellSize)) {
      if(xClickPosition>=(xPixel+gameOptions.cellPadding) && xClickPosition<=(xPixel+gameOptions.cellPadding+gameOptions.cellSize) && yClickPosition>=(yPixel+gameOptions.cellPadding) && yClickPosition<=(yPixel+gameOptions.cellPadding+gameOptions.cellSize)) {
        if(gameState.player==1 && gameState.board[xIndex][yIndex]>=0) {
          gameState.board[xIndex][yIndex]++;
        }
        else if(gameState.player==-1 && gameState.board[xIndex][yIndex]<=0) {
          gameState.board[xIndex][yIndex]--;
        }
        else {
          flag = 1;
        }
      }
      xIndex++;
    }
    yIndex++;
  }
  if(flag==0) {
      updateBoard();
      gameState.player *= -1;
  }
}

function updateBoard() {
  for(let xIndex=0; xIndex<gameState.board.length; ++xIndex) {
    for(let yIndex=0; yIndex<gameState.board[xIndex].length; ++yIndex) {
      if(gameState.board[xIndex][yIndex]>0) {
        switch(gameState.board[xIndex][yIndex]) {
          case 4: graphics.fillStyle(0xffff00, 1);
                  graphics.beginPath();
                  graphics.moveTo((gameOptions.cellPadding+gameOptions.cellSize)*(xIndex)+39, (gameOptions.cellPadding+gameOptions.cellSize)*(yIndex)+39);
                  graphics.fillCircle((gameOptions.cellPadding+gameOptions.cellSize)*(xIndex)+39, (gameOptions.cellPadding+gameOptions.cellSize)*(yIndex)+39, gameOptions.orbRadius);
                  graphics.closePath();
                  graphics.fillPath();
          case 3: //graphics.fillCircle((gameOptions.cellPadding+gameOptions.cellSize)*(xIndex)+19, (gameOptions.cellPadding+gameOptions.cellSize)*(yIndex)+39, gameOptions.orbRadius);
          case 2: //graphics.fillCircle((gameOptions.cellPadding+gameOptions.cellSize)*(xIndex)+39, (gameOptions.cellPadding+gameOptions.cellSize)*(yIndex)+19, gameOptions.orbRadius);
          case 1: graphics.fillStyle(0xffff00, 1);
                  graphics.beginPath();
                  graphics.moveTo((gameOptions.cellPadding+gameOptions.cellSize)*(xIndex)+19, (gameOptions.cellPadding+gameOptions.cellSize)*(yIndex)+19);
                  graphics.fillCircle((gameOptions.cellPadding+gameOptions.cellSize)*(xIndex)+19, (gameOptions.cellPadding+gameOptions.cellSize)*(yIndex)+19, gameOptions.orbRadius);
                  graphics.closePath();
                  graphics.fillPath();
        }
      }
      else {
        if(gameState.board[xIndex][yIndex]<0) {
          switch(gameState.board[xIndex][yIndex]) {
            case -4: //this.add.image((gameOptions.cellPadding+gameOptions.cellSize)*(xIndex)+19, (gameOptions.cellPadding+gameOptions.cellSize)*(yIndex)+19, 'green_orb').setOrigin(0, 0);
            case -3: //this.add.image((gameOptions.cellPadding+gameOptions.cellSize)*(xIndex)+9, (gameOptions.cellPadding+gameOptions.cellSize)*(yIndex)+19, 'green_orb').setOrigin(0, 0);
            case -2: //this.add.image((gameOptions.cellPadding+gameOptions.cellSize)*(xIndex)+19, (gameOptions.cellPadding+gameOptions.cellSize)*(yIndex)+9, 'green_orb').setOrigin(0, 0);
            case -1: //this.add.image((gameOptions.cellPadding+gameOptions.cellSize)*(xIndex)+9, (gameOptions.cellPadding+gameOptions.cellSize)*(yIndex)+9, 'green_orb').setOrigin(0, 0);
          }
        }
      }
    }
  }
}
