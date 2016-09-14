[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

import numpy as np
import first
import nsfg
import thinkstats2
import thinkplot

#Reads in the NSFG data
import chap01soln
resp = chap01soln.ReadFemResp()

#Assigns the variable "pmf" to the Pmf function from thinkstats2 for number of kids in the household.
pmf = thinkstats2.Pmf(resp.numkdhh)

#Uses the thinkplot function to plot pmf as a Pmf graph, with the label "numkdhh"
thinkplot.Pmf(pmf,label ='numkdhh')
#Displays the plot
#thinkplot.Show()

#A function to create the biased pmf
def BiasPmf(pmf, label=''):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)

    new_pmf.Normalize()
    return new_pmf

#Enter data that should be used for the biased pmf
biased = BiasPmf(pmf,label='biased')

#Shows both plots on the same axis
thinkplot.Pmfs([pmf,biased]) #the two plots to be graphed
thinkplot.Show()

#Mean of actual vs biased
mean_actual = pmf.Mean()
mean_biased = biased.Mean()

print mean_actual #1.02420515504

print mean_biased #2.40367910066