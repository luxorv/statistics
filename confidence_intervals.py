# Complete the test function to perform a hypothesis test
# on list l under the null that the mean is h

from math import sqrt


def mean(l):
    return float(sum(l))/len(l)


def var(l):
    m = mean(l)
    return sum([(x-m)**2 for x in l])/len(l)


def factor(l):
    return 1.96


def conf(l):
    return factor(l) * sqrt(var(l) / len(l))


def test(h, mu, ci):
    return abs(h-mu) <= ci

l = [0.79, 0.70, 0.73, 0.66, 0.65, 0.70, 0.74, 0.81, 0.71, 0.70]

mu = mean(l)
ci = conf(l)

print("{} - {}".format(mu - ci, mu + ci))
