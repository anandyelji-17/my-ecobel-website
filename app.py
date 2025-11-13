from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hello', methods=['POST'])
def hello():
    name = request.form.get('name', 'Friend')
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    # Bind to 0.0.0.0 so Codespaces can forward the port
    app.run(host='0.0.0.0', port=8080, debug=True)
