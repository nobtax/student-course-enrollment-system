"""Local web front end for the Student, Course, Enrollment OOP system."""
from flask import Flask, jsonify, render_template, request
from pathlib import Path
import json
from models import EnrollmentSystem

app = Flask(__name__)
DB = Path(__file__).with_name('data.json')
system = EnrollmentSystem()


def load():
    if not DB.exists():
        return
    data = json.loads(DB.read_text(encoding='utf-8'))
    for s in data.get('students', []):
        system.add_student(s['student_id'], s['name'], s['email'])
    for c in data.get('courses', []):
        system.add_course(c['course_id'], c['title'], c['instructor'])
    for e in data.get('enrollments', []):
        system.enroll(e['student_id'], e['course_id'])


def save():
    data = {
        'students': [vars(s) for s in system.students.values()],
        'courses': [vars(c) for c in system.courses.values()],
        'enrollments': [{'student_id': e.student.student_id, 'course_id': e.course.course_id} for e in system.enrollments]
    }
    tmp = DB.with_suffix('.tmp')
    tmp.write_text(json.dumps(data, indent=2), encoding='utf-8')
    tmp.replace(DB)


def positive_id(value, field):
    try:
        n = int(value)
    except (TypeError, ValueError):
        raise ValueError(f'{field} must be a whole number.')
    if n <= 0:
        raise ValueError(f'{field} must be greater than zero.')
    return n


@app.get('/')
def home():
    return render_template('index.html')


@app.get('/api/records')
def records():
    return jsonify({
        'students': [vars(s) for s in sorted(system.students.values(), key=lambda s: s.student_id)],
        'courses': [vars(c) for c in sorted(system.courses.values(), key=lambda c: c.course_id)],
        'enrollments': [
            {'student_id': e.student.student_id, 'student_name': e.student.name,
             'course_id': e.course.course_id, 'course_title': e.course.title}
            for e in system.enrollments
        ]
    })


@app.post('/api/students')
def add_student():
    try:
        d = request.get_json(force=True)
        student = system.add_student(positive_id(d.get('student_id'), 'Student ID'), str(d.get('name', '')), str(d.get('email', '')))
        save()
        return jsonify(vars(student)), 201
    except (ValueError, TypeError, KeyError) as exc:
        return jsonify(error=str(exc)), 400


@app.post('/api/courses')
def add_course():
    try:
        d = request.get_json(force=True)
        course = system.add_course(positive_id(d.get('course_id'), 'Course ID'), str(d.get('title', '')), str(d.get('instructor', '')))
        save()
        return jsonify(vars(course)), 201
    except (ValueError, TypeError, KeyError) as exc:
        return jsonify(error=str(exc)), 400


@app.post('/api/enrollments')
def add_enrollment():
    try:
        d = request.get_json(force=True)
        e = system.enroll(positive_id(d.get('student_id'), 'Student ID'), positive_id(d.get('course_id'), 'Course ID'))
        save()
        return jsonify(student_id=e.student.student_id, course_id=e.course.course_id), 201
    except (ValueError, TypeError, KeyError) as exc:
        return jsonify(error=str(exc)), 400


@app.delete('/api/students/<int:sid>')
def delete_student(sid):
    if sid not in system.students:
        return jsonify(error='Student not found.'), 404
    system.enrollments = [e for e in system.enrollments if e.student.student_id != sid]
    del system.students[sid]
    save()
    return jsonify(ok=True)


@app.delete('/api/courses/<int:cid>')
def delete_course(cid):
    if cid not in system.courses:
        return jsonify(error='Course not found.'), 404
    system.enrollments = [e for e in system.enrollments if e.course.course_id != cid]
    del system.courses[cid]
    save()
    return jsonify(ok=True)


@app.delete('/api/enrollments/<int:sid>/<int:cid>')
def delete_enrollment(sid, cid):
    old = len(system.enrollments)
    system.enrollments = [e for e in system.enrollments if not (e.student.student_id == sid and e.course.course_id == cid)]
    if len(system.enrollments) == old:
        return jsonify(error='Enrollment not found.'), 404
    save()
    return jsonify(ok=True)


load()
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
