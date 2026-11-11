# CampusFlow — Student, Course & Enrollment Manager (Web Version)

A local web application with an **HTML/CSS/JavaScript frontend**, a **Python Flask backend**, and OOP `Student`, `Course`, `Enrollment`, and `EnrollmentSystem` classes.

## Run on Windows

1. Open PowerShell in this `web-version` folder.
2. Install Flask (one time):
   ```powershell
   python -m pip install -r requirements.txt
   ```
3. Start the app:
   ```powershell
   python app.py
   ```
4. Open **http://127.0.0.1:5000** in your browser.
5. Press **Ctrl+C** in PowerShell to stop the server.

## Features

- Interactive dashboard with counts of students, courses, and enrollments
- Create students with ID, full name, email
- Create courses with ID, title, instructor
- Enroll students using student/course dropdowns
- Show All Records page with all students, courses, and student-course relationships
- Search student and course tables
- Delete students, courses, or enrollments (with related enrollments removed automatically)
- Duplicate ID and duplicate enrollment protection, plus required-field checks
- Records automatically saved to a local `data.json` file and loaded on restart

## Files

- `app.py` — Flask server, REST API, and JSON persistence
- `models.py` — Python OOP classes
- `templates/index.html` — HTML front end
- `static/style.css` — styling and responsive layout
- `static/app.js` — browser interaction and API requests
- `test_system.py` — model tests
- `requirements.txt` — Flask dependency

## Test

```powershell
python -m unittest -v
```

## Demo

1. Go to **Students**, create student `101` / `Alex Lee` / `alex@example.com`.
2. Go to **Courses**, create course `201` / `Intro to Python` / `Professor Smith`.
3. Go to **Enrollments**, choose both entries, and click **Create Enrollment**.
4. Open **Show All Records** and confirm all three records appear.
5. Restart the app to confirm persistence.

**Note:** This runs locally on your computer. Do not expose the development server to the public internet. The generated `data.json` is excluded from GitHub to avoid uploading student information.
