[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

import scipy.stats


mu = 178
sigma = 7.7
heights_norm = scipy.stats.norm(loc=mu, scale=sigma)

lower_cdf = heights_norm.cdf(177.8)
upper_cdf = heights_norm.cdf(185.4)

print upper_cdf - lower_cdf

#0.342094682946 -- 34% of the population of men are between 5'10" and 6'1"
