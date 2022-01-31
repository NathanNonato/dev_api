from flask_restful import Resource
import json
from flask import request


lista_habilidades = [
    {
        'habilidade': 'Python'
    },

    {
        'habilidade': 'Java'
    },

    {
        'habilidade': 'Flask'
    },

    {
        'habilidade': 'PHP'
    }]


class ListaHabilidades(Resource):
    def get(self):
        return lista_habilidades

    def post(self):
        dados = json.loads(request.data)
        posicao = len(lista_habilidades)
        lista_habilidades.append(dados)
        return lista_habilidades[posicao]


class Habilidades(Resource):
    def put(self, id):
        dados = json.loads(request.data)
        lista_habilidades[id] = dados
        return dados

    def delete(self, id):
        lista_habilidades.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excluido'}