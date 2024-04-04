from matplotlib import pyplot as plt

# Mentions
mentions = [500, 505]
# Years
years = [2017, 2018]

# plot bars with x axis years and y axis mentions 
plt.bar(years, mentions, 0.8)
# label the x axis with the years numbers in the centers of the bars 
plt.xticks(years)
# add y axis label
plt.ylabel("N° of times I heard someone say 'data science'")

# if you don't do this, matplotlib will label thw x axis as 0, 1
# and add a +2.013e3 off in the corner
plt.ticklabel_format(useOffset=False)

# the naughty y axis only shows the part above 500
plt.axis([2016.5, 2018.5, 499, 506])
# add title
plt.title("Look at the 'Huge' Increase!")
plt.show()