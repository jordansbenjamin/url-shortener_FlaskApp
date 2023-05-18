from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os.path

app = Flask(__name__)
# Allows us to securely send messages back and forth to the user
# For the time being because we're in development we can provide any string for the key but when in production create a strong randomised key
app.secret_key = 'wqkbhcwklqfbwklebh'

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
        # Prevents users from overriding exisitng data in the JSON file
        # without this code it will only print one data in the JSON file and keeps overriding if new ones are added
        if os.path.exists('urls.json'):
            with open('urls.json') as urls_file:
                urls = json.load(urls_file)
        # This code prevents duplicate data entries and insteads redirects to the homepage
        if request.form['code'] in urls.keys():
            # Displays message to users when a short name has already been taken
            flash('That short name has already been taken. Please select another name.')
            return redirect(url_for('home'))    

        urls[request.form['code']] = {'url': request.form['url']}
        with open('urls.json', 'w') as url_file:
            json.dump(urls, url_file)
        return render_template('your_url.html', code=request.form['code'])
    else:
        # return redirect('/') # Redirects to the homepage
        # You can instead do this
        return redirect(url_for('home'))