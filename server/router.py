from flask import Flask
app = Flask(__name__)
from query import db_query

@app.route("/")
def home():
    return category(0)

@app.route("/category/<topic_id>")
def category(topic_id):

    return db_query(int(topic_id))


if __name__ == "__main__":
    app.run()
    
