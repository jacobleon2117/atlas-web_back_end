const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    
    const lines = data.trim().split('\n');
    
    if (lines.length <= 1) {
      console.log('Number of students: 0');
      return;
    }

    const fields = {};
    let totalStudents = 0;

    for (let i = 1; i < lines.length; i++) {
      const line = lines[i].trim();
      if (line) {
        const [firstname, , , field] = line.split(',');

        if (fields[field]) {
          fields[field].push(firstname);
        } else {
          fields[field] = [firstname];
        }
        totalStudents++;
      }
    }

    console.log(`Number of students: ${totalStudents}`);

    for (const field in fields) {
      const studentsList = fields[field].join(', ');
      console.log(`Number of students in ${field}: ${fields[field].length}. List: ${studentsList}`);
    }

  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
