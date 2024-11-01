import mysql.connector
from config import DATABASE_CONFIG

class MascarillaModel:
    def __init__(self):
        self.connection = mysql.connector.connect(**DATABASE_CONFIG)
        self.cursor = self.connection.cursor(dictionary=True)

    def get_all_mascarillas(self):
        self.cursor.execute("SELECT * FROM tbmascarillas")
        result = self.cursor.fetchall()
        return result
    
    def insert_mascarilla(self, nombre, marca, tipo_piel, ingredientes_clave, beneficios, precio, opiniones):
        try:
            self.cursor.execute(
                'INSERT INTO tbmascarillas(nombre, marca, tipo_piel, ingredientes_clave, beneficios, precio, opiniones) VALUES(%s, %s, %s, %s, %s, %s, %s)', 
                (nombre, marca, tipo_piel, ingredientes_clave, beneficios, precio, opiniones)
            )
            self.connection.commit()
        except:
            print("Error 001 en la función insert_mascarilla")

    def get_one_mascarilla(self, id):
        self.cursor.execute("SELECT * FROM tbmascarillas WHERE id = %s", [id])
        result = self.cursor.fetchall()
        return result
    
    def delete_mascarilla(self, id):
        try:
            self.cursor.execute('DELETE FROM tbmascarillas WHERE id = %s', (id, ))
            self.connection.commit()
        except:
            print("Error 001 en la función delete_mascarilla")

    def update_mascarilla(self, id, nombre, marca, tipo_piel, ingredientes_clave, beneficios, precio, opiniones):
        try:
            self.cursor.execute(
                "UPDATE tbmascarillas SET nombre=%s, marca=%s, tipo_piel=%s, ingredientes_clave=%s, beneficios=%s, precio=%s, opiniones=%s WHERE id = %s", 
                (nombre, marca, tipo_piel, ingredientes_clave, beneficios, precio, opiniones, id)
            )
            self.connection.commit()
        except:
            print("Error 001 en la función update_mascarilla")
    
    def close(self):
        self.cursor.close()
        self.connection.close()
