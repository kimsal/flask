
from connect import *
from models import *
#POST => add data
#GET => get data from server
#PUT => update data to server
#DELETE => Delete data from server

@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method=="GET":
		return render_template('index.html')
	else:
		myusername = request.form['username']
		myemail = request.form['email']


		print myusername+" : "+ myemail
		obj = Contact(myusername,myemail)
		Contact.add(obj)
		return render_template('index.html',email=myemail,username=myusername)




@app.route('/category/<data>', methods=['POST', 'GET'])
def category(data=''):
	return render_template('html/category.html',data=data)
@app.route('/<data>', methods=['POST', 'GET'])
def single(data=''):
	return render_template('html/single.html',data=data)
@app.route('/page/<data1>', methods=['POST', 'GET'])
def page(data1=''):
	return render_template('html/page.html',data1=data1)
if __name__ == '__main__':
	app.run(debug = True,host='0.0.0.0')