from flask import Flask, request

# Create a Flask application
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def index():
    return 'Usage: /add?a=<int>&b=<int> to add two integers a and b.'

# Define a route for addition
@app.route('/add')
def add():
    # Get the values of 'a' and 'b' from the query parameters
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    
    # Perform addition
    result = a + b
    
    # Return the result as a string
    return 'The sum of {} and {} is {}.'.format(a, b, result)

# Run the application if this file is executed
if __name__ == '__main__':
    app.run(debug=True)
