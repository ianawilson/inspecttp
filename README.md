Tiny little Django app for inspecting arbitrary requests. Useful for debugging
webhooks from a service or device you don't control.

Each time a request is made, the server drops into a pdb interactive shell.
See http://docs.python.org/library/pdb.html for more info about pdb.

- You'll probably want to start the server with `manage.py runserver 0.0.0.0:8000`.
- The `request` is available for your inspection.
- Type `c` when you are done to let the server respond with an HTTP 200.
- `^C` or `^D` will break the connection, sending a bad response to your client.
- Beware of client-side timeouts. The server will not timeout on its own.
