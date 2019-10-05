from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])    
def checkout():
    print(request.form)
    count = int(request.form['apple']) + int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['blackberry'])
    print('x'*120)
    print(f"Charging {request.form['first_name'] + ' ' + request.form['last_name']} for {count} fruits")
    return render_template("checkout.html",
     numApple = request.form['apple'],
     numStraw = request.form['strawberry'],
     numRasp = request.form['raspberry'],
     numBlack = request.form['blackberry'],
     firstName = request.form['first_name'],
     lastName = request.form['last_name'],
     userId = request.form['student_id']
     )

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    