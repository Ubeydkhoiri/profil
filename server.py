import model # Import the python file containing the ML model
from flask import Flask, request, render_template,jsonify # Import flask libraries

# Initialize the flask class and specify the templates directory
app = Flask(__name__,template_folder="templates")

# Default route set as 'home'
@app.route('/home')
def home():
    return render_template('home.html') # Render home.html

# Route 'classify' accepts GET request
@app.route('/classify',methods=['POST','GET'])
def classify_type():
    try:
        name = request.args.get('name') # Get parameters for name
        sex = request.args.get('sex') # Get parameters for sex
        age = request.args.get('age') # Get parameters for age
        sibs = request.args.get('sibs') # Get parameters for sibs
        parch = request.args.get('parch') # Get parameters for parch
        pclass = request.args.get('pclass') # Get parameters for pclass
        fare = request.args.get('fare') # Get parameters for fare
        # Get the output from the classification model
        survive = model.classify(sex, age, sibs, parch, pclass, fare)

        # Render the output in new HTML page
        return render_template('output.html', survive=survive, name=name)
    except:
        return 'Error'

# Run the Flask server
if(__name__=='__main__'):
    app.run(debug=True)        