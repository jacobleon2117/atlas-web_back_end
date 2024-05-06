export default class HolbertonClass {
    constructor(size, location) {
      this.size = size;
      this.location = location;
    }
  
    toString() {
      return this.location;
    }
  
    valueOf() {
      return this.size;
    }
  
    set size(val) {
      if (typeof (val) === 'number') {
        this._size = val;
      } else {
        throw TypeError('size must be a number');
      }
    }
  
    get size() {
      return this._size;
    }
  
    set location(val) {
      if (typeof (val) === 'string') {
        this._location = val;
      } else {
        throw TypeError('location must be a string');
      }
    }
  
    get location() {
      return this._location;
    }
  }