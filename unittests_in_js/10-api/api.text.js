const axios = require('axios');
const { expect } = require('chai');

describe('Payment API', () => {
    const baseUrl = 'http://localhost:7865';

    describe('Index Route', () => {
        it('should return a successful status code and the landing message', async () => {
            const res = await axios.get(`${baseUrl}/`);
            expect(res.status).to.equal(200);
            expect(res.data).to.equal('Welcome to the payment system');
        });
    });

    describe('Cart Route', () => {
        it('should return a successful status code with a valid ID', async () => {
            const res = await axios.get(`${baseUrl}/cart/12`);
            expect(res.status).to.equal(200);
            expect(res.data).to.equal('Payment methods for cart ID: 12');
        });

        it('should return a 404 status with an invalid ID', async () => {
            try {
                await axios.get(`${baseUrl}/cart/twelve`);
            } catch (error) {
                expect(error.response.status).to.equal(404);
                expect(error.response.data).to.equal('Cart not found');
            }
        });
    });

    describe('Available Payments Route', () => {
        it('should return the available payment methods', async () => {
            const res = await axios.get(`${baseUrl}/available_payments`);
            expect(res.status).to.equal(200);
            expect(res.data).to.deep.equal({
                payment_methods: {
                    credit_cards: true,
                    paypal: false,
                },
            });
        });
    });

    describe('Login Route', () => {
        it('should return a welcome message with a valid username', async () => {
            const res = await axios.post(`${baseUrl}/login`, { userName: 'Betty' });
            expect(res.status).to.equal(200);
            expect(res.data).to.equal('Welcome Betty');
        });

        it('should return a 400 status if username is missing', async () => {
            try {
                await axios.post(`${baseUrl}/login`, {});
            } catch (error) {
                expect(error.response.status).to.equal(400);
                expect(error.response.data).to.equal('Missing username');
            }
        });
    });
});
