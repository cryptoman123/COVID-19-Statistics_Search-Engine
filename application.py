from flask import Flask
from flask import render_template
from flask import request
from coronavirus_monitor import Monitor

server = Flask(__name__)


@server.route("/")
def home():
    return render_template('home.html')


@server.route("/search", methods=["POST", "GET"])
def get_country():
    if request.method == 'POST':
        country = request.form.get('textBoxData')
        M = Monitor()
        M.get_update_by_country(country)
        return render_template("result.html", result=M.return_data_as_list())
    return f'''
        FAILED TO LOAD DATA
    '''


if __name__ == '__main__':
    server.run(debug=False)
