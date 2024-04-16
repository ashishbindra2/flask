from flask import has_request_context, request, Flask
import logging

# using custom formatter to inject contextual data into logging
class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
        else:
            record.url = None
            record.remote_addr = None
        return super().format(record)

formatter = RequestFormatter(
    '[%(asctime)s] %(remote_addr)s requested %(url)s\n'
    '%(levelname)s in %(module)s: %(message)s'
)

logger = logging.getLogger()
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)

app = Flask(__name__)

@app.route("/")
def home():
    app.logger.info("Calling from request handler...")
    return "Hello World!!!"

app.run(host="0.0.0.0", port=50100)