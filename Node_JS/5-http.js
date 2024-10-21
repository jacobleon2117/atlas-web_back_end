const http = require('http');
const fs = require('fs').promises;

const app = http.createServer(async (req, res) => {
  const url = req.url === '/' ? '/' : '/students';

  try {
    if (url === '/') {
      res.writeHead(200, { 'Content-Type': 'text/plain' });
      await res.end('Hello Holberton School!');
    }
    
    else if (url === '/students') {
      const dbFile = process.argv[process.argv.length - 1];
      
      const csvData = await fs.readFile(dbFile, 'utf8');
      
      const students = parseCsv(csvData);
      
      const totalStudents = countStudents(students);
      const csStudents = countCsStudents(students);
      
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

function parseCsv(data) {
}

function countStudents(students) {
}

function countCsStudents(students) {
}

function countStudentsInList(list) {
}

module.exports = app;
