import kue from 'kue';

const queue = kue.createQueue();

const sendNotification = (phoneNumber, message) => {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  
  done();
});

queue.on('job complete', (id) => {
  console.log(`Notification job with ID ${id} completed`);
});

queue.on('job failed', (id, errorMessage) => {
  console.log(`Notification job with ID ${id} failed: ${errorMessage}`);
});
