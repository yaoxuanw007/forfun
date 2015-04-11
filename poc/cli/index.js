var fs = require('fs'),
  path = require('path'),
  spawn = require('child_process').spawn,
  out = fs.openSync(path.join(__dirname, 'out.log'), 'a'),
  err = fs.openSync(path.join(__dirname, 'out.log'), 'a');

var pidFile = path.join(__dirname, 'pid.json');

try {
  var data = fs.readFileSync(pidFile, { encoding: 'utf8' }),
      info = JSON.parse(data);
  if (info.pid) {
    console.log('The command (pid: %s) is still running', info.pid);
    process.exit(0);
  }
} catch (e) {
}

// long run command example
var child = spawn('node', [ path.join(__dirname, 'bg.js') ], {
  stdio: [ 'ignore', out, err ],
  detached: true
});

var content = JSON.stringify({ pid: child.pid });
fs.writeFile(pidFile, content, {
  encoding: 'utf8'
}, function (err) {
  child.unref();
  if(err) {
    return console.error(err);
  }
  console.log("The file was saved!");
});
