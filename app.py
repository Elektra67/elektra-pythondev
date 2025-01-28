from flask import Flask #importing the class Flask
app = Flask(__name__) #creating an instance of the class Flask
app.route('/')

def hello():
  print("hi Elektra")

print(__name__)
if __name__ == '__main__':
  #print("inside main")
  #this is start the website using app.py inside of Flask run
  app.run(host ='0.0.0.0', debug = True)
  