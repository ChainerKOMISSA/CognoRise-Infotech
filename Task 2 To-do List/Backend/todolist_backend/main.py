from flask import Flask, render_template
import jsonify


app = Flask(__name__)


def getConnection():
    print()

@app.route('/')
def getListTasks():
    return render_template('index.html')


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