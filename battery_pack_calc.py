def calculate_battery_pack_config(cell_nominal_voltage,cell_capacity, required_voltage, required_capacity):
    """
    Calculate the parallel and series configuration of the battery pack.

    Args:
        cell_capacity (float): Capacity of a single cell in Ah
        required_voltage (float): Required voltage of the battery pack in V
        required_capacity (float): Required capacity of the battery pack in Ah

    Returns:
        tuple: (num_cells_parallel, num_cells_series)
    """
    # Nominal voltage of a single cell (Li-ion)
    
    required_capacity = (required_capacity/cell_nominal_voltage )* 1000

    # Calculate the number of cells in series
    num_cells_series = int(required_voltage / cell_nominal_voltage)

    # Calculate the number of cells in parallel
    num_cells_parallel = int(required_capacity / (num_cells_series * cell_capacity))

    return num_cells_parallel, num_cells_series
def calculate_battery_pack_weight(cell_weight,cooling_system_weight):
    """
    Calculate the parallel and series configuration of the battery pack.

    Args:
        cell_weight (float): Weight of a single cell in Ah
        cooling_system_weight (float): Percentage of the weight of the cooling system with respect to the battery weight
        

    Returns:
        tuple: (num_cells_parallel, num_cells_series)
    """
    total_cell_weight = (num_cells_parallel + num_cells_series) * cell_weight
    total_weight = (total_cell_weight*0.4)+total_cell_weight
    return total_weight
# Example usage
cell_nominal_voltage = 3.7
cell_capacity = 3.0  # Ah 
required_voltage = 800  # V 
required_capacity = 441.0494  #kWh
cell_weight = 121 #g
cooling_system_weight = 40 #percentage

num_cells_parallel, num_cells_series = calculate_battery_pack_config(cell_nominal_voltage,cell_capacity, required_voltage, required_capacity)
weight =calculate_battery_pack_weight(cell_weight,cooling_system_weight)
print(f"Number of cells in parallel: {num_cells_parallel}")
print(f"Number of cells in series: {num_cells_series}")
print(f"total_weight {weight/1000} Kg")





