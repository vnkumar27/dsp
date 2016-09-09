import csv

faculty = csv.reader(open('faculty.csv', 'r'))
next(faculty)
faculty = list(faculty)
emails = [row[3] for row in faculty]
email_domains = {}
for i in emails:
    email_split = i.split("@")
    if email_split[-1] in email_domains:
        email_domains[email_split[-1]] += 1
    else:
        email_domains[email_split[-1]] = 1

print email_domains

