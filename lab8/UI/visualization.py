import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

class VisualizationReceiver:
    def __init__(self, data):
        self.data = data

    def basic_visualization(self):
        self.data.plot(kind='bar')
        plt.show()

    def extended_visualization(self):
        if len(self.data.columns) >= 2:
            col1 = self.data.columns[0]
            col2 = self.data.columns[1]
            plt.scatter(self.data[col1], self.data[col2])
            plt.xlabel(col1)
            plt.ylabel(col2)
            plt.title('Extended Visualization: Scatter Plot')
            plt.show()
        else:
            print("Not enough columns for extended visualization.")

    def save_extended_visualization_html(self, filename):
        if len(self.data.columns) >= 2:
            fig = px.scatter(self.data, x=self.data.columns[0], y=self.data.columns[1],
                             title='Extended Visualization: Scatter Plot')
            fig.write_html(filename)
            print(f"Extended visualization saved as HTML: {filename}")
        else:
            print("Not enough columns for extended visualization.")

    def save_basic_visualization_html(self, filename):
        long_form_data = pd.melt(self.data, id_vars=self.data.columns[0], value_vars=self.data.columns[1:])
        fig = px.bar(long_form_data, x='variable', y='value', title='Basic Visualization: Bar Plot')
        fig.write_html(filename)
        print(f"Basic visualization saved as HTML: {filename}")

    def save_extended_visualization_png(self, filename):
        if len(self.data.columns) >= 2:
            col1 = self.data.columns[0]
            col2 = self.data.columns[1]
            plt.scatter(self.data[col1], self.data[col2])
            plt.xlabel(col1)
            plt.ylabel(col2)
            plt.title('Extended Visualization: Scatter Plot')
            plt.savefig(filename)
            plt.show()
            print(f"Extended visualization saved as PNG: {filename}")
        else:
            print("Not enough columns for extended visualization.")

    def save_basic_visualization_png(self, filename):
        long_form_data = pd.melt(self.data, id_vars=self.data.columns[0], value_vars=self.data.columns[1:])
        plt.bar(long_form_data['variable'], long_form_data['value'])
        plt.title('Basic Visualization: Bar Plot')
        plt.savefig(filename)
        plt.show()
        print(f"Basic visualization saved as PNG: {filename}")
