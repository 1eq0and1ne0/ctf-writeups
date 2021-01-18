# oh-my-socket (24 solves, 465 pts)

Why just not to communicate with flag server directly (from webserver)? So I just uploaded python file, which sends requiered message and receives the flag. File should be uploaded and executed right after server restart, until "cnt" on flag server is less than 2. Seems like unintended solution.

P.S. In fact, we need to connect to flag server before "client" will do it first and block all other connections.
