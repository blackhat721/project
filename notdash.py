import os
from flask import Flask, request, render_template, redirect, session, url_for
import pandas as pd
from werkzeug.utils import secure_filename
from DataProcess import *
# print(os.path.join(os.path.dirname(__file__),"templates"))
app = Flask(__name__)
# file = ""
# file1 = ""
# sheet = ""
# sheet1 = ""
def func():
    # print(file)
    # path  = os.path.join(os.path.dirname(__file__),"templates",file)
    # path1 = os.path.join(os.path.dirname(__file__),"templates",file1)

    df,df1 = loadData(file,file1,sheet,sheet1)
    # print(df.head())


    df  = cleanData(df)
    # print(df.head())

    df1 = cleanData(df1)
    # print(df.head())
    ls = Process(df,df1)
    # print(ls)
    writeOutput(ls,df)





@app.route('/success/<name>')
def success(name):
  # df = pd.read_excel(name,sheet_name="Anex")
  func()
  return 'welcome %s' %name

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        global file  
        global file1 
        global sheet 
        global sheet1 
        f  = request.files['nm']
        f1 = request.files['nm1']
        sh = request.form['sheet']
        sh1 = request.form['sheet1']
        # print(file)
        file = f.filename
        file1 = f1.filename
        sheet = sh
        sheet1 = sh1
        # print(session.get("f"))
        # f.save(f.filename)
        f.save(os.path.join(os.path.dirname(__file__),"templates",secure_filename(f.filename)))
        f1.save(os.path.join(os.path.dirname(__file__),"templates",secure_filename(f1.filename)))
        u = 'file uploaded successfully with {}, {}'.format(sheet,sheet1)
        # u = [f.filename,f1.filename,sheet,sheet1]


        return redirect(url_for('success',name = u))
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug = True)