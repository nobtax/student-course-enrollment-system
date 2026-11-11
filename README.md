# Student Course Enrollment Management System

An object-oriented Student, Course, and Enrollment Management System with two interactive user interfaces.

## Project Versions

### 1. Desktop Application — Python Tkinter
Located in `desktop-version/`.

A graphical desktop application for creating students, managing courses, enrolling students, and viewing all records.

**Run:**
```bash
cd desktop-version
python main.py
```

### 2. Web Application — HTML, CSS, JavaScript, and Python Flask
Located in `web-version/`.

A browser-based application with a dashboard, interactive forms, searchable records, and enrollment management.

**Run:**
```bash
cd web-version
python -m pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000` in a browser.

## Features

- Create and view student records
- Create and view course records
- Enroll students in courses
- Display all students, courses, and enrollments
- Object-oriented Student, Course, and Enrollment classes
- Input validation and duplicate prevention
- Persistent data storage

## Testing

Each version includes `test_system.py`.

Run the tests from the corresponding version's folder:

```bash
python -m unittest -v
```

## Technologies

- Python
- Object-Oriented Programming
- Tkinter
- HTML, CSS, JavaScript
- Flask

## Notes

Both applications are independent implementations of the same enrollment system. Each can be run separately, and their saved data is not shared.