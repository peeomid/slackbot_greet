import time
from slackclient import SlackClient

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

# Constants
CONFIG_FILE = 'bot_config.ini'

def greet_new_user(sc, message):
	if sc.rtm_connect():
	    while True:
			new_events = sc.rtm_read()
			for event in new_evts:				
		        event_type = event.get("type")
		        event_user = event.get("user")
		        if not event_type or not event_user:
		            continue
		        sc.rtm_send_message("general", message.format(user))
	        # Sleep for half a second
            time.sleep(1)
	else:
	    print "There's error connecting to slack, please check configuration or contact support engineer"


if __name__ == "__main__":
	# Gather configuration
    bot_config = configparser.ConfigParser()
    bot_config.read(CONFIG_FILE)
    api_key = bot_config.get("bot", "apikey")
    message = bot_config.get("bot", "message")

    sc = SlackClient(api_key)
    greet_new_user(sc, message)
