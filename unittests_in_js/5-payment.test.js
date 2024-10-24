const sinon = require('sinon');
const sendPaymentRequestToApi = require('./4-payment.js');
const Utils = require('./utils.js');
const { assert } = require('chai');

describe('sendPaymentRequestToApi', () => {
    let spy = null;
    beforeEach(function() {
        spy = sinon.spy(console, 'log')
    });

    afterEach(function() {
        sinon.restore();
    });

    it('call sendPaymentRequestToApi with 100 and 20', () => {
        sendPaymentRequestToApi(100, 20);
        assert(spy.calledWith('The total is: 120'));
    });
    it('call sendPaymentRequestToApi with 10 and 10', () => {
        sendPaymentRequestToApi(10, 10);
        assert(spy.calledWith('The total is: 20'));
    });
});