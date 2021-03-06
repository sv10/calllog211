from flask import Flask
from flask.ext.restful import Api
from flask.ext.restful.utils import cors

from api import config
from api.calllog.CallLogAPI import CallLogAPI, CallLogQuery

app = Flask(__name__)
app.config.from_object(config)

api = Api(app, decorators=[cors.crossdomain(origin='*')])

# public services
api.add_resource(CallLogAPI, CallLogAPI.route())
api.add_resource(CallLogQuery, CallLogQuery.route())
