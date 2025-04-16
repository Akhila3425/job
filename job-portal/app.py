from flask import Flask, render_template 



# Create Flask app
app = Flask(__name__, template_folder='templates')

# Route for homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for login page
@app.route('/login')
def login():
    return render_template('login.html')

# Route for government jobs page
@app.route('/govt_jobs')
def govt_jobs():
    return render_template('govt_jobs.html')

# Route for post job page
@app.route('/post_job')
def post_job():
    return render_template('post_job.html')

# Route for success page (after form submission)
@app.route('/success')
def success():
    return render_template('success.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
