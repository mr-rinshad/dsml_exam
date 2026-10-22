import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()

# Get sepal length and sepal width
sepal_length = iris.data[:, 0]
sepal_width = iris.data[:, 1]

# Create scatter plot
plt.scatter(sepal_length, sepal_width,
            color="green", marker="o")

# Labels and title
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("Sepal Length vs Sepal Width (Iris Dataset)")

# Show plot
plt.show()
