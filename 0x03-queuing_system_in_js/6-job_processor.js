/* advanced redis: queuing system */
import { createQueue } from 'kue';

// initialize queue instance.
const queue = createQueue();

const sendNotification = (phoneNumber, message) => {
  console.log(
    `Sending notification to ${phoneNumber},`,
    'with message:',
    message,
  );
};

queue.process('push_notification_code', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});
