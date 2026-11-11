# Student Course Enrollment System

This is my Student, Course, and Enrollment project using Python and object-oriented programming (OOP). It allows users to add students, create courses, enroll students, and view all records.

I made two versions: a desktop application using Python Tkinter and a web application using HTML, CSS, JavaScript, and Flask.

## Features

- Add students with ID, name, and email
- Add courses with ID, title, and instructor
- Enroll students in courses
- View all students, courses, and enrollments
- Remove students, courses, and enrollments
- Prevent duplicate records
- Save data automatically

## Project Structure

```text
student-course-enrollment-system/
├── README.md
├── desktop-version/
│   └── student_course_enrollment/
│       ├── main.py
│       ├── models.py
│       ├── test_system.py
│       └── README.md
└── web-version/
    └── student_enrollment_web/
        ├── app.py
        ├── models.py
        ├── test_system.py
        ├── requirements.txt
        ├── README.md
        ├── templates/
        └── static/
```

## Desktop Version

This version uses Tkinter for the graphical interface. Users can add students, manage courses, enroll students, and view records.

**How to run:**

Open a terminal in the main project folder and enter:

```powershell
cd desktop-version/student_course_enrollment
python main.py
```

## Web Version

This version uses HTML, CSS, and JavaScript for the front end and Python Flask for the backend.

**How to run:**

Open a terminal in the main project folder and enter:

```powershell
cd web-version/student_enrollment_web
python -m pip install -r requirements.txt
python app.py
```

Then open:

http://127.0.0.1:5000

## OOP Classes

- **Student:** Stores student ID, name, and email.
- **Course:** Stores course ID, title, and instructor.
- **Enrollment:** Connects students to courses.
- **EnrollmentSystem:** Manages students, courses, and enrollments.

## Testing

Both versions include a `test_system.py` file.

To run the tests, open a terminal inside either application's folder and enter:

```powershell
python -m unittest -v
```

## Requirements

- Python 3.10 or newer
- Tkinter for the desktop version
- Flask for the web version

Both versions run separately and store their own records.
