var BottomBar = require("inquirer").ui.BottomBar,
  spawn = require("child_process").spawn,
  path = require('path');

var loader = [
  "/ Installing",
  "| Installing",
  "\\ Installing",
  "- Installing"
];

var i = 4;
var ui = new BottomBar({ bottomBar: loader[i % 4] });

setInterval(function() {
  ui.updateBottomBar( loader[i++ % 4] );
}, 300 );

var cmd = spawn("node", [ path.join(__dirname, 'bg.js') ], { stdio: "pipe" });
cmd.stdout.pipe( ui.log );
cmd.on( "close", function() {
  ui.updateBottomBar("bg done!\n");
  process.exit();
});
