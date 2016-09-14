[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

import numpy as np
import nsfg
import first
import thinkstats2
import thinkplot
import random

#Generates 1000 random numbers
rand_num = [random.random() for x in range(1000)]

#Create a PMF of the numbers
pmf = thinkstats2.Pmf(rand_num)
thinkplot.Pmf(pmf, linewidth=0.1)
thinkplot.Show()

#Create a CDF of the numbers
cdf = thinkstats2.Cdf(rand_num)
thinkplot.Cdf(cdf)
thinkplot.Show()


#Since the CDF graph appears to be almost a straight line, it appears that the numbers are uniformally distributed.
