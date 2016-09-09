import csv

faculty = csv.reader(open('faculty.csv', 'r'))
next(faculty)
faculty = list(faculty)
emails = [row[3] for row in faculty]

writer = csv.writer(open("/Users/veenakumar/ds/metis/metisgh/prework/dsp/python/emails.csv", 'w'),delimiter = ',')
for row in emails:
    writer.writerow([row])
