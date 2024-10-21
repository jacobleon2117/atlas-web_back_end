const countStudents = require('./3-read_file_async');

countStudents('./database.csv')
  .then(() => console.log('Async operation complete'))
  .catch((err) => console.error(err.message));