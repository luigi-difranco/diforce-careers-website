from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key = os.environ.get('SESSION_SECRET', 'dev-key-placeholder')

# Configuration
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), '../static/uploads')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Allowed file extensions
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}

db = SQLAlchemy(app)

# Database Models
class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    linkedin = db.Column(db.String(200))
    education = db.Column(db.Text, nullable=False)
    experience = db.Column(db.Text, nullable=False)
    resume_path = db.Column(db.String(200))
    job_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
    job = jobs.get(job_id)
    if not job:
        return redirect(url_for('index'))
    job['id'] = job_id
    return render_template('job_details.html', job=job)

@app.route('/apply', methods=['POST'])
def apply():
    """Handle job application submission"""
    job_id = request.form.get('job_id', type=int)
    name = request.form.get('name')
    email = request.form.get('email')
    linkedin = request.form.get('linkedin')
    education = request.form.get('education')
    experience = request.form.get('experience')

    # Basic Validation
    if not name or not email or not education or not experience:
        flash('Please fill in all required fields.')
        return redirect(url_for('job_details', job_id=job_id))

    resume_path = None
    # Handle file upload
    if 'resume' in request.files:
        resume = request.files['resume']
        if resume and allowed_file(resume.filename):
            filename = secure_filename(f"{name.replace(' ', '_')}_{resume.filename}")
            resume_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            resume.save(resume_path)
        else:
            flash('Invalid file type. Only PDF, DOC, and DOCX are allowed.')
            return redirect(url_for('job_details', job_id=job_id))

    # Save to database
    try:
        new_app = Application(
            name=name,
            email=email,
            linkedin=linkedin,
            education=education,
            experience=experience,
            resume_path=resume_path,
            job_id=job_id
        )
        db.session.add(new_app)
        db.session.commit()
        print(f"Application received from {name} ({email}) and saved to database.")
    except Exception as e:
        db.session.rollback()
        print(f"Error saving to database: {e}")
        flash('An error occurred while saving your application.')
        return redirect(url_for('job_details', job_id=job_id))

    return redirect(url_for('confirmation'))

@app.route('/confirmation')
def confirmation():
    """Application confirmation page"""
    return render_template('confirmation.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)