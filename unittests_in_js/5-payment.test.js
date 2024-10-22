import { sendPaymentRequestToApi } from './5-payment.js';
import Utils from './utils.js';
import sinon from 'sinon';
import chai from 'chai';

const { expect } = chai;

describe('sendPaymentRequestToApi', () => {
    let consoleSpy;

    beforeEach(() => {
        consoleSpy = sinon.spy(console, 'log');
    });

    afterEach(() => {
        consoleSpy.restore();
    });

    it('should log the correct message when called with 100 and 20', () => {
        sendPaymentRequestToApi(100, 20);

        expect(consoleSpy.calledOnce).to.be.true;
        expect(consoleSpy.calledWith('The total is: 120')).to.be.true;
    });

    it('should log the correct message when called with 10 and 10', () => {
        sendPaymentRequestToApi(10, 10);

        expect(consoleSpy.calledOnce).to.be.true;
        expect(consoleSpy.calledWith('The total is: 20')).to.be.true;
    });
});
