from flask import Flask, jsonify, request
import socket

app = Flask(__name__)


@app.route('/')
def get_seed():
    return socket.gethostname()

@app.route('/', methods = ['POST'])
def set_seed():
    subprocess.call(['python', 'stress_cpu.py'])
    return "Success"
