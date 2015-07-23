import inspect
from gae_override import httplib as gae_httplib
from python_std_lib import httplib as sockets_httplib

# Can't just do from version.httplib import * as that skips variables
# prefixed with an underscore. As this proxy should be transparent, we need
# every variable.
globals().update(gae_httplib.__dict__)

def is_called_by_requests():
    # Get the module that called us two operations up the stack
    caller = inspect.stack()[2]
    module = inspect.getmodule(caller[0]).__name__
    return module.startswith('requests.packages.urllib3.')

# If is_called_by_requests(), HTTPConnection should subclass python_std_lib.httplib.HTTPConnection,
# else HTTPConnection will subclass gae_override.httplib.HTTPConnection
class HTTPConnection(sockets_httplib.HTTPConnection if is_called_by_requests() else gae_httplib.HTTPConnection, object):
    pass