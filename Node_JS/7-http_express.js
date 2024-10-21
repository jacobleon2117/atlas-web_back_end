// Import the required modules
const express = require('express');
const fs = require('fs');

// Create an instance of an Express app
const app = express();

// Define the port to listen on
const PORT = 1245;

// Route for the root path
app.get('/', (req, res) => {
    res.type('text/plain');
    res.send('Hello Holberton School!');
});

// Route for /students
app.get('/students', (req, res) => {
    const dbName = process.argv[2]; // Get the database name from command line arguments

    // Read the CSV file asynchronously
    fs.readFile(dbName, 'utf8', (err, data) => {
        if (err) {
            res.status(500).type('text/plain').send('Error reading database');
            return;
        }

        // Split the data into lines and filter out empty lines
        const lines = data.trim().split('\n').filter(line => line.trim() !== '');

        // Check if there are any valid student lines
        if (lines.length < 2) {
            res.type('text/plain').send('No students found');
            return;
        }

        // Get the headers and extract student names from the rest of the lines
        const students = lines.slice(1) // Skip the header line
            .map(line => line.split(',')[0]) // Extract first names
            .filter(name => name); // Filter out any undefined values

        // Prepare the response
        res.type('text/plain');
        res.send(`This is the list of our students\n${students.join('\n')}`);
    });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is listening on port ${PORT}`);
});

// Export the app
module.exports = app;
