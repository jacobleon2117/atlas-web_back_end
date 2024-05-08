export default class Car {
  constructor(brand, motor, color) {
    this.brand = brand;
    this.motor = motor;
    this.color = color;
  }

  set brand(val) {
    this._brand = val;
  }

  get brand() {
    return this._brand;
  }

  set motor(val) {
    this._motor = val;
  }

  get motor() {
    return this._motor;
  }

  set color(val) {
    this._color = val;
  }

  get color() {
    return this._color;
  }

  cloneCar() {
    return new this.constructor();
  }
}
