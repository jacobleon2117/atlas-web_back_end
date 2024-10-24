
const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', () => {
    it('should return the sum of rounded numbers', () => {
        assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
        assert.strictEqual(calculateNumber('SUM', 1.2, 3.7), 5);
    });

    it('should return the difference of rounded numbers', () => {
        assert.strictEqual(calculateNumber('SUBTRACT', 4.5, 1.4), 3);
        assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });

    it('should return the division of rounded numbers', () => {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });

    it('should return "Error" when dividing by zero', () => {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });

    it('should throw an error for invalid operation type', () => {
        assert.throws(() => calculateNumber('INVALID', 1.4, 4.5), {
            message: 'Invalid operation type'
        });
    });
});
