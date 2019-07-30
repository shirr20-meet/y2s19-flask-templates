from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html", name= "katerina", food_list= ["strawberry",'chocolate',"spageti"], age=66)

@app.route('/info/<string:info_name>/<int:age>')
def profile(info_name,age):
	return render_template("index.html", name=info_name, food_list=[], age=age)

if __name__ == '__main__':
    app.run(debug = True)
