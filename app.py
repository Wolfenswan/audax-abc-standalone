from flask import Flask
from werkzeug import run_simple
from werkzeug.middleware.profiler import ProfilerMiddleware

from routes import adx_abctrainer_bp

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
app.register_blueprint(adx_abctrainer_bp)

if __name__ == '__main__':
    app.run()