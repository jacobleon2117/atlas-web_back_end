import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  before(() => {
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  after(() => {
    queue.testMode.exit();
    return queue.removeJobs('failed')
      .then(() => queue.removeJobs('completed'))
      .then(() => queue.removeJobs('active'))
      .catch((err) => console.error('Error clearing jobs:', err));
  });

  it('should display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');
  });

  it('should create two new jobs in the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 5678 to verify your account'
      }
    ];

    createPushNotificationsJobs(jobs, queue);

    const jobsInQueue = queue.testMode.jobs;
    expect(jobsInQueue).to.have.lengthOf(2);

    expect(jobsInQueue[0].data).to.deep.equal(jobs[0]);
    expect(jobsInQueue[1].data).to.deep.equal(jobs[1]);
  });

});
