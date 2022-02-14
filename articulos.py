import sqlite3

class Articulos:

    def abrir(self):
        conexion=sqlite3.connect("admin.db")
        return conexion


    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into articulos(descripcion, precio) values (?,?)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select cedula, Nombre from usuarios where cedula=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()
            
    def recuperar_todos(self):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select cedula, Nombre, Apellido, Cargo, from usuarios"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()