Slack bot to greet new user joining a team, making used of SlackClient.

To deploy this Slack bot, you will need to set up a python environment.

With the assumption that you already have a python environment, you'll need to:

- Install required packages:
`pip install -r requirements.txt'
- Change the configuration in `bot_config.ini` file. More specifically, you'll need to get API key from slack team and put it in there. The current key is for the test team `ebayL3Collaboration`.
- Run following command to connect the bot to slack, and leave it there. It would be great idea to run it as daemon.
`python slackbot_greet.py`

And now you can test out by inviting a new user, and check direct message of that user.