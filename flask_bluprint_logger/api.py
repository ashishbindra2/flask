# this is an example blueprint python file
from flask import Blueprint, current_app

apibp = Blueprint('api',__name__)

@apibp.route("/info")
def api_route1():
    current_app.logger.info("called from api route method1 inside blueprint")
    return "Hello World!!!"
