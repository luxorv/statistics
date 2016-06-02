# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 

def isLeapYear(year):
    if year%4 != 0:
        return False
    elif year%100 !=0:
        return True
    elif year%400 !=0:
        return False
    else:
        return True

def daysInMonth(month, year):
    daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2 and isLeapYear(year):
        daysOfMonths[month-1] += 1

    return daysOfMonths[month-1]

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < daysInMonth(month, year):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""

    # YOUR CODE HERE!
    days = 0
    second_date = (year2, month2, day2)
    first_date = (year1, month1, day1)

    assert not first_date > second_date

    while first_date < second_date:
        days += 1
        first_date = nextDay(*first_date)

    return days

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

