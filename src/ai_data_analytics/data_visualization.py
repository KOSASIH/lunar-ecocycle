import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualizer:
    def __init__(self):
        self.data = pd.read_csv("data.csv")  # Load data from CSV file

    def visualize_data(self):
        """
        Visualizes the data using a histogram and a scatter plot.
        """
        plt.figure(figsize=(10, 6))
        sns.histplot(self.data["feature1"], bins=20)
        plt.title("Histogram of Feature 1")
        plt.show()

        plt.figure(figsize=(10, 6))
        sns.scatterplot(x="feature1", y="feature2", data=self.data)
        plt.title("Scatter Plot of Feature 1 vs Feature 2")
        plt.show()
