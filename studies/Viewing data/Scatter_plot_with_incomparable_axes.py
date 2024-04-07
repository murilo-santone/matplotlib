from matplotlib import pyplot as plt

# Test 1 grades
test_1_grades = [99, 90, 85, 97, 80]
# Test 2 grades
test_2_grades = [100, 85, 60, 90, 70]

plt.scatter(test_1_grades, test_2_grades)
# add title
plt.title("Axes Aren't Comparable")
# add label in x axes
plt.xlabel("test 1 grade")
# add label in y axes
plt.ylabel("test 2 grade")
plt.show()