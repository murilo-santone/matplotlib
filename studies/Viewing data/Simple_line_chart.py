from matplotlib import pyplot as plt

# Years
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
# GDP (Gross Domestic Product)
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# create a line chart, years on the x-axis, gdp on the y-axis
# green color, marker o (dot), solid line style
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

# add a title
plt.title("Nominal GDP")

# add a label to the y axis
plt.ylabel("Billions of $")

plt.show()
