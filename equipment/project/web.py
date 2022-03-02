#!/usr/bin/env python

from datetime import datetime
from flask import Flask
from app.App.Container import Container


app = Flask(__name__)
app.container = Container()

log = app.container.log()
config = app.container.config()

log.info(
    f'''

    Welcome to {config.get('APP', 'name')}

    To run the web server on production run
    the following command, based on your OS:

    Linux:
    $ pip install -r requirements.txt
    $ waitress-serve --listen *:8000 web:app

    Windows:
    $ pip install -r .\\requirements.txt
    $ waitress-serve.exe --listen *:8000 web:app
    '''
)


@app.route('/')
def landing():
    log.info('Logging from Flask route!')
    return f"<p>Welcome to <b>{config.get('APP', 'name')}</b> at {str(datetime.now())}</p>"


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000
    )
