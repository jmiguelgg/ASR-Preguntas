from resources.Tabla3.P1 import P1
from resources.Tabla3.P2 import P2
from resources.Tabla3.P3 import P3

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

api.add_resource(P1, '/api/Tabla3/P1')
api.add_resource(P2, '/api/Tabla3/P2')
api.add_resource(P3, '/api/Tabla3/P3')

if __name__ == '__main__':
    app.run(port=5000,debug=True)