__author__ = 's7a'

# All imports
from extras import Logger
from lexus import LWLM
from webapp import WebApp


# The main method
def main():
    Logger.log_message("Running application Simplify")
    LWLM.build_tables('corpus')
    Logger.log_success("Application exited successfully")

    Logger.log_message('Running application server')
    web_app = WebApp('localhost', 8000, True)
    web_app.run()

# Call the main method
if __name__ == '__main__':
    main()