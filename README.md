InspecTTP
=========

Tiny little Django app for inspecting arbitrary HTTP requests. Useful for
debugging or playing with webhooks from a blackbox service or device.

Each time a request is made to this, the server drops into a pdb interactive shell.
See http://docs.python.org/library/pdb.html for more info about pdb.

Quick start
-----------

- You'll probably want to start the server with `manage.py runserver 0.0.0.0:8000`.
- The `request` is available for your inspection.
- Type `c` when you are done to let the server respond with an HTTP 200.
- `^C` or `^D` will break the connection, sending a bad response to your client.
- Beware of client-side timeouts. The server will not timeout on its own.
