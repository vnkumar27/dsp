# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

1. ls : lists the names of files in a directory  
2. cd : change directory  
3. cat : displays the contents of a file  
4. mkdir : make a directory  
5. pwd : displays the name of the current directory  
6. q : quit info  
7. grep : search a file for a specific string or expression  
8. tail : prints last few lines of a file  
9. rm : removes a file  
10. cmp : compare the contents of two files  
11. aprops : locate commands  

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  


ls : lists the contents of a directory  
ls -a : displays all files  
ls -l : displays the long format  
ls -lh : use a long list format and print in a human readable font  
ls -lah : list all entries using a long list format in a human readable font  
ls -t : displays newest files first  
ls -Glp : do not print group names, list in long format, and include "\" to directories  


---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

1. -1 : displays entries on separate lines  
2. -r : displays entries in reverse order  
3. -m : displays entries separated with a comma  
4. -t : displays newest files first  
5. -F : flags file names  

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

xargs executes a series of arguments.   
Example: **xargs -d\n** will return the input split on the "\n" deliminator i.e. every new line.

 

