from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

# client = MongoClient('localhost', 27017)
# db = client.flaskdb
# collec = db.mycollection

app.config['MONGO_URI'] = "mongodb://localhost:27017/flaskdb"
mongo = PyMongo(app)
collection = mongo.db.collection

cursor = list(collection.find({}, {"_id":0}))

# docs = {}
# for a in cursor:  
#     docs.append(a)

# j2h = json2html.convert(json = docs)
# print(j2h)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create')
def create_user():
    return render_template('create.html')
    # if request.method == "POST":
    #     todo_title = request.form['todo_title']
    #     todo_desc = request.form['todo_desc']
    #     collection.insert_one({'Title': todo_title, 'Description': todo_desc})
    # all_todos = collection.find({}, {"_id": 0})
    # return redirect(url_for('save_table', todos = all_todos))
    
@app.route('/post', methods=['GET', 'POST'])
def save_form():
    if request.method == "POST":
        todo_title = (request.form['todo_title'])
        todo_desc = (request.form['todo_desc'])
        collection.insert_one({'Title': todo_title, 'Description': todo_desc})
    elif request.method == "GET":
        print("Bro, don't use hard encoding in the link use the form provided")
    else:
        print("error")
    
    return redirect(url_for('show_table'))


@app.route('/show')
def show_table():
    all_todos = list(collection.find({}, {"_id": 0}))
    return render_template("show.html", todos = all_todos)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)


# What's left to edit :
#? adding data and time on which form is submitted using datatime module...
#? And also pls use try...except for exception handling (especially for connecting to mongoDB)
