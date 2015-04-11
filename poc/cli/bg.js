#!/usr/bin/env node

var fs = require('fs'),
  path = require('path'),
  program = require('commander');

program
.version('0.0.1')
.usage('test')
.option('-s --size <size>', 'Pizza size', /^(large|medium|small)$/i, 'medium')
.option('-d --drink [drink]', 'Drink', /^(coke|pepsi|izze)$/i)
.parse(process.argv);

setTimeout(function() {
  console.log(' size: %j', program.size);
  console.log(' drink: %j', program.drink);

  fs.writeFile(path.join(__dirname, 'pid.json'), JSON.stringify({
      pid: ''
    }), function(err) {
      if(err) {
        return console.error(err);
      }
      console.log("The file was saved!");
  });
}, 5000);

