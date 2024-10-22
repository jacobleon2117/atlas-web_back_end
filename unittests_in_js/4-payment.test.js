import { sendPaymentRequestToApi } from './4-payment.js';
import Utils from './utils.js';
import sinon from 'sinon';
import chai from 'chai';

const { expect } = chai;

describe('sendPaymentRequestToApi', () => {
    let consoleSpy;
    let calculateNumberStub;

    beforeEach(() => {
        calculateNumberStub = sinon.stub(Utils, 'calculateNumber').returns(10);
        consoleSpy = sinon.spy(console, 'log');
    });

    afterEach(() => {
        calculateNumberStub.restore();
        consoleSpy.restore();
    });

    it('should call Utils.calculateNumber with correct arguments', () => {
        sendPaymentRequestToApi(100, 20);

        expect(calculateNumberStub.calledOnce).to.be.true;
        expect(calculateNumberStub.calledWith('SUM', 100, 20)).to.be.true;
    });

    it('should log the correct message', () => {
        sendPaymentRequestToApi(100, 20);
        expect(consoleSpy.calledWith('The total is: 10')).to.be.true;
    });
});
