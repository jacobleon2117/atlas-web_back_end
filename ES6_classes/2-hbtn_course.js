export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof (name) === 'string') {
      this._name = name;
    } else {
      throw TypeError('Name must be a string');
    }
    if (typeof (length) === 'number') {
      this._length = length;
    } else {
      throw TypeError('Length must be a number');
    }
    if (Array.isArray(students)) {
      this._students = students;
    } else {
      throw TypeError('Students must be an array');
    }
  }

  set name(val) {
    if (typeof (val) === 'string') {
      this._name = val;
    } else {
      throw TypeError('Name must be a string');
    }
  }

  get name() {
    return this._name;
  }

  set length(val) {
    if (typeof (val) === 'number') {
      this._length = val;
    } else {
      throw TypeError('Length must be a number');
    }
  }

  get length() {
    return this._length;
  }

  set students(arr) {
    if (Array.isArray(arr)) {
      this._students = arr;
    } else {
      throw TypeError('Students must be an array');
    }
  }

  get students() {
    return this._students;
  }
}
