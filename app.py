from flask import Flask, render_template, request, redirect, url_for
import json

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
        urls = {}
        urls[request.form['code']] = {'url': request.form['url']}
        with open('urls.json', 'w') as url_file:
            json.dump(urls, url_file)
        return render_template('your_url.html', code=request.form['code'])
    else:
        # return redirect('/') # Redirects to the homepage
        # You can instead do this
        return redirect(url_for('home'))