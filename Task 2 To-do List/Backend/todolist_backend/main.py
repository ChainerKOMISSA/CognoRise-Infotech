from flask import Flask, render_template
import jsonify
import mysql.connector

app = Flask(__name__)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="todo_list_database",
)

@app.route('/', methods=['GET'])
def getListTasks():
    cursor = db.cursor()
    query = "SELECT t.id, t.title, t.description, t.date_debut, t.date_fin, e.libelle FROM task t JOIN etat e ON e.idetat = t.id WHERE e.idetat = t.id"
    cursor.execute(query)
    tasks = cursor.fetchall()
    cursor.close()

    task_formatted = []
    for task in tasks :
        formatage = {
            'id' : task[0],
            'titre' : task[1],
            'description' : task[2] if task[2] else '',
            'dateDebut': task[3],
            'dateFin': task[4] if task[4] else '',
            'etat': task[5],
        }
        task_formatted.append(formatage)
    return render_template('index.html', tasks = task_formatted)


"""def files(user_id):
    cursor = db.cursor()
    query = "SELECT * FROM File"
    cursor.execute(query)
    files = cursor.fetchall()
    cursor.close()

    files_formatted = []
    for file in files :
        linkfile = file[3]
        nom, extension = os.path.splitext(linkfile)
        color_class = get_color_class(extension[1:])

        format = {
            'id' : file[0],
            'namefile' : file[1],
            'description' : file[2],
            'linkfile': file[3],
            'extension': extension[1:],
            'added': file[4],
            'user_id' : file[5],
            'icon_class': get_icon_class(file[3].split('.')[-1]),
            'color_class' : color_class
        }
        files_formatted.append(format)
    return render_template('files.html', fichiers = files_formatted, user_id = user_id)"""

def get_color_class():
    color_mapping = {
        'forte': '#FF2D00',
        'moyenne': '#2A60F3',
        'faible': '#313132'
    }
    return color_mapping.get('#313132')

@app.route('/create')
def createTask():
    print()

@app.route('/update')
def updateTask():
    print()

@app.route('/delete')
def deleteTask():
    print()

if __name__ == '__main__' :
    app.run(debug=True)