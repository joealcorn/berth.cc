from berth.settings.common import *

DEBUG = True
TEMPLATE_DEBUG = True

try:
    from berth.settings.local_settings import *
except ImportError:
    pass
