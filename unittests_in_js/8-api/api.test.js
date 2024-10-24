const request = require('supertest');
const app = require('./api');
const { expect } = require('chai');

describe('Index page', () => {
    let server;

    before((done) => {
        server = app.listen(7865, done);
    });

    after((done) => {
        server.close(done);
    });

    it('should return a status code of 200', async () => {
        const res = await request(server).get('/');
        expect(res.status).to.equal(200);
    });

    it('should return the correct result', async () => {
        const res = await request(server).get('/');
        expect(res.text).to.equal('Welcome to the payment system');
    });
});
