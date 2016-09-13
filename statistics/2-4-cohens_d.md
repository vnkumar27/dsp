[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

import math
import numpy as np
import thinkstats2
import nsfg

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

live_mean = np.mean(live.totalwgt_lb)
firsts_mean = np.mean(firsts.totalwgt_lb)
others_mean = np.mean(others.totalwgt_lb)

firsts_var = np.var(firsts.totalwgt_lb)
others_var = np.var(others.totalwgt_lb)

n1 = len(firsts)
n2 = len(others)

mean_diff = firsts_mean - others_mean
pooled_var = (n1 * firsts_var + n2 * others_var)/ (n1 + n2)
cohensd = mean_diff/math.sqrt(pooled_var)

print cohensd
#-0.088672927072602

#Since the value of Cohen's d is small, it can be deduced that there is very little difference in the means and thus the effect is very minimal.