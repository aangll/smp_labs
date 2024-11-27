from DAL.load_data import LoadDataCommand
from BLL.commands import ExtremeValuesCommand, BasicVisualizationCommand, ExtendedVisualizationCommand
from UI.visualization import VisualizationReceiver
from BLL.client import Client

def run_lab():
    # Load data
    load_command = LoadDataCommand("assets/weather.csv")
    data = load_command.execute()

    # Analyze extreme values
    extreme_values_command = ExtremeValuesCommand(data)
    extreme_values = extreme_values_command.execute()
    print("Extreme Values:")
    print(extreme_values)

    # Visualizations
    visualization_receiver = VisualizationReceiver(data)

    basic_visualization_command = BasicVisualizationCommand(visualization_receiver)
    basic_visualization_command.execute()

    extended_visualization_command = ExtendedVisualizationCommand(visualization_receiver)
    extended_visualization_command.execute()

    visualization_receiver.save_basic_visualization_html("assets/basic_visualization.html")
    visualization_receiver.save_extended_visualization_html("assets/extended_visualization.html")

    visualization_receiver.save_basic_visualization_png("assets/basic_visualization.png")
    visualization_receiver.save_extended_visualization_png("assets/extended_visualization.png")

    # Client commands
    client = Client()
    client.run_command(load_command)

if __name__ == "__main__":
    lab8()