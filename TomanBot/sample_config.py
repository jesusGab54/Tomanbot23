if not __name__.endswith("sample_config"):
    import sys
    print("The README is there to be read. Extend this sample config to a config file, don't just re>
          "values here. Doing that WILL backfire on you.\nBot quitting.", file=sys.stderr)
    quit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "DWPFBQ-MHGMCG-PRJUJY-NHSPWI-ARQ"
    OWNER_ID = "5516142677"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "Remnashi"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgres://dzpawnsj:2ZrIeM5vzxBhW8N4R6C_9nJTsZ2pWhcF@raja.db.elephant>
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS =[ 921396580, 954299697, 5010209835, 5676170494, 5492224551, 551614267]  # List of id>
    SUPPORT_USERS = [921396580, 954299697, 5010209835, 5676170494, 5492224551, 5516142677]  # List o>
    WHITELIST_USERS =[921396580, 954299697, 5010209835, 5676170494, 5492224551, 5516142677]  # List >
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = False
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself wh>
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker
    ALLOW_EXCL = False  # Allow ! commands as well as /
    BMERNU_SCUT_SRELFTI = 0

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
