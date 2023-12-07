from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

api_key = os.getenv("API_KEY")
db_password = os.getenv("DB_PASSWORD")

def create_user_repository(name, password, email):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=db_password,
    database="atividade_ponderada"
)
    cursor = mydb.cursor()
    sql = "INSERT INTO users (name, password, email) VALUES (%s, %s, %s)"
    val = (name, password, email)
    
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()
    

    return {"message": f"Usuário {name} foi cadastrado(a) com sucesso!"}

def get_users_repository():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = db_password,
        database = "atividade_ponderada"
    )
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users")
    myresult = cursor.fetchall()
    cursor.close()
    return myresult

def update_user_repository(id, usuario):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = db_password,
        database = "atividade_ponderada"
    )
    cursor = mydb.cursor()
    sql = "UPDATE users SET name = %s, password = %s, email = %s WHERE id = %s"
    val = (usuario.name, usuario.password, usuario.email, id)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()
    return {"message": f"Usuário {usuario.name} foi atualizado(a) com sucesso!"}

def delete_user_repository(id):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = db_password,
        database = "atividade_ponderada"
    )

    cursor = mydb.cursor()
    sql = "DELETE FROM users WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()
    return {"message": f"Usuário {id} foi deletado(a) com sucesso!"}

def authenticate_user_repository(username, password):

    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = db_password,
        database = "atividade_ponderada"
    )
    cursor = mydb.cursor()
    query = "SELECT * FROM Users WHERE email = %s"

    with mydb.cursor() as cursor:
        cursor.execute(query, (username,))
        user = cursor.fetchone()

    return  {"access_token": str(user[0]), "token_type": "bearer"}

