from flask_restful import Resource

lista_especializacoes = ['pediatra', 'ortopedista', 'clinico geral']

class Especializacoes(Resource):
    def get(self):
        return lista_especializacoes
