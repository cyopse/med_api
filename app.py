from flask import Flask, jsonify, request
from flask.wrappers import Request
import json

app = Flask(__name__)

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

#devolve, altera e deleta medico por id(read one, update and delete)
@app.route('/med/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def medico(id):
    if request.method == 'GET':
        try:
            response = medicos[id]
        except IndexError:
            mensagem = 'medico de id {} nao existe'.format(id)
            response = {'status':'erro', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido'
            response = {'status':'erro', 'mensagem':mensagem}
        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        medicos[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        medicos.pop(id)
        return jsonify({'status':'sucesso', 'mensagem':'o registro foi excluido'})

#lista e inclui medicos (create and read all)
@app.route('/med/', methods=['POST', 'GET'])
def lista_medicos():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(medicos)
        dados['id'] = posicao
        medicos.append(dados)
        return jsonify(medicos[posicao])
    elif request.method == 'GET':
        return jsonify(medicos)


if __name__ == '__main__':
    app.run(debug=True)
