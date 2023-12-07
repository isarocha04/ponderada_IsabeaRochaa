import mysql.connector
import dotenv
import os

dotenv.load_dotenv()

db_password = os.getenv("DB_PASSWORD")

def save_story_repository(story, response):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=db_password,
    database="atividade_ponderada"
)
    connection = mydb
    cursor = connection.cursor()

    query = "INSERT INTO stories (title, description, gpt_description, category) VALUES (%s, %s, %s, %s)"
    values = (story.title, story.description, response ,story.category)

    with mydb.cursor() as cursor:
        cursor.execute(query, values)
        mydb.commit()

    return {"message": "História registrada com sucesso"}

def get_stories_repository():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=db_password,
    database="atividade_ponderada"
) 
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM stories")
    myresult = cursor.fetchall()
    cursor.close()
    return myresult

def update_story_repository(id, story):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=db_password,
    database="atividade_ponderada"
) 
    cursor = mydb.cursor()
    sql = "UPDATE stories SET title = %s, description = %s, category = %s WHERE id = %s"
    val = (story.title, story.description, story.category, id)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()
    return {"message": f"História {story.title} foi atualizada com sucesso!"}

def delete_story_repository(id):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=db_password,
    database="atividade_ponderada"
) 
     
    cursor = mydb.cursor()
    sql = "DELETE FROM stories WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()
    return {"message": f"História {id} foi deletada com sucesso!"}