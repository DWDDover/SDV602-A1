from file_manager import FileManager
import matplotlib.pyplot as plt

class DataVisualiser:
    
    def __init__(self):
        self.fm = FileManager()
        self.data = []
        
    def load_csv(self, file_name):
        data = self.fm.read_csv(file_name)
        
        if not data:
            print(f"No data loaded from file: {file_name}")
            return
        
        self.data = data
        
    def plot_line_chart(self, x_key, y_key, title, series_key=None):
        if not self.data:
            print("No data to plot!")
            return

        series = {}
        for row in self.data:
            series.setdefault(row.get(series_key), []).append(row)

        plt.figure(figsize=(8, 6))

        for name, rows in series.items():
            rows = sorted(rows, key=lambda r: r[x_key])
            x_values = [row[x_key] for row in rows]
            y_values = [float(row[y_key]) for row in rows]
            plt.plot(x_values, y_values, marker='o', label=name)

        if series_key:
            plt.legend()
        plt.xlabel(x_key)
        plt.ylabel(y_key)
        plt.title(title)
        plt.show()
