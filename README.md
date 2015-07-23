# GAE Requests Library MTLS Auth Demo

A small example of requesting remote HTTPS resources authenticated with mutual TLS
(MTLS) on Google App Engine via the [Requests][requests] library.

## Why?

Mutual TLS provides several major benefits over other means of two-party authentication, such as OAuth2.
* Speed: cryptographic operations are performed by C libraries.
* Security: authentication occurs before the HTTPS server requests a resource, effectively preventing
application insecurities from being identified or exploited.
* Key Management: client certificates can be issued by a single authority which the destination server
trusts; additional clients can be created without modification to the destination server.

## Limitations

At this time, MTLS connections can be initiated from, *but not to*, Google App Engine.
If clients will need to authentication to your Google App Engine application, MTLS will unfortunately
not be an option.

The use of MTLS requires support for the Google [Sockets API][sockets-api].
As of July 2015, the Sockets API is in beta and is not covered by any SLA or depreciation policy.
Use at your own risk.

[requests]: http://docs.python-requests.org/en/latest/
[sockets-api]: https://cloud.google.com/appengine/docs/python/sockets/
