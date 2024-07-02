const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const { exec } = require('child_process');
const path = require('path');

const app = express();
const port = 3001;

app.use(cors());
app.use(bodyParser.json());
app.use(express.static('images')); // Serve images statically

app.post('/run-script', (req, res) => {
    exec('python3 script.py', (error, stdout, stderr) => {
        if (error) {
            console.error(`Execution error: ${error.message}`);
            return res.status(500).send(`Execution error: ${error.message}`);
        }
        if (stderr) {
            console.error(`Execution stderr: ${stderr}`);
            return res.status(500).send(`Execution stderr: ${stderr}`);
        }
        console.log(`Execution stdout: ${stdout}`);
        res.status(200).send('Script executed successfully');
    });
});

app.listen(port, () => {
    console.log(`Server listening at http://localhost:${port}`);
});
