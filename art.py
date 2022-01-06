import json

with open('148.json') as jsonfile:
    art = json.load(jsonfile)
    print(art['dimension'])

print()

me = {'first_name': 'Kenneth', 'last_name': 'Love', 'topic': 'Python'}
him = {'first_name': 'Craig', 'last_name': 'Dennis', 'topic': 'Java'}
# print(str(me))
# print(json.dumps(me))

# with open('teachers.json', 'a') as teacher_file:
#     json.dump([me, him], teacher_file)

with open('teachers.json') as teachers_file:
    teachers = json.load(teachers_file)
    print(teachers)
