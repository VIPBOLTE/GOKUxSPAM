from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def start():
    return "HellBot Started Successfully"

os.system("python3 -m GOKUxSPAM")
app.run(port=5000)
