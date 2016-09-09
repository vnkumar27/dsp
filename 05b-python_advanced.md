## Advanced Python    

###Regular Expressions, Dictionary, Writing to CSV File  

This question has multiple parts, and will take **20+ hours** to complete, depending on your python proficiency level.  Knowing these skills will be extremely beneficial during the first few weeks of the bootcamp.

For Part 1, use of regular expressions is optional.  Work can be completed using a programming approach of your preference. 

---

The data file represents the [Biostats Faculty List at University of Pennsylvania](http://www.med.upenn.edu/cceb/biostat/faculty.shtml)

This data is available in this file:  [faculty.csv](python/faculty.csv)

--- 

###Part I - Regular Expressions  


####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

import csv

faculty = csv.reader(open('faculty.csv', 'r'))
next(faculty)
faculty = list(faculty)
frequencies = {}
for row in faculty:
    new = row[1].replace(".","")
    new_row = new.split()
    for i in new_row:
        if i in frequencies:
            frequencies[i] +=1
        else:
            frequencies[i] = 1

print frequencies

####Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

import csv

faculty = csv.reader(open('faculty.csv', 'r'))
next(faculty)
faculty = list(faculty)
frequencies = {}
for row in faculty:
    if row[2] in frequencies:
        frequencies[row[2]] +=1
    else:
        frequencies[row[2]] = 1

print frequencies

####Q3. Search for email addresses and put them in a list.  Print the list of email addresses.

import csv

faculty = csv.reader(open('faculty.csv', 'r'))
next(faculty)
faculty = list(faculty)
emails = [row[3] for row in faculty]

print emails

####Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

Code in advanced_python_regex.py

Place your code in this file: [advanced_python_regex.py](python/advanced_python_regex.py)

---

###Part II - Write to CSV File

####Q5.  Write email addresses from Part I to csv file

Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

The emails.csv file you create should be added and committed to your forked repository.

Your file, emails.csv, will look like this:
```
bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
```

---

### Part III - Dictionary

####Q6.  Create a dictionary in the below format:
```
faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
```
Print the first 3 key and value pairs of the dictionary:

{'Putt': [' PhD ScD', 'Professor of Biostatistics', 'mputt@mail.med.upenn.edu'], 'Feng': [' Ph.D', 'Assistant Professor of Biostatistics', 'ruifeng@upenn.edu'], 'Bilker': ['Ph.D.', 'Professor of Biostatistics', 'warren@upenn.edu']}

####Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

```
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }
```

{('Hongzhe', 'Li'): [' Ph.D', 'Professor', 'hongzhe@upenn.edu'], ('Justine', 'Shults'): [' Ph.D.', 'Professor', 'jshults@mail.med.upenn.edu'], ('Yimei', 'Li'): [' Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu']}

####Q8.  It looks like the current dictionary is printing by first name.  Print out the dictionary key value pairs based on alphabetical orders of the last name of the professors

('Scarlett', 'Bellamy'): [' Sc.D.', 'Associate Professor', 'bellamys@mail.med.upenn.edu']
('Warren', 'Bilker'): ['Ph.D.', 'Professor', 'warren@upenn.edu']
('Matthew', 'Bryan'): [' PhD', 'Assistant Professor', 'bryanma@upenn.edu']
('Jinbo', 'Chen'): [' Ph.D.', 'Associate Professor', 'jinboche@upenn.edu']
('Jonas', 'Ellenberg'): [' Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']
('Susan', 'Ellenberg'): [' Ph.D.', 'Professor', 'sellenbe@upenn.edu']
('Rui', 'Feng'): [' Ph.D', 'Assistant Professor', 'ruifeng@upenn.edu']
('Benjamin', 'French'): [' PhD', 'Associate Professor', 'bcfrench@mail.med.upenn.edu']
('Phyllis', 'Gimotty'): [' Ph.D', 'Professor', 'pgimotty@upenn.edu']
('Wensheng', 'Guo'): [' Ph.D', 'Professor', 'wguo@mail.med.upenn.edu']
('Yenchih', 'Hsu'): [' Ph.D.', 'Assistant Professor', 'hsu9@mail.med.upenn.edu']
('Rebecca', 'Hubbard'): [' PhD', 'Associate Professor', 'rhubb@mail.med.upenn.edu']
('Wei-Ting', 'Hwang'): [' Ph.D.', 'Associate Professor', 'whwang@mail.med.upenn.edu']
('Marshall', 'Joffe'): [' MD MPH Ph.D', 'Professor', 'mjoffe@mail.med.upenn.edu']
('J.', 'Landis'): [' B.S.Ed. M.S. Ph.D.', 'Professor', 'jrlandis@mail.med.upenn.edu']
('Yimei', 'Li'): [' Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu']
('Hongzhe', 'Li'): [' Ph.D', 'Professor', 'hongzhe@upenn.edu']
('Mingyao', 'Li'): [' Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu']
('A.', 'Localio'): [' JD MA MPH MS PhD', 'Associate Professor', 'rlocalio@upenn.edu']
('Nandita', 'Mitra'): [' Ph.D.', 'Associate Professor', 'nanditam@mail.med.upenn.edu']
('Knashawn', 'Morales'): [' Sc.D.', 'Associate Professor', 'knashawn@mail.med.upenn.edu']
('Kathleen', 'Propert'): [' Sc.D.', 'Professor', 'propert@mail.med.upenn.edu']
('Mary', 'Putt'): [' PhD ScD', 'Professor', 'mputt@mail.med.upenn.edu']
('Sarah', 'Ratcliffe'): [' Ph.D.', 'Associate Professor', 'sratclif@upenn.edu']
('Michelle', 'Ross'): [' PhD', 'Assistant Professor', 'michross@upenn.edu']
('Jason', 'Roy'): [' Ph.D.', 'Associate Professor', 'jaroy@mail.med.upenn.edu']
('Mary', 'Sammel'): [' Sc.D.', 'Professor', 'msammel@cceb.med.upenn.edu']
('Pamela', 'Shaw'): [' PhD', 'Assistant Professor', 'shawp@upenn.edu']
('Russell', 'Shinohara'): ['0', 'Assistant Professor', 'rshi@mail.med.upenn.edu']
('Haochang', 'Shou'): [' Ph.D.', 'Assistant Professor', 'hshou@mail.med.upenn.edu']
('Justine', 'Shults'): [' Ph.D.', 'Professor', 'jshults@mail.med.upenn.edu']
('Alisa', 'Stephens'): [' Ph.D.', 'Assistant Professor', 'alisaste@mail.med.upenn.edu']
('Andrea', 'Troxel'): [' ScD', 'Professor', 'atroxel@mail.med.upenn.edu']
('Rui', 'Xiao'): [' PhD', 'Assistant Professor', 'rxiao@mail.med.upenn.edu']
('Sharon', 'Xie'): [' Ph.D.', 'Associate Professor', 'sxie@mail.med.upenn.edu']
('Dawei', 'Xie'): [' PhD', 'Assistant Professor', 'dxie@upenn.edu']
('Wei', 'Yang'): [' Ph.D.', 'Assistant Professor', 'weiyang@mail.med.upenn.edu']

Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)

--- 

If you're all done and looking for an extra challenge, then try the below problem:  

### [Markov](python/markov.py) (Optional)

