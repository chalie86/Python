from flask import Flask, render_template,send_file


app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/test/')
def test():
    return render_template('test.html')      

if __name__=="__main__":
    app.run(debug=True)



@app.route('/download/')
def download():
    try:
        #return send_file('C:/PythonProject/flask/mysite/MyApp/download/cv4.doc', attachment_filename='cv4.doc')
         #return send_file(r'C:/PythonProject/flask/mysite/MyApp/download/cv4.doc', attachment_filename='cv4.doc')
         return send_file(r'C:\PythonProject\flask\mysite\MyApp\download\cv4.doc',
                 attachment_filename='/download/cv4.doc')
    except Exception as e:
        return str(e)
