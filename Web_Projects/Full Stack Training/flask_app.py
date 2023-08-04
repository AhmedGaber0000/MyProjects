from flask import *


app = Flask(__name__)

    
    
@app.route('/')
def index():
    return render_template('index.html')




@app.route('/<task>' )
def Task(task):

    return render_template(f"{task}.html")
    


if __name__ == "__main__":
    app.run()