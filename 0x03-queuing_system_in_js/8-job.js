/* advanced redis: queuing system */
import { Queue, Job } from 'kue';

/**
 * Creates push notification jobs.
 */
export const createPushNotificationsJobs = (jobs, queue) => {
  // check job's existence.
  if (!(jobs instanceof Array)) {
    throw new Error('Jobs is not an array');
  }
  for (const jobInfo of jobs) {
    const job = queue.create('push_notification_code_3', jobInfo);

    job
      .on('enqueue', () => {
        console.log('Notification job created:', job.id);
      })
      .on('complete', () => {
        console.log('Notification job', job.id, 'completed');
      })
      .on('failed', (err) => {
        console.log('Notification job', job.id, 'failed:', err.message || err.toString());
      })
      .on('progress', (progress, _data) => {
        console.log('Notification job', job.id, `${progress}% complete`);
      });
    job.save();
  }
};

// default exports:
export default createPushNotificationsJobs;
