import csv

faculty = csv.reader(open('faculty.csv', 'r'))
next(faculty)
faculty = list(faculty)
faculty_dict = {}
professor_dict = {}
faculty_2 = []

#Replaces current titles with shortened title.
for row in faculty:
    full_title = row[2].split()
    if full_title[0].startswith("A"):
        part_title = " ".join(full_title[:2])
    else:
        part_title = full_title[0]
    row[2] = part_title
    faculty_2.append(row)

#Q6: creates faculty_dict
for row in faculty:
    name = row[0].split()
    last_name = name[-1]
    if last_name in faculty_dict:
        faculty_dict[last_name] += [row[1:]]
    else:
        faculty_dict[last_name] = row[1:]
first_3 = {item: faculty_dict[item] for item in faculty_dict.keys()[:3]}
print first_3

#Q7: creates professor_dict
for row in faculty:
    name = row[0].split()
    first_last = (name[0],name[-1])
    professor_dict[first_last] = row[1:]

first_3 = {item: professor_dict[item] for item in professor_dict.keys()[:3]}
print first_3

#Q8: prints professor_dict by last name, descending
for key in sorted(professor_dict,key = lambda item: item[1]):
    print "%s: %s" % (key, professor_dict[key])
