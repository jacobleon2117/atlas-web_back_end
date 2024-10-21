import request from 'supertest';
import { expect } from 'chai';
import app from '../full_server/server.js';

describe('Server API', () => {
    describe('GET /', () => {
        it('should return Hello Holberton School!', async () => {
            const response = await request(app).get('/');
            expect(response.status).to.equal(200);
            expect(response.text).to.equal('Hello Holberton School!');
        });
    });

    describe('GET /students', () => {
        it('should return the list of students', async () => {
            const response = await request(app).get('/students');
            expect(response.status).to.equal(200);
            expect(response.text).to.contain('This is the list of our students');
        });
    });

    describe('GET /students/CS', () => {
        it('should return the list of CS students', async () => {
            const response = await request(app).get('/students/CS');
            expect(response.status).to.equal(200);
            expect(response.text).to.contain('List:');
        });
    });
});
