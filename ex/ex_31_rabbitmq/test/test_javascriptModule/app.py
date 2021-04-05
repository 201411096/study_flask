from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def render_samplePage():
    return render_template('/samplePage.html')

if __name__ == '__main__':
    app.run(debug=True)
