const assert = require('assert');
const calculateNumber = require('./1-calcul.js')

describe('calculateNumber()', () => {
  it('should return a sum of rounded a and rounded b', () => {
    assert.equal(calculateNumber('SUM', 1.6, 3.2), 5);
    assert.equal(calculateNumber('SUM', 1.3, 5), 6);
    assert.equal(calculateNumber('SUM', 2, 4.7), 7);
  });
  it('should return rounded a divided by rounded b', () => {
    assert.equal(calculateNumber('DIVIDE', 2, 1.4), 2);
    assert.equal(calculateNumber('DIVIDE', 5.4, 10), 0.5);
    assert.equal(calculateNumber('DIVIDE', 9.2, 2.7), 3);
    assert.equal(calculateNumber('DIVIDE', 123.456, 0), 'Error');
  });
  it('should return rounded a minus rounded b', () => {
    assert.equal(calculateNumber('SUBTRACT', 5, 2.2), 3);
    assert.equal(calculateNumber('SUBTRACT', 5.4, 2), 3);
    assert.equal(calculateNumber('SUBTRACT', 5.6, 2.6), 3);
  });
});