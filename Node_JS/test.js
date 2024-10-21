// this is for texting #0-#7 las tested on #3 read file async
const countStudents = require('./3-read_file_async');

countStudents('./database.csv')
  .then(() => console.log('Async operation complete'))
  .catch((err) => console.error(err.message));