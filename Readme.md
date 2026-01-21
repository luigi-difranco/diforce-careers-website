# DiForce Careers Connector - Flask Application

A careers portal built with Flask, Bootstrap, and the "Frozen Mist" color scheme.

## Color Scheme - Frozen Mist
- **Gray Dark (#7C7D75)**: Mountains, borders, text
- **Gray Light (#ADACA7)**: Mountain shadows, placeholder gradients
- **Cream (#FCF8D8)**: Body background
- **Gray Medium (#D9DADF)**: Header background, form borders
- **Cinnamon (#DD700B)**: CTA buttons, palm fronds, accents

## Features
- Responsive design with Bootstrap 5
- Canvas-generated header with hand-drawn mountains and palm tree
- Three-page workflow: Job Listings → Application Form → Confirmation
- File upload for resumes
- Form validation

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask development server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

## File Structure
```
.
├── app.py                      # Flask application
├── requirements.txt            # Python dependencies
├── templates/
│   ├── index.html             # Job listings page
│   ├── job_details.html       # Job details and application form
│   └── confirmation.html      # Success confirmation page
├── static/
│   ├── css/
│   │   └── styles.css         # Frozen Mist themed styles
│   ├── js/
│   │   └── header-canvas.js   # Canvas header generator
│   └── uploads/               # Resume upload directory
└── README.md
```

## Pages

### 1. Home Page (/)
- Displays all job openings
- "About DiForce" section with placeholder content
- Job listings with Apply buttons

### 2. Job Details (/job/<id>)
- Job description with responsibilities and requirements
- Application form with fields for:
  - Name
  - Email
  - LinkedIn
  - Education
  - Work Experience
  - Resume upload

### 3. Confirmation (/confirmation)
- Success message after application submission
- Option to explore other jobs

## Development

The application uses:
- **Flask**: Web framework
- **Bootstrap 5**: Responsive grid and components
- **Canvas API**: Custom header illustrations
- **CSS Variables**: Easy theme customization

## Customization

To modify the color scheme, edit the CSS variables in `static/css/styles.css`:
```css
:root {
    --gray-dark: #7C7D75;
    --gray-light: #ADACA7;
    --cream: #FCF8D8;
    --gray-medium: #D9DADF;
    --cinnamon: #DD700B;
}
```

## Notes

- Uploaded resumes are stored in `static/uploads/`
- In production, implement proper file validation and database storage
- Current setup uses in-memory data; add a database for persistence