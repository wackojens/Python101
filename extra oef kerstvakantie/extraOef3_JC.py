def list_of_dicts(marks):
    result = []
    for i in range(len(marks['Name'])):
        result.append({key : marks[key][i] for key in marks})
    return result

marks = {'Name': ["Jan", "Piet", "Joris", "Corneel"], 'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}

print("Original dictionary of lists:")
print(marks)

# verwachte output: {'Name': ["Jan", "Piet", "Joris", "Corneel"],'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
print("\nSplit said dictionary of lists into list of dictionaries:")
print(list_of_dicts(marks))
# verwachte output: 

[{'Name': 'Jan', 'Science': 88, 'Language': 77}, {'Name': 'Piet', 'Science': 89, 'Language': 78}, {'Name': 'Joris', 'Science': 62, 'Language': 84}, {'Name': 'Corneel', 'Science': 95, 'Language': 80}]