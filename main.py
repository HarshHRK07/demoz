from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    with open('index.html', 'r') as file:
        html_content = file.read()
    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
