const request = require('request');
const { expect } = require('chai');

describe('Payment API', () => {
    const baseUrl = 'http://localhost:7865';

    describe('Index page', () => {
        it('should return correct status code when GET /', (done) => {
            request.get(baseUrl + '/', (_err, res, body) => {
                expect(res.statusCode).to.equal(200);
                expect(body).to.equal('Welcome to the payment system');
                done();
            });
        });
    });

    describe('Cart page', () => {
        it('should return status code 200 when :id is a number', (done) => {
            request.get(baseUrl + '/cart/12', (_err, res, body) => {
                expect(res.statusCode).to.equal(200);
                expect(body).to.equal('Payment methods for cart 12');
                done();
            });
        });

        it('should return status code 404 when :id is NOT a number', (done) => {
            request.get(baseUrl + '/cart/hello', (_err, res, body) => {
                expect(res.statusCode).to.equal(404);
                expect(body).to.equal('Cart not found');
                done();
            });
        });
    });

    describe('Available payments', () => {
        it('should return correct payment methods', (done) => {
            request.get(baseUrl + '/available_payments', (_err, res, body) => {
                expect(res.statusCode).to.equal(200);
                expect(JSON.parse(body)).to.deep.equal({
                    payment_methods: {
                        credit_cards: true,
                        paypal: false
                    }
                });
                done();
            });
        });
    });

    describe('Login', () => {
        it('should return welcome message with valid username', (done) => {
            request.post({
                url: baseUrl + '/login',
                json: { userName: 'Betty' }
            }, (_err, res, body) => {
                expect(res.statusCode).to.equal(200);
                expect(body).to.equal('Welcome Betty');
                done();
            });
        });

        it('should return error when username is missing', (done) => {
            request.post({
                url: baseUrl + '/login',
                json: {}
            }, (_err, res, body) => {
                expect(res.statusCode).to.equal(400);
                expect(body).to.equal('Missing username');
                done();
            });
        });
    });
});