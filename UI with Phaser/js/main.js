var board = [
  [
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
];

var gameOptions = {
  gameWidth: 397,
  gameHeight: 592,
  cellSize: 100,
  boardSize: {
    rows: 9,
    cols: 6
  },
  colors: [0xff0000, 0x00ff00],
}

var config = {
  type: Phaser.AUTO,
  width: gameOptions.gameWidth,
  height: gameOptions.gameHeight,
  parent: 'game-section',
  scene: {
    preload: preload,
    create: create,
    update: update
  }
}

var game = new Phaser.Game(config);

function preload() {
  this.load.image('cell', 'assets/cell.png');
}

function create() {
  for(let i=0; i<=520; i=i+65) {
    for(let j=0; j<=325; j=j+65) {
      this.add.image(j+7, i+7, 'cell').setOrigin(0, 0);
    }
  }
}

function update() {

}
