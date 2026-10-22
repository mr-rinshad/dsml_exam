import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()

# Get sepal length
sepal_length = iris.data[:, 0]

# Create histogram
plt.hist(sepal_length, bins=10, edgecolor="black")

# Labels and title
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.title("Histogram of Sepal Length (Iris Dataset)")

# Show plot
plt.show()
