from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return 'Hey there! I\'m alive.'

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_running():
    server = Thread(target=run)
    server.start()
