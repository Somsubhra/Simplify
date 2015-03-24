__author__ = 's7a'

# All imports
from extras import Logger
from lexus import LWLM
from webapp import WebApp
from subprocess import call
import sys
from os import stat


# Clean up all files
def cleanup():
    Logger.log_message('Cleaning up')
    call(['rm', '-rf', 'out'])
    call(['mkdir', 'out'])
    Logger.log_success('Finished cleaning up')


# Run the server
def run_server():

    try:
        stat('out')
    except:
        Logger.log_error('Data tables not built yet')
        Logger.log_message('Please run ./run first')
        return

    Logger.log_message('Running application server')
    web_app = WebApp('localhost', 8000, True)
    web_app.run()


# The main method
def main():

    if len(sys.argv) > 1:
        if sys.argv[1] == 'server':
            run_server()
            return

    Logger.log_message("Running application Simplify")
    cleanup()
    LWLM.build_tables('corpus')
    Logger.log_success("Application exited successfully")


# Call the main method
if __name__ == '__main__':
    main()