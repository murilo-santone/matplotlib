from matplotlib import pyplot as plt

# Movies
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
# Oscar number
num_oscars = [5, 11, 3, 8, 10]

# Plot bars with left x coordinates [0, 1, 2, 3, 4], heights [num_oscars]
plt.bar(range(len(movies)), num_oscars)

# add a title
plt.title("My Favotite Movies")
# add label to the y axis
plt.ylabel("N° of Academy Awards")

# label the x-axis with the movie names in the centers of the bars
plt.xticks(range(len(movies)), movies)

plt.show()