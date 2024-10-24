const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
    it('should return the sum of two rounded numbers', () => {
        assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
        assert.strictEqual(calculateNumber('SUM', 2.2, 2.7), 5);
    });

    it('should return the difference of two rounded numbers', () => {
        assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
        assert.strictEqual(calculateNumber('SUBTRACT', 5.5, 3.3), 3);
    });

    it('should return the quotient of two rounded numbers', () => {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
        assert.strictEqual(calculateNumber('DIVIDE', 9.8, 4.0), 2.5);
    });

    it('should return "Error" when dividing by zero', () => {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
        assert.strictEqual(calculateNumber('DIVIDE', 0, 0), 'Error');
    });

    it('should throw an error for invalid operation types', () => {
        assert.throws(() => {
            calculateNumber('INVALID', 1, 2);
        }, /Invalid operation type/);
    });
});
