from math import sqrt


def likelihood(dist, data):
    lik = 0.000000

    for i in data:
        lik *= dist[i]

    return lik

data1 = [1, 5, 2, 5, 2, 5, 10, -20]
data3=[13.04, 1.32, 22.65, 17.44, 29.54, 23.22, 17.65, 10.12, 26.73, 16.43]

def mean(data):
    return sum(data)/len(data)

def median(data):
    sorted_data = sorted(data)
    return sorted_data[(len(sorted_data) - 1)/2]

def mode(data):
    best_number = data[0]
    best_count = 1

    for num in data:
        cnt = data.count(num)

        if cnt > best_count:
            best_count = cnt
            best_number = num

    return best_number

def variance(data):
    mu = mean(data)
    data2 = [(i - mu)**2 for i in data]
    return mean(data2)

def stantard_dev(data):
    return sqrt(variance(data))

test = likelihood({'A':0.2,'B':0.2,'C':0.2,'D':0.2,'E':0.2},'ABCEDDECAB')
print test
