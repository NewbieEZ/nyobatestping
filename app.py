from flask import Flask, render_template, request

# Create a Flask application
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def index():
    return render_template('index.html')

# Define a route for addition
@app.route('/add', methods=['POST'])
def add():
    # Get the values of 'a' and 'b' from the form
    a = int(request.form['a'])
    b = int(request.form['b'])
    
    # Perform addition
    result = a + b
    
    # Return the result as a string
    return 'The sum of {} and {} is {}.'.format(a, b, result)

# Run the application if this file is executed
if __name__ == '__main__':
    app.run(debug=True)
