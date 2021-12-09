from flask import Flask, request
from flask_restful import Resource, Api
from especializacoes import Especializacoes
import json




app = Flask(__name__)
api = Api(app)

medicos = [
    {'id':'0',
     'nome':'lucas',
     'especializacao':'pediatra'
    },
    {'id':'1',
     'nome':'kaylanne',
     'especializacao':'ortopedista'
    }
]

#CRUD medico
class Medico(Resource):
    #Read one
    def get(self, id):
        try:
            response = medicos[id]
        except IndexError:
            mensagem = 'medico de id {} nao existe'.format(id)
            response = {'status':'erro', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido'
            response = {'status':'erro', 'mensagem':mensagem}
        return response
    #Update
    def put(self, id):
        dados = json.loads(request.data)
        medicos[id] = dados
        return dados
    #Delete
    def delete(self, id):
        medicos.pop(id)
        return {'status':'sucesso', 'mensagem':'registro excluído'}

class ListaMedicos(Resource):
    #Read all
    def get(self):
        return medicos

    #Create
    def post(self):
        dados = json.loads(request.data)
        posicao = len(medicos)
        dados['id'] = posicao
        medicos.append(dados)
        return medicos[posicao]

api.add_resource(Medico, '/med/<int:id>/')
api.add_resource(ListaMedicos, '/med/')
api.add_resource(Especializacoes, '/espec/')

if __name__ == '__main__':
    app.run(debug=True)
