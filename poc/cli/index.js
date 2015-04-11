var fs = require('fs'),
  path = require('path'),
  spawn = require('child_process').spawn,
  out = fs.openSync(path.join(__dirname, 'out.log'), 'a'),
  err = fs.openSync(path.join(__dirname, 'out.log'), 'a');

// long run command example
var child = spawn('node', [ path.join(__dirname, 'bg.js') ], {
  stdio: [ 'ignore', out, err ],
  detached: true
});

fs.writeFile(path.join(__dirname, 'pid.json'), JSON.stringify({
    pid: child.pid
  }), function(err) {
    child.unref();
    if(err) {
      return console.error(err);
    }
    console.log("The file was saved!");
});
