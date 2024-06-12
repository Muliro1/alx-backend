import { createQueue } from 'kue';

const blacklistedNumbers = ['4153518780', '4153518781'];
const queue = createQueue();


/**
 * Handles notification jobs for the 'push_notification_code_2' queue.
 *
 * @param {string} phoneNumber - The user's phone number.
 * @param {string} message - The push notification message.
 * @param {import('kue').Job} job - The queue job.
 * @param {import('kue').DoneCallback} done - The done callback.
 * @returns {void}
 */
function sendNotification(phoneNumber, message, job, done) {
  // Update the job progress to 0%
  job.progress(0, 100);

  // Check if the phone number is blacklisted
  if (blacklistedNumbers.some((number) => number === phoneNumber)) {
    // If the phone number is blacklisted, call the done callback with an error
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    return;
  }

  // Update the job progress to 50%
  job.progress(50, 100);

  // Log the notification details
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // Call the done callback to indicate that the job is complete
  done();
}

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
