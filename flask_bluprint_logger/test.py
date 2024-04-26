from flask import has_request_context, request, Flask
import logging

logger = logging.getLogger()
consoleHandler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s:%(name)s: %(levelname)s: %(message)s', datefmt='%d-%m-%Y %I:%M:%S %p')

consoleHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)

app = Flask(__name__)

@app.route("/")
def home():
    app.logger.info("Calling from request handler...")
    return "Hello World!!!"

app.run(host="0.0.0.0", port=50100,debug=True)