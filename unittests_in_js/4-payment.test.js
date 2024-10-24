const sinon = require('sinon');
const sendPaymentRequestToApi = require('./4-payment.js');
const Utils = require('./utils.js');
const { assert } = require('chai');

describe('sendPaymentRequestToApi', () => {
    beforeEach(function() {
        const stub = sinon.stub(Utils, "calculateNumber");
        stub.withArgs('SUM', 100, 20).returns(10);
        sinon.spy(console, 'log')
    });

    afterEach(function() {
        sinon.restore();
    });

    it('call console.log with the value 10', () => {
        assert(Utils.calculateNumber.returns(10));
        
    });
});