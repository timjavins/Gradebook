grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    return grades_sum(grades) / float(len(grades))

def grades_variance(grades):
    variance = float(0)
    for grade in grades:
        variance += (grades_average(grades) - grade) ** 2
    return variance / len(grades)

variance = grades_variance(grades)

def grades_std_deviation(variance):
    return variance ** (0.5)

print "The grades are:"
print_grades(grades)
print ""
print grades_sum(grades)

print "Average:"
print grades_average(grades)
print "Variance:"
print variance
print "Standard Deviation:"
print grades_std_deviation(variance)
