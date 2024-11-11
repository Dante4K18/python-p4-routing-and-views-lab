#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:text>')
def print_string(text):
    print(text)  # Prints the string to the console
    return text  # Returns only the text, without HTML tags

@app.route('/count/<int:parameter>')
def count(parameter):
    count_string = "\n".join(str(i) for i in range(parameter)) + "\n"
    return count_string  # Ensure a newline at the end


@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div' and num2 != 0:
        result = num1 / num2  # Use floating-point division
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation or division by zero", 400

    return str(result)  # Return the result as a string

if __name__ == '__main__':
    app.run(debug=True)

