import inspect
from gae_override import httplib as gae_httplib
from python_std_lib import httplib as sockets_httplib

# Can't just do from version.httplib import * as that skips variables
# prefixed with an underscore. As this proxy should be transparent, we need
# every variable.
globals().update(gae_httplib.__dict__)


class HTTPConnection(sockets_httplib.HTTPConnection if inspect.getmodule(inspect.stack()[1][0]).__name__.startswith('requests.packages.urllib3.') else gae_httplib.HTTPConnection, object):
    pass