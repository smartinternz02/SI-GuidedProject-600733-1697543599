from flask import Flask,render_template,request
app = Flask(__name__)
import pickle
import numpy as np

model = pickle.load(open('startup.pkl','rb'))

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/login',methods =['POST'])

def login():
   
   a = request.form["bmi"]
   b = request.form["GenHlth"]
   c = request.form["MentHlth"]
   d = request.form["PhysHlth"]
   e = request.form["Age"]
   f = request.form["Education"]
   g = request.form["Income"]

   h = request.form["cc"]
   if (h=="y"):
       h=1
   elif(h=="n"):
       h=0
   i = request.form["hc"]
   if (i=="y"):
       i=1
   elif(i=="n"):
       i=0

   j = request.form["hbp"]
   if (j=="y"):
       j=1
   elif(j=="n"):
       j=0
    
   k = request.form["s"]
   if (k=="y"):
       k=1
   elif(k=="n"):
       k=0


   l = request.form["st"]
   if (l=="y"):
       l=1
   elif(l=="n"):
       l=0

   m = request.form["hda"]
   if (m=="y"):
       m=1
   elif(m=="n"):
       m=0

   n = request.form["pa"]
   if (n=="y"):
       n=1
   elif(n=="n"):
       n=0

   o = request.form["f"]
   if (o=="y"):
       o=1
   elif(o=="n"):
       o=0

   p = request.form["v"]
   if (p=="y"):
       p=1
   elif(p=="n"):
       p=0


   q = request.form["hac"]
   if (q=="y"):
       q=1
   elif(q=="n"):
       q=0


   r = request.form["ahc"]
   if (r=="y"):
       r=1
   elif(r=="n"):
       r=0
    
   s = request.form["ndc"]
   if (s=="y"):
       s=1
   elif(s=="n"):
       s=0
    
   u = request.form["dw"]
   if (u=="y"):
       u=1
   elif(u=="n"):
       u=0

   v = request.form["sex"]
   if (v=="y"):
       v=1
   elif(v=="n"):
       v=0

   t =  [[float(a),float(b),float(c),float(d),float(e),float(f),float(g),float(h),float(i),float(j),float(k),float(l),float(m),float(n),float(o),float(p),float(q),float(r),float(s),float(u),float(v)]]
   output =model.predict(t)
   
   if(output==1.0):
       output="Oops!!You Have Diabates"
   elif(output==0.0):
       output="Great!!You Dont Have Diabetes"

   return render_template("index.html", y = str((output)))
#    return render_template("front.html")

if __name__ == '__main__' :
    app.run(debug=True)
          





