// 1-calcul.test.js

import assert from 'assert';
import calculateNumber from './1-calcul.js';

describe('calculateNumber', () => {
    // Test case for SUM
    it('should return the sum of rounded numbers', () => {
        assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
        assert.strictEqual(calculateNumber('SUM', 1.2, 3.7), 5);
        assert.strictEqual(calculateNumber('SUM', 1.5, 3.5), 6);
    });

    it('should return the difference of rounded numbers', () => {
        assert.strictEqual(calculateNumber('SUBTRACT', 4.5, 1.4), 4); // 5 - 1 = 4
        assert.strictEqual(calculateNumber('SUBTRACT', 1.5, 3.7), -2); // 2 - 4 = -2
    });

    // Test case for DIVIDE
    it('should return the division of rounded numbers', () => {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2); // 1 - 5 = 0.2
    });

    // Test case for DIVIDE by zero
    it('should return "Error" when dividing by zero', () => {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });

    // Test case for invalid operation type
    it('should throw an error for invalid operation type', () => {
        assert.throws(() => calculateNumber('INVALID', 1.4, 4.5), {
            message: 'Invalid operation type'
        });
    });
});
