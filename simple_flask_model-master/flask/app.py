from flask import Flask
from flask import render_template

# app = Flask(__name__, template_folder='templates')
app = Flask(__name__)

@app.route('/')#google decorate in python 


def main():
    #return "<center>Welcome to the Flask World </center>"
    msg1 = "Hello Students"
    my_dict1={'name':'Zoya','Rank':'Last'}
    return render_template('result.html', msg=msg1 , my_dict=my_dict1)

if __name__ == '__main__':
	app.run(debug=True)# tells which line has an error
                       # this line should only be there if the model is in production 
                       # when it goes to development mode. So, type command set FLASK_ENV=development