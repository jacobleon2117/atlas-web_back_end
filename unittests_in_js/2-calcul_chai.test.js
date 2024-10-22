import calculateNumber from './2-calcul_chai.js';
import { expect } from 'chai';

describe('calculateNumber', () => {
    it('should return 3 when adding 1.4 and 1.6', () => {
        expect(calculateNumber('SUM', 1.4, 1.6)).to.equal(3);
    });

    it('should return 0 when subtracting 1.4 from 1.4', () => {
        expect(calculateNumber('SUBTRACT', 1.4, 1.4)).to.equal(0);
    });

    it('should return 2 when dividing 5 by 2.5', () => {
        expect(calculateNumber('DIVIDE', 5, 2.5)).to.equal(2);
    });

    it('should return "Error" when dividing by 0', () => {
        expect(calculateNumber('DIVIDE', 5, 0)).to.equal('Error');
    });

    it('should throw an error for invalid operation type', () => {
        expect(() => calculateNumber('INVALID', 1, 1)).to.throw('Invalid operation type');
    });
});
