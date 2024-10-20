from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name')
    message = request.args.get('message')
    if request.args.get('name') == None and request.args.get('message') == None:
        return "<h1>Hello</h1>"
    if request.args.get('name') == None:
        return '''<h1>Hello ! {}!</h1>'''.format(message)
    if request.args.get('message') == None:
        return '''<h1>Hello {}!</h1>'''.format(name)
    else:
        return '''<h1>Hello {}! {}!</h1>'''.format(name, message)

if __name__ == "__main__":
    app.run()