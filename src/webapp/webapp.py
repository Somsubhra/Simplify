__author__ = 's7a'

# All imports
from flask import Flask, render_template, request, jsonify
from extras import Logger


# The Web Application class
class WebApp:

    # Constructor for the Web Application
    def __init__(self, host, port, debug):
        self.host = host
        self.port = port
        self.debug = debug

        self.app = Flask(__name__)

        @self.app.route('/')
        def index():
            return "test"

        Logger.log_success("Started application server successfully")

    # Run the application server
    def run(self):
        self.app.run(self.host, self.port, self.debug)