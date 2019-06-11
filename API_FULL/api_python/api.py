from resources.Tabla3.P1 import T3_P1
from resources.Tabla3.P2 import T3_P2
from resources.Tabla3.P3 import T3_P3
from resources.Tabla4.P1 import T4_P1
from resources.Tabla4.P2 import T4_P2
from resources.Tabla6.P1 import T6_P1
from resources.Tabla6.P2 import T6_P2

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

api.add_resource(T3_P1, '/api/Tabla3/P1')
api.add_resource(T3_P2, '/api/Tabla3/P2')
api.add_resource(T3_P3, '/api/Tabla3/P3')
api.add_resource(T4_P1, '/api/Tabla4/P1')
api.add_resource(T4_P2, '/api/Tabla4/P2')
api.add_resource(T6_P1, '/api/Tabla6/P1')
api.add_resource(T6_P2, '/api/Tabla6/P2')

if __name__ == '__main__':
    app.run(port=5000,debug=True)