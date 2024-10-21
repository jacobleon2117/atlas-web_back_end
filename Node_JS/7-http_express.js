const express = require('express');
const fs = require('fs');

const app = express();

const PORT = 1245;

app.get('/', (req, res) => {
    res.type('text/plain');
    res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
    const dbName = process.argv[2];
    fs.readFile(dbName, 'utf8', (err, data) => {
        if (err) {
            res.status(500).type('text/plain').send('Error reading database');
            return;
        }

        const lines = data.trim().split('\n').filter(line => line.trim() !== '');

        if (lines.length < 2) {
            res.type('text/plain').send('No students found');
            return;
        }

        const students = lines.slice(1)
            .map(line => line.split(',')[0])
            .filter(name => name);

        res.type('text/plain');
        res.send(`This is the list of our students\n${students.join('\n')}`);
    });
});

app.listen(PORT, () => {
    console.log(`Server is listening on port ${PORT}`);
});

module.exports = app;
