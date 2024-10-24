const request = require('request');
const { expect } = require('chai');

describe('Login endpoint', () => {
    const API_URL = 'http://localhost:7865';

    it('POST /login with valid username should return correct response', (done) => {
        const options = {
            url: API_URL + '/login',
            method: 'POST',
            json: {
                userName: 'Betty'
            }
        };

        request(options, function(error, response, body) {
            expect(response.statusCode).to.equal(200);
            expect(body).to.equal('Welcome Betty');
            done();
        });
    });

    it('POST /login without username should return error', (done) => {
        const options = {
            url: API_URL + '/login',
            method: 'POST',
            json: {}
        };

        request(options, function(error, response, body) {
            expect(response.statusCode).to.equal(400);
            expect(body).to.equal('Missing username');
            done();
        });
    });
});