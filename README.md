# Power Calculation for eVTOL Aircraft

This project contains two Python scripts that calculate different aspects of the power requirements and configurations for an electric vertical take-off and landing (eVTOL) aircraft.

## Files

### `power_calc.py`

#### Functions

1. **`calculate_battery_power(mtow, l_d_max, eta_total, v_inf)`**
    - **Description:** Calculates the power absorbed by the battery during cruise flight.
    - **Arguments:**
        - `mtow` (float): Maximum Take-Off Weight (MTOW) in Newtons.
        - `l_d_max` (float): Maximum lift-to-drag ratio.
        - `eta_total` (float): Total system efficiency.
        - `v_inf` (float): Free-stream velocity in meters per second.
    - **Returns:** Power absorbed by the battery in watts.

2. **`calculate_vertical_flight_power(aircraft_weight, disk_area, air_density, climb_rate, fom, eta_vertical, is_ducted, fuselage_correction_factor)`**
    - **Description:** Calculates the power required for vertical flight.
    - **Arguments:**
        - `aircraft_weight` (float): Aircraft weight in Newtons.
        - `disk_area` (float): Rotor disk area in square meters.
        - `air_density` (float): Air density at flight altitude in kg/m³.
        - `climb_rate` (float): Climb rate in meters per second.
        - `fom` (float): Figure of Merit.
        - `eta_vertical` (float): Combined efficiency of motors and electric powertrain during vertical flight.
        - `is_ducted` (bool): True if the aircraft has ducted fans, False for open rotors.
        - `fuselage_correction_factor` (float): Correction factor for interference from the fuselage.
    - **Returns:** Power required for vertical flight in watts.

#### Outputs

The script calculates and prints:
- Power absorbed from the battery during cruise (in kilowatts).
- Power absorbed from the battery during vertical takeoff (in kilowatts).
- Total power absorbed from the battery (in kilowatts).

### `battery_pack_calc.py`

#### Functions

1. **`calculate_battery_pack_config(cell_nominal_voltage, cell_capacity, required_voltage, required_capacity)`**
    - **Description:** Calculates the parallel and series configuration of the battery pack.
    - **Arguments:**
        - `cell_nominal_voltage` (float): Nominal voltage of a single cell.
        - `cell_capacity` (float): Capacity of a single cell in Ah.
        - `required_voltage` (float): Required voltage of the battery pack in V.
        - `required_capacity` (float): Required capacity of the battery pack in Ah.
    - **Returns:** Tuple containing the number of cells in parallel and in series.

2. **`calculate_battery_pack_weight(cell_weight, cooling_system_weight)`**
    - **Description:** Calculates the total weight of the battery pack including the cooling system.
    - **Arguments:**
        - `cell_weight` (float): Weight of a single cell in grams.
        - `cooling_system_weight` (float): Percentage of the weight of the cooling system with respect to the battery weight.
    - **Returns:** Total weight of the battery pack in grams.



#### Outputs

The script calculates and prints:
- Number of cells in parallel.
- Number of cells in series.
- Total weight of the battery pack in kilograms.


