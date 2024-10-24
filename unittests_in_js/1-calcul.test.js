const assert = require('assert');
const calculateNumber = require('./utils'); // Adjust the path if needed

describe('calculateNumber', () => {
    // Test for SUM
    describe('SUM', () => {
        it('should return 4 for 1.4 and 2.6', () => {
            assert.strictEqual(calculateNumber('SUM', 1.4, 2.6), 4);
        });

        it('should return 5 for 2.5 and 2.5', () => {
            assert.strictEqual(calculateNumber('SUM', 2.5, 2.5), 5);
        });

        it('should return 0 for -1.5 and 1.5', () => {
            assert.strictEqual(calculateNumber('SUM', -1.5, 1.5), 0);
        });
    });

    // Test for SUBTRACT
    describe('SUBTRACT', () => {
        it('should return 3 for 5.5 and 2.2', () => {
            assert.strictEqual(calculateNumber('SUBTRACT', 5.5, 2.2), 3);
        });

        it('should return -1 for 2 and 3', () => {
            assert.strictEqual(calculateNumber('SUBTRACT', 2, 3), -1);
        });

        it('should return -1 for 2.5 and 3.5', () => {
            assert.strictEqual(calculateNumber('SUBTRACT', 2.5, 3.5), -1);
        });
    });

    // Test for DIVIDE
    describe('DIVIDE', () => {
        it('should return 4 for 10.5 and 2.5', () => {
            assert.strictEqual(calculateNumber('DIVIDE', 10.5, 2.5), 4);
        });

        it('should return 2 for 6 and 3', () => {
            assert.strictEqual(calculateNumber('DIVIDE', 6, 3), 2);
        });

        it('should return "Error" for division by 0', () => {
            assert.strictEqual(calculateNumber('DIVIDE', 5, 0), 'Error');
        });
    });

    // Test for invalid operation type
    it('should throw an error for an invalid operation type', () => {
        assert.throws(() => calculateNumber('INVALID', 1, 2), {
            name: 'Error',
            message: 'Invalid operation type',
        });
    });
});
