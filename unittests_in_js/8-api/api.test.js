const axios = require('axios');
const { expect, assert } = require('chai');

describe('API index page integration test', () => {
    it('should return a successful status code and the landing message', () => {
        axios.get('localhost:7865/').then((res) => {
            assert.equal(res.status, 200);
            assert.equal(res.data, 'Welcome to the payment system');
        });
    });
});