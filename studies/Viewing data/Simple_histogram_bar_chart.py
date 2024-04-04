from matplotlib import pyplot as plt
from collections import Counter

# Grades
grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
# Group the grades by decile, but put the 100 with the 90
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)

plt.bar([x + 5 for x in histogram.keys()],      # Move the bars to the right by 5 
        histogram.values(),                     # Assign the corret height to each bar
        10,                                     # Assign width 10 to each bar
        edgecolor=(0, 0, 0))                    # Darken the edges if the bars

plt.axis([-5, 105,      # x axis from -5 to 105,
           0, 5])       # y axis from 0 to 5

# x axis labels at 0, 10, ..., 100
plt.xticks([10 * i for i in range(11)])
# add a x label
plt.xlabel("Decile")
# add a y label
plt.ylabel("N° of Students")
# add a title
plt.title("Distribution of Exam 1 Grades")
plt.show()