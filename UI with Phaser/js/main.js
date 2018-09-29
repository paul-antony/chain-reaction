var game;

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
  gameWidth: 700,
  gameHeight: 1050,
  cellSize: 100,
  boardSize: {
    rows: 9,
    cols: 6
  },
  directions: [
    new Phaser.Point(0, 1),
    new Phaser.Point(0, -1),
    new Phaser.Point(1, 0),
    new Phaser.Point(-1, 0),
  ]
}

window.onload = function() {
  game = new Phaser.Game(gameOptions.gameWidth, gameOptions.gameHeight);
  game.state.add("TheGame", TheGame);
  game.state.start("TheGame");
}

var TheGame = function() {};

TheGame.prototype = {
  preload: function() {
    game.stage.backgroundColor = 0x2e3131;
  },
  create: function() {
    game.scale.scaleMode = Phaser.ScaleManager.SHOW_ALL;
    game.scale.pageAlignHorizontally = true;
    game.scale.pageAlignVertically = true;
    this.createBoard();
  },
  createBoard: function() {
    this.cellsArray = [];
    this.cellGroup = game.add.group();
    this.cellGroup.x = (game.width - gameOptions.cellSize * gameOptions.boardSize.cols) / 2;
    this.cellGroup.y = (game.height - gameOptions.cellSize * gameOptions.boardSize.rows) / 2;
    for(var i = 0; i < gameOptions.boardSize.rows; i++) {
      this.cellsArray[i] = [];
      for(var j = 0; j < gameOptions.boardSize.cols; j++) {
        this.addCell(i, j);
      }
    }
    game.input.onDown.add(this.pickCell, this);
  },
  addCell: function(row, col) {
    var cellXPos = col * gameOptions.cellSize + gameOptions.cellSize / 2;
    var cellYPos = row * gameOptions.cellSize + gameOptions.cellSize / 2;
