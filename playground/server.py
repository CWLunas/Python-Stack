from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def main():
    return render_template("index.html", row=8, col=8, color_one='black', color_two='red') 

@app.route('/<int:x>')
def row(x):
    return render_template("index.html", row=x, col=8, color_one='black', color_two='red')

@app.route('/<int:x>/<int:y>')
def row_col(x,y):
    return render_template("index.html", row=x, col=y, color_one='black', color_two='red')

@app.route('/<int:x>/<int:y>/<string:one>')
def row_col_one(x,y,one):
    return render_template("index.html", row=x, col=y, color_one=one, color_two='red')

@app.route('/<int:x>/<int:y>/<string:one>/<string:two>')
def row_col_one_two(x,y,one,two):
    return render_template("index.html", row=x, col=y, color_one=one, color_two=two)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)
