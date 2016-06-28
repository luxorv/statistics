# This is a regression example where we calculate the slope of the correlation
# between the variable x and y

mult = lambda x, y: x * y

x = [70, 57, 63, 70, 53, 75, 58]
y = [1, 1, 1, 1, 2, 2, 1]
s = 0

for i in range(len(x)):
    s += mult(x[i], y[i])

b = (s - (1/7) * 9 * 446)/(28816 - (1/7) * 446**2)

a = (1/7) * sum(y) - b * (1/7) * sum(x)

print(36 * b + a)
