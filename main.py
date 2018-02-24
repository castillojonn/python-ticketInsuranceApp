from flask import Flask, render_template, request, json
app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
	return render_template('signup.html')

@app.route('/showSignIn')
def showSignIn():
	return render_template('signin.html')

@app.route('/signup', methods=['POST'])
def signUp():
	# read the posted values from the UI
	_name = request.form['inputName']
	_email = request.form['inputEmail']
	_password = request.form['inputPassword']

	# validate the received values
	if _name and _email and _password:
		return json.dumps({'html':'<span>Success</span>'})
	else:
		return json.dumps({'html':'<span>Enter the required fields</span>'})

@app.route('/showPlans')
def showPlans():
	return render_template('pickplans.html')

@app.route('/showUserInfo')
def showUserInfo():
	return render_template('dash.html')

@app.route('/submitClaim')
def submitClaim():
	return render_template('claimsubmit.html')

@app.route('/showBilling')
def showBilling():
	return render_template('billingInfo.html')

@app.route('/processPayment')
def processPayment():
	return render_template('payment.html')

@app.route('/showAccountInfo')
def showAccountInfo():
	return render_template('account.html')

if __name__ == "__main__":
	app.run()