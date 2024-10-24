const assert = require('assert');
const calculateNumber = require('./0-calcul.js')

describe('calculateNumber()', () => {
  it('return a sum of the rounded integers', () => {
    assert.equal(calculateNumber(1.6, 3.2), 5);
    assert.equal(calculateNumber(1.3, 5), 6);
    assert.equal(calculateNumber(2, 4.7), 7);
  })
});