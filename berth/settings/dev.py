from berth.settings.common import *

DEBUG = True
TEMPLATE_DEBUG = True
SESSON_COOKIE_SECURE = False

try:
    from berth.settings.local_settings import *
except ImportError:
    pass
