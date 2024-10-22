import { getPaymentTokenFromAPI } from './6-payment_token.js';
import chai from 'chai';

const { expect } = chai;

describe('getPaymentTokenFromAPI', () => {
    it('should return a successful response when success is true', (done) => {
        getPaymentTokenFromAPI(true).then((response) => {
            expect(response).to.deep.equal({ data: 'Successful response from the API' });
            done();
        });
    });

    it('should reject when success is false', (done) => {
        getPaymentTokenFromAPI(false).then(() => {
            done(new Error('Expected promise to be rejected'));
        }).catch((error) => {
            expect(error.message).to.equal('Failure: Not a successful response');
            done();
        });
    });
});
