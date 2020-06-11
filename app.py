import datetime
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    current_time = datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")
    return 'Hello, GDG Hong Kong! The time now is {}'.format(current_time)


if __name__ == "__main__":
    app.run(port=8080, host='0.0.0.0')
