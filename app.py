from flask import Flask,request,render_template

app = Flask(__name__)
@app.route('/square',methods=['GET'])
def squarenumber():
	num = request.args.get('num')
	square = None

	if num and num.strip():
		try:
			square = int(num)**2
		except ValueError:
			return "<h1>Invalid input. Please enter a valid number..</h1>"

	return render_template('sqaurenum.html',num=num,square=square)

if __name__== '__main__':
	app.run(debug=True)

	#value={{num if num else ''}}