from collections import defaultdict

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

# the naive way
def set_grade_naive(name, score):
    if name in student_grades:
        grades = student_grades[name]
    else:
        student_grades[name] = []
        grades = student_grades[name]
    grades.append(score)

# the better way
def set_grade_better(name, score):
    grades = get_grades_with_assignment_better(name)
    grades.append(score)

# defaultdict is a dictionary with a default value
# everytime we try to acess a key that doesn't exist
# it will bind the default value to that key
# student_grades = defaultdict(list)

# we can use define the default value like this
# student_grades = defaultdict(lambda:'default value')

# even better way
def set_grade_best(name, score):
    #Here we add a score to the key called name
    #if that key doesn't exist then the defaultdict
    #applies the an empty list to the key
    
    
# The second argument of defaultdict is the initial dict
# which means that it is the dict from where you want to create
# the default dict
student_grades = defaultdict(list, {
    'Jack': [85, 90],
    'Jill': [80, 95]
})
