const sinon = require('sinon');
const sendPaymentRequestToApi = require('./3-payment.js');
const Utils = require('./utils.js');
const { assert } = require('chai');

describe('sendPaymentRequestToApi', () => {
    beforeEach(function() {
        sinon.spy(Utils, 'calculateNumber')
    });

    afterEach(function() {
        sinon.restore();
    });

    it('should match math of sendPaymentRequest and calculateNumber', () => {
        sendPaymentRequestToApi(100, 20);
        assert(Utils.calculateNumber.calledOnce);
    });
});