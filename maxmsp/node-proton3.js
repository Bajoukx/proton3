const maxAPI = require("max-api");
const { spawn } = require('child_process');
// The path to the script that is gonna be execute
const path = 'script.py' 

/*
    Defining the function that takes care off calling 
    the execution of the python script
*/

const pythonScript = (scriptPath, data) => {
    const python = spawn('python3', [scriptPath, data]);
    return new Promise((resolve, reject) => {
      let result = ""
      python.stdout.on('data', (data) => {
        result += data
        /* print from python to MaxMSP console */
        console = data.toString()
        // maxAPI.post(console)
        /*  
            in order to avoid clashing with read and write
            and trigger the reading of the JSON file 
            we are sending back the data value (meaning the input value from MaxMSP)
            allows to say 'ok, python has compiled and saved the file'
        */
        if (console == data) {
          outputJSON()
        }
      });
      python.on('close', () => {
        resolve(result)
      });
      python.on('exit', () => {
        resolve(result)
      });
      python.on('error', (err) => {
        reject(err)
        maxAPI.post(err)
      });
    })
}

/* 
    This function takes the {data} saved in the file data.json 
    and sends them on the output of the node.script module in MaxMSP.
*/

const outputJSON = () => {
    fs = require('fs')
    fs.readFile('./data.json', 'utf8', function (err, data) {
      if (err) {
        return maxAPI.outlet(err)
      }
      x = JSON.parse(data)
      maxAPI.outlet(x.data)
    });
}

/*
    A MaxMSP handler is used to call the function 
    in addition the handler is also passing a value from
    the MaxMSP environment into this nodejs script
*/ 

maxAPI.addHandler('sendValue', (input) => {
  pythonScript(path, input);
});






