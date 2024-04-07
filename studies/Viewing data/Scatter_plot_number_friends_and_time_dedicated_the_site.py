from matplotlib import pyplot as plt

# Friends
friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
# Minutes
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
# Labels
labels = ['a','b','c','d','e','f','g','h','i']

plt.scatter(friends, minutes)

# Label each point
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
                 xy=(friend_count, minute_count),       # Place the label at the appropriate point
                 xytext=(5, -5),                        # but slightly displaced
                 textcoords='offset points')
    
# add title
plt.title("Daily Minutes vs. Number of Friends")
# add label in x-axes
plt.xlabel("N° of friends")
# add label in y-axes
plt.ylabel("daily minutes spent on the site")
# Here we have a scatter plot between the number of
# friends and the time dedicated to the site
plt.show()