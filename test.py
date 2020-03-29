from flask import Flask, request
import os

app = Flask(__name__)
flag_file = open("flag.txt", "r")


@app.route('/shell')
def shell():
    os.system("rm -f flag.txt")
    exec_cmd = request.args.get('c')
    os.system(exec_cmd)
    return "1"


@ app.route('/')
def source():
    return open("app.py", "r").read()


if __name__ == "__main__": app.run(host='0.0.0.0')
