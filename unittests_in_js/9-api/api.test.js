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
            const res = await axios.get(`${baseUrl}/cart/twelve`);
            expect(res.status).to.equal(404);
            expect(res.data).to.equal('Cart not found');
        });
    });

    describe('Payment Methods Route', () => {
        it('should return a list of available payment methods', async () => {
            const res = await axios.get(`${baseUrl}/payment-methods`);
            expect(res.status).to.equal(200);
            expect(res.data).to.have.property('paymentMethods').that.is.an('array');
            expect(res.data.paymentMethods).to.include.members(['Credit Card', 'PayPal', 'Bank Transfer']);
        });
    });
});
