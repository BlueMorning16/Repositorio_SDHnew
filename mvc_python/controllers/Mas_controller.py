from flask import (Flask, render_template, request, flash, jsonify)
from models.mascarilla_model import MascarillaModel

class MascarillaController:
    @staticmethod
    def show_mascarillas():
        mascarilla_model = MascarillaModel()
        tbmascarillas = mascarilla_model.get_all_mascarillas()
        mascarilla_model.close()
        return render_template('index.html', tbmascarillas=tbmascarillas)
    
    @staticmethod
    def viewMascarillas():
        try:
            mascarilla_model = MascarillaModel()
            id = request.form['id']
            data = mascarilla_model.get_one_mascarilla(id)
            mascarilla_model.close()
            return jsonify({'htmlresponse': render_template('viewmascarilla.html', mascarillas=data)})
        except:
            flash('¡Ha ocurrido un error!')
    
    @staticmethod
    def insertMascarillas():
        try:
            mascarilla_model = MascarillaModel()
            nombre = request.form['nombre']
            marca = request.form['marca']
            tipo_piel = request.form['tipo_piel']
            ingredientes_clave = request.form['ingredientes_clave']
            beneficios = request.form['beneficios']
            precio = request.form['precio']
            opiniones = request.form['opiniones']
            mascarilla_model.insert_mascarilla(nombre, marca, tipo_piel, ingredientes_clave, beneficios, precio, opiniones)
            mascarilla_model.close()
            flash('Mascarilla registrada correctamente!!!')      
        except:
            flash('¡Ha ocurrido un error!')
    
    @staticmethod
    def deleteMascarillas(id):
        try:
            mascarilla_model = MascarillaModel()
            mascarilla_model.delete_mascarilla(id)
            mascarilla_model.close()
            flash('Mascarilla eliminada correctamente!!!') 
        except:
            flash('¡Ha ocurrido un error!')

    @staticmethod
    def updateMascarillas():
        try:
            mascarilla_model = MascarillaModel()
            id = request.form['id']
            nombre = request.form['nombre']
            marca = request.form['marca']
            tipo_piel = request.form['tipo_piel']
            ingredientes_clave = request.form['ingredientes_clave']
            beneficios = request.form['beneficios']
            precio = request.form['precio']
            opiniones = request.form['opiniones']
            mascarilla_model.update_mascarilla(id, nombre, marca, tipo_piel, ingredientes_clave, beneficios, precio, opiniones)
            mascarilla_model.close()
            flash('Mascarilla actualizada correctamente!!!')      
        except:
            flash('¡Ha ocurrido un error!')
