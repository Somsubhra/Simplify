__author__ = 's7a'

# All imports
from flask import Flask, render_template, request, jsonify
from extras import Logger
from lexus import LexicalSimplifier
from syntax import SyntacticSimplifier
from enrich import Enricher


# The Web Application class
class WebApp:

    # Constructor for the Web Application
    def __init__(self, host, port, debug):
        self.host = host
        self.port = port
        self.debug = debug

        self.app = Flask(__name__)

        self.syntactic_simplifier = SyntacticSimplifier()
        self.enricher = Enricher()

        @self.app.route('/')
        def index():
            return render_template('index.html')

        @self.app.route('/enrich')
        def enrich():
            return render_template('enrich.html')

        @self.app.route('/lexus')
        def lexus():
            return render_template('lexus.html')

        @self.app.route('/syntax')
        def syntax():
            return render_template('syntax.html')

        @self.app.route('/api/simplify')
        def simplify_api():
            text = request.args['text']
            n = request.args['n']

            lex_result = LexicalSimplifier.simplify(text, n)
            syn_result = self.syntactic_simplifier.simplify(text)

            result = {
                "lexical": lex_result,
                "syntactic": syn_result
            }

            return jsonify(success=True, result=result)

        @self.app.route('/api/enrich')
        def enrich_api():
            text = request.args['text']
            result = self.enricher.enrich(text)
            return jsonify(success=True, result=result)

        @self.app.route('/api/lexus/simplify')
        def lexus_simplify_api():
            text = request.args['text']
            n = request.args['n']

            result = LexicalSimplifier.simplify(text, n)
            return jsonify(success=True, result=result)

        @self.app.route('/api/syntax/simplify')
        def syntax_simplify_api():
            text = request.args['text']

            result = self.syntactic_simplifier.simplify(text)
            return jsonify(success=True, result=result)

        Logger.log_success("Started application server successfully")

    # Run the application server
    def run(self):
        self.app.run(self.host, self.port, self.debug)