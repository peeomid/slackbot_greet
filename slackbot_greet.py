import time
from slackclient import SlackClient

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

# Constants
CONFIG_FILE = 'bot_config.ini'

def get_direct_channel(sc, user_id):
    '''
    Get direct channel id from username
    '''
    direct_message = sc.api_call("im.open", user=user_id)
    channel = direct_message.get("channel")
    if channel:        
        channel_id = channel.get("id")
        if channel_id:
            return channel_id

    return None

def greet_new_user(sc, message):
    if sc.rtm_connect():
        print "successfully connect to the team"
        while True:            
            new_events = sc.rtm_read()
            # print new_events
            for event in new_events:                              
                event_type = event.get("type")
                event_user = event.get("user")                
                if not event_type or not event_user:
                    continue
                if event_type == "team_join":
                    # print event
                    user_id = event_user.get("id")
                    if not user_id:
                        continue
                    channel_id = get_direct_channel(sc, user_id)
                    if channel_id:                    
                        to_send = message.format(user_id)                        
                        sc.rtm_send_message(channel_id, to_send)
            # Sleep for a second
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
