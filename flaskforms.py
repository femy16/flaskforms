from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=["GET", "POST"])
def show_hi():
    if request.method=="GET":
        return render_template("index.html")
    else:
        # print(request.form['option'])
        # return str("option" in request.form)
        check = request.form.get('option')
        if check:
            is_checked=True
            return str(is_checked)
        else:
            is_checked=False
            return str(is_checked)
        


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)