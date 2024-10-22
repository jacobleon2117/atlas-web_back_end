const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
    describe('SUM', () => {
        it('should return 6 when inputs are 1.4 and 4.5', () => {
            assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
        });

        it('should return 5 when inputs are 1.5 and 2.4', () => {
            assert.strictEqual(calculateNumber('SUM', 1.5, 2.4), 4);
        });
    });

    describe('SUBTRACT', () => {
        it('should return -4 when inputs are 1.4 and 4.5', () => { // Corrected the expected value to -4
            assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
        });
    
        it('should return 0 when inputs are 2.5 and 2.5', () => {
            assert.strictEqual(calculateNumber('SUBTRACT', 2.5, 2.5), 0);
        });
    });

    describe('DIVIDE', () => {
        it('should return 0.2 when inputs are 1.4 and 4.5', () => {
            assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
        });

        it('should return "Error" when second input is 0', () => {
            assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
        });

        it('should return "Error" when rounded second input is 0', () => {
            assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0.3), 'Error');
        });

        it('should return 1 when inputs are 3.5 and 3.5', () => {
            assert.strictEqual(calculateNumber('DIVIDE', 3.5, 3.5), 1);
        });
    });
});
function calculateNumber(type, a, b) {
    const roundedA = Math.round(a);
    const roundedB = Math.round(b);

    if (type === 'SUM') {
        return roundedA + roundedB;
    }

    if (type === 'SUBTRACT') {
        return roundedA - roundedB;
    }

    if (type === 'DIVIDE') {
        if (roundedB === 0) {
            return 'Error';
        }
        return roundedA / roundedB;
    }

    throw new Error('Invalid operation type');
}

module.exports = calculateNumber;
