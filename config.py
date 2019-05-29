class Config(object):
    NUM_DOMAINS = None
    FILE_URL = 'http://localhost:8020/updates.html'
    HOST_IP = '34.235.226.40'
    DB_NAME = 'giselletest'
    ADD_REGEX = r'New Spyware DNS C2 Signatures'
    REM_REGEX = r'Old Spyware DNS C2 Signatures'
    VER_REGEX = r'^[0-9]+$'
    USE_CURR_DATE = False # TODO maybe not this and the next line but idk w/e
    ALT_DATE = '1970-01-01'

class DebugConfig(Config):
    NUM_DOMAINS = 1000
    HOST_IP = '10.54.92.70'

class BreakingConfig(Config):
    HOST_IP = 'abjc;aw'