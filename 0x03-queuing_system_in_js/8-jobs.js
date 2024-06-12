/**
 * Function to add jobs to the 'push_notification_code_3' queue.
 * @param {Array} jobs - An array of objects containing job data.
 * @param {import('kue').Queue} queue - The queue object.
 */
export default function createPushNotificationsJobs(jobs, queue) {
  // Check if the jobs parameter is an array.
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  // Iterate over the jobs array and create a job for each object.
  jobs.forEach((jobData) => {
    // Create a job with the type 'push_notification_code_3' and the job data.
    const job = queue.create('push_notification_code_3', jobData);

    // Save the job to the queue.
    job.save((error) => {
      // If the job is saved successfully, log the job ID.
      if (!error) {
        console.log(`Notification job created: ${job.id}`);
      }
    });

    // Add event listeners for the job.
    job.on('complete', () => {
      // Log when the job is completed.
      console.log(`Notification job ${job.id} completed`);
    });

    job.on('progress', (progress) => {
      // Log the progress of the job.
      console.log(`Notification job ${job.id} ${progress}% completed`);
    });

    job.on('failed', (errorMessage) => {
      // Log when the job fails.
      console.log(`Notification job ${job.id} failed: ${errorMessage}`);
    });
  });
}
