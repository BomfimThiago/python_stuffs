student_grades = {
    'Jack': [85, 90],
    'Jill': [80, 95]
}

# the naive way
def get_grades_naive(name):
    if name in student_grades:
        return student_grades[name]
    return []

# the better way
def get_grades_better(name):
    return student_grades.get(name, [])

# the naive way
def get_grades_with_assignment(name):
    if name not in student_grades:
        student_grades[name] = []
    return student_grades[name]

# the better way
def get_grades_with_assignment_better(name):
    return student_grades.setdefault(name, [])

def set_grade_naive(name, score):
    if name in student_grades:
        grades = student_grades[name]
    else:
        student_grades[name] = []
        grades = student_grades[name]
    grades.append(score)