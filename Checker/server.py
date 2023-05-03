from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', color1="black", color2="red",num_row=8,num_col=8)

app.route('/<int:x>')
def row(x):
    return render_template('index.html', color1="black", color2="red",num_row=x,num_col=8)

app.route('/<int:x>/<int:y>')
def row_col(x, y):
    return render_template('index.html', color1="black", color2="red",num_row=x,num_col=y)


if __name__=="__main__":
    app.run(debug=True)
