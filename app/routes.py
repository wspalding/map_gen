from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home Page')

















if __name__ == '__main__':
    app.run()
