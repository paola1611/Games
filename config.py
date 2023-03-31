import sqlite3

class usuarios:
    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña
        self.database = sqlite3.connect('db_login.db', check_same_thread=False)
        self.cursor = self.database.cursor()
        
    def Iniciar_sesion(self): 

        self.cursor.execute(f"SELECT contraseña FROM usuario WHERE usuario ='{self.usuario}'")
        result = self.cursor.fetchone()

        validar_datos = False
        
        if result is not None and result[0] == self.contraseña:
            validar_datos = True
        
            return validar_datos
        else:
           return validar_datos 
        
    def registrarse(self, nombre):
        nombre_usuario = nombre
        datos = nombre_usuario, self.usuario, self.contraseña
        
        try:
            self.cursor.execute('INSERT INTO usuario (nombre, usuario, contraseña) VALUES (?, ?, ?)', datos)
            self.database.commit()
            return True
        except:
            return False

            
    def nombre_usuario(self):
        
        self.cursor.execute(f'SELECT nombre FROM usuario WHERE usuario = "{self.usuario}"')
        resultado = self.cursor.fetchone()
        nombre = resultado[0]
        
        return nombre
        