const getPaymentTokenFromApi = require('./6-payment_token.js');
const { expect, assert } = require('chai');

describe('getPaymentTokenFromApi()', () => {
    it('return {data: "Successful response from the API" } when successful', (done) => {
        getPaymentTokenFromApi(true)
        .then((data) => {
            const expected = {data: 'Successful response from the API' };
            assert.equal(expected.data, data.data);
            done();
        });
    });
});