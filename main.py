from flask import *
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('fileuploadform.html')
@app.route('/success',methods=['POST'])
def success():
    if request.method=='POST':
        name=request.files['file']
        name.save(name.filename)
        return render_template('success.html',abc='name')
if __name__=='__main__':
    app.run(debug=True)