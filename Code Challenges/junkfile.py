from itertools import groupby

persons = [{'name': 'Tim', 'age':25}, {'name': 'Jim', 'age':25},
    {'name': 'Cory', 'age':25}, {'name': 'Lisa', 'age':28},]

group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))