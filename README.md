# groupme_photo_bot

A simple, lightweight service triggered by keywords in a GroupMe chat group that sends images and messages on demand.

The service is hosted on Heroku, which provided an easy (and free) way to set up a gunicorn-based python webserver. Flask more than serves
the purpose of handling HTTP POST requests, and python requests communicates back to the GroupMe API.

Notes:
- Images must be hosted on GroupMe and first uploaded with their Image Service, which generates a url to the image. The outgoing message
to the group accepts that URL for posting.
- A random image and message are chosen eat time the bot is invoked - the list of image URLs and phrases are stored in text files within
the directory. This could/should be somewhere like S3, but for now a new commit is required to update the images/phrases.
- Heroku made it ridiculously easy to get the server set up and running. The git integration was really nice too. AWS would have been nice to
explore but is probably overkill here.
