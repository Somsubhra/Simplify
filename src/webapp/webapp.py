__author__ = 's7a'

# All imports
from flask import Flask, render_template, request, jsonify
from extras import Logger
from lexus import LexicalSimplifier
from syntax import SyntacticSimplifier


# The Web Application class
class WebApp:

    # Constructor for the Web Application
    def __init__(self, host, port, debug):
        self.host = host
        self.port = port
        self.debug = debug

        self.app = Flask(__name__)

        self.syntactic_simplifier = SyntacticSimplifier()

        @self.app.route('/')
        def index():
            return render_template('index.html')

        @self.app.route('/api/simplify')
        def simplify_api():
            text = request.args['text']
            n = request.args['n']
            result = LexicalSimplifier.simplify(text, n)
            syn_result = self.syntactic_simplifier.simplify(text)
            return jsonify(success=True, result=result, syn_result=syn_result)

        Logger.log_success("Started application server successfully")

    # Run the application server
    def run(self):
        self.app.run(self.host, self.port, self.debug)