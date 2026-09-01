from data_visualiser import DataVisualiser

if __name__ == "__main__":
    dv = DataVisualiser()
    
    dv.load_csv("data/bd-natural-increase-2010-2014.csv")
    dv.load_csv("data/bd-natural-increase-2015-2019.csv")
    dv.plot_line_chart("Period", "Count", "test", series_key="Births_Deaths_or_Natural_Increase")