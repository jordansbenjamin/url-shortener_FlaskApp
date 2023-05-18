from flask import Flask, render_template, request

app = Flask(__name__)

# Homepage/base url route is generally indicated with a /
@app.route('/')
def home():
    # return 'Hello Flask!'
    # instead of returning the string we can return the home.html file instead
    # Using the render template function which is imported above
    return render_template('home.html')
    # return render_template('home.html', name='Jordan')

# Name of route and function does not need to match
@app.route('/your-url', methods=['GET', 'POST'])
def your_url():
    # return 'This is a url shortener'
    if request.method == 'POST':
        return render_template('your_url.html', code=request.form['code'])
    else:
        return 'This is not valid'

