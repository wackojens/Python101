def getValues(dictt,keys):
    studentValues = []
    for student in dictt:
        studentValues.append([student[key] for key in keys])
    return studentValues
    
students = [
        {'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, 
        {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
        {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, 
        {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, 
        {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}
        ]

print("\nOriginal Dictionary:")
print(students)
print("\nExtract values from the said dictionarie and create a list of lists using those values:")

print("\n",getValues(students,('student_id', 'name', 'class')))
# dit zou het volgende moeten printen: [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]

print("\n",getValues(students,('student_id', 'name')))
# dit zou het volgende moeten printen: [[1, 'Jean Castro'], [2, 'Lula Powell'], [3, 'Brian Howell'], [4, 'Lynne Foster'], [5, 'Zachary Simon']]

print("\n",getValues(students,('name', 'class')))
# dit zou het volgende moeten printen [['Jean Castro', 'V'], ['Lula Powell', 'V'], ['Brian Howell', 'VI'], ['Lynne Foster', 'VI'], ['Zachary Simon', 'VII']]