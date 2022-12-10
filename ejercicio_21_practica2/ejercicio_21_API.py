# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 07:31:11 2022

@author: Alumno
"""

from flask import Flask, jsonify, request

app = Flask(__name__)



@app.route('/nombre', methods=['POST'])

def set_nombre():
    if request.method == 'POST':
        dato_posteado = request.get_json()
        dato = dato_posteado['dato']
        return jsonify('Almacenado correctamente {}'.format(dato))
    

@app.route('/mensaje', methods=['GET'])

def mensaje():
    dato_posteado=request.get_json()
    nombre=dato_posteado['nombre']
    return jsonify('Saludos {}'.format(nombre))

if __name__=='__main__':
    app.run(debug=True)