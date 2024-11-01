from flask import (Flask, config, render_template, request, flash, json, send_file, session, jsonify, redirect, url_for)

from controllers.mascarilla_controller import MascarillaController  # Cambiado a MascarillaController

app = Flask(__name__)
app.secret_key = "crudpythonmysql"

@app.route('/')
def main():
    return MascarillaController.show_mascarillas()  # Cambiado a show_mascarillas

@app.route('/addmascarillas', methods=['POST', 'GET'])  # Cambiado a addmascarillas
def addmascarillas():
    if request.method == 'POST':
        MascarillaController.insertMascarillas()  # Cambiado a insertMascarillas
    return redirect(url_for('main'))

@app.route('/viewmascarillas', methods=['POST','GET'])  # Cambiado a viewmascarillas
def viewmascarillas():
    if request.method == 'POST':
        return MascarillaController.viewMascarillas()  # Cambiado a viewMascarillas
    
@app.route('/deletemascarillas/<string:id>', methods=['POST', 'GET'])  # Cambiado a deletemascarillas
def deletemascarillas(id): 
    if request.method == 'GET': 
       MascarillaController.deleteMascarillas(id)  # Cambiado a deleteMascarillas
    return redirect(url_for('main'))

@app.route('/updatemascarillas', methods=['GET','POST'])  # Cambiado a updatemascarillas
def updatemascarillas(): 
    if request.method == 'POST':
        MascarillaController.updateMascarillas()  # Cambiado a updateMascarillas
    return redirect(url_for('main'))
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
