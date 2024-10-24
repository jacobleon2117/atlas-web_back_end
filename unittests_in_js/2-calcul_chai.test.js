const expect = require('chai').expect;
const calculateNumber = require('./2-calcul_chai.js')


describe('calculateNumber()', () => {
  it('return a sum of rounded a and rounded b', () => {
    const sum = 'SUM';
    expect(sum).to.be.a('string');
    expect(calculateNumber(sum, 1.6, 3.2)).to.equal(5);
    expect(calculateNumber(sum, 1.6, 3.2)).to.be.a('number');
    expect(calculateNumber(sum, 1.3, 5)).to.equal(6);
    expect(calculateNumber(sum, 1.3, 5)).to.be.a('number');
    expect(calculateNumber(sum, 2, 4.7)).to.equal(7);
    expect(calculateNumber(sum, 2, 4.7)).to.be.a('number');
  });
  it('return rounded a divided by rounded b', () => {
    const divide = 'DIVIDE';
    expect(divide).to.be.a('string');
    expect(calculateNumber(divide, 2, 1.4)).to.equal(2);
    expect(calculateNumber(divide, 2, 1.4)).to.be.a('number');
    expect(calculateNumber(divide, 5.4, 10)).to.equal(0.5);
    expect(calculateNumber(divide, 5.4, 10)).to.be.a('number');
    expect(calculateNumber(divide, 9.2, 2.7)).to.equal(3);
    expect(calculateNumber(divide, 9.2, 2.7)).to.be.a('number');
    expect(calculateNumber(divide, 123.456, 0)).to.equal('Error');
    expect(calculateNumber(divide, 123.456, 0)).to.be.a('string');
  });
  it('return rounded a minus rounded b', () => {
    const subtract = 'SUBTRACT';
    expect(subtract).to.be.a('string');
    expect(calculateNumber(subtract, 5, 2.2)).to.equal(3);
    expect(calculateNumber(subtract, 5, 2.2)).to.be.a('number');
    expect(calculateNumber(subtract, 5.4, 2)).to.equal(3);
    expect(calculateNumber(subtract, 5.4, 2)).to.be.a('number');
    expect(calculateNumber(subtract, 5.6, 2.6)).to.equal(3);
    expect(calculateNumber(subtract, 5.6, 2.6)).to.be.a('number');
  });
});
