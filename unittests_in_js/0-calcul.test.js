// 0-calcul.test.js
const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
    it('should return 4 when inputs are 1.4 and 2.6', () => {
        assert.strictEqual(calculateNumber(1.4, 2.6), 4);
    });

    it('should return 4 when inputs are 1.5 and 2.4', () => { // Updated expected value
        assert.strictEqual(calculateNumber(1.5, 2.4), 4);
    });

    it('should return 0 when inputs are 0.1 and -0.4', () => {
        assert.strictEqual(calculateNumber(0.1, -0.4), 0);
    });

    it('should return -5 when inputs are -2.7 and -1.8', () => {
        assert.strictEqual(calculateNumber(-2.7, -1.8), -5);
    });

    it('should return 0 when inputs are 0 and 0', () => {
        assert.strictEqual(calculateNumber(0, 0), 0);
    });

    it('should return the rounded sum of negative and positive numbers', () => {
        assert.strictEqual(calculateNumber(1.7, -1.2), 1);
    });
});
