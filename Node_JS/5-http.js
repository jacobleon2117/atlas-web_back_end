const http = require('http');
const fs = require('fs').promises;

const app = http.createServer(async (req, res) => {
  const url = req.url === '/' ? '/' : '/students';

  try {
    // Handle root path (/)
    if (url === '/') {
      res.writeHead(200, { 'Content-Type': 'text/plain' });
      await res.end('Hello Holberton School!');
    }
    
    // Handle /students path
    else if (url === '/students') {
      const dbFile = process.argv[process.argv.length - 1];
      
      // Read the CSV file
      const csvData = await fs.readFile(dbFile, 'utf8');
      
      // Parse the CSV data
      const students = parseCsv(csvData);
      
      // Count total and CS students
      const totalStudents = countStudents(students);
      const csStudents = countCsStudents(students);
      
      // Generate the response
      const response = `
        This is the list of our students
        Number of students: ${totalStudents}
        Number of students in CS: ${csStudents}. List: ${csStudentsList}
      `;
      
      res.writeHead(200, { 'Content-Type': 'text/plain' });
      await res.end(response);
    }
  } catch (error) {
    res.writeHead(500, { 'Content-Type': 'text/plain' });
    await res.end('Error processing request');
  }
});

// Helper functions
function parseCsv(data) {
  // Implementation to parse CSV data
}

function countStudents(students) {
  // Implementation to count total students
}

function countCsStudents(students) {
  // Implementation to count CS students
}

function countStudentsInList(list) {
  // Implementation to count students in CS list
}

module.exports = app;
