## flask TODO app

### Create an environment
`py -3 -m venv .venv`

activate the enviroment
`.venv\Scripts\activate`

### Install Flask
`pip install Flask`

These distributions will be installed automatically when installing Flask.

    Werkzeug implements WSGI, the standard Python interface between applications and servers.

    Jinja is a template language that renders the pages your application serves.

    MarkupSafe comes with Jinja. It escapes untrusted input when rendering templates to avoid injection attacks.

    ItsDangerous securely signs data to ensure its integrity. This is used to protect Flask’s session cookie.

    Click is a framework for writing command line applications. It provides the flask command and allows adding custom management commands.

    Blinker provides support for Signals.

### To run a flask application
To run the application, use the flask command or python -m flask.
`flask --app app run`<br>
`flask run --host = 0.0.0.0`
- --app: instance name
- app: app.py file name

if the file is named app.py or wsgi.py, you don’t have to use --app.

### Install 
`pip install -e .`

### Run
`flask --app todo init-db`
`flask --app todo run`