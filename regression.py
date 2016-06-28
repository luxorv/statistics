def correlation_cohefitien(x, y):
    xmu = mean(x)
    ymu = mean(y)

    r = (sum([(i - xmu)*(j-ymu) for i, j in x, y]))
    print(r)
