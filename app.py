from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    """Main careers page with job listings"""
    jobs = [
        {'title': 'Data Analyst', 'location': 'Miami, Florida', 'id': 1},
        {'title': 'Data Scientist', 'location': 'Orlando, Florida', 'id': 2},
        {'title': 'Full Stack Engineer', 'location': 'Gainesville, Florida', 'id': 3}
    ]
    return render_template('index.html', jobs=jobs)

@app.route('/job/<int:job_id>')
def job_details(job_id):
    """Job details page with application form"""
    jobs = {
        1: {'title': 'Data Analyst', 'location': 'Miami, Florida'},
        2: {'title': 'Data Scientist', 'location': 'Orlando, Florida'},
        3: {'title': 'Full Stack Engineer', 'location': 'Gainesville, Florida'}
    }
    job = jobs.get(job_id, jobs[1])
    return render_template('job_details.html', job=job)

@app.route('/apply', methods=['POST'])
def apply():
    """Handle job application submission"""
    name = request.form.get('name')
    email = request.form.get('email')
    linkedin = request.form.get('linkedin')
    education = request.form.get('education')
    experience = request.form.get('experience')

    # Handle file upload
    if 'resume' in request.files:
        resume = request.files['resume']
        if resume.filename:
            filename = f"{name.replace(' ', '_')}_{resume.filename}"
            resume.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    # In a real app, you would save this to a database
    print(f"Application received from {name} ({email})")

    return redirect(url_for('confirmation'))

@app.route('/confirmation')
def confirmation():
    """Application confirmation page"""
    return render_template('confirmation.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)