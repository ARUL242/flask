from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<marquee behavior="scroll" direction="left">This text will scroll from right to left.</marquee>'

if __name__ == '__main__':
    app.run(debug=True)