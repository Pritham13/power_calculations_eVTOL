import math

def calculate_battery_power(mtow, l_d_max, eta_total, v_inf):
    """
    Calculate the power absorbed from the battery.

    Args:
        mtow (float): Maximum Take-Off Weight (MTOW) in N
        l_d_max (float): Maximum lift-to-drag ratio
        eta_total (float): Total system efficiency
        v_inf (float): Free-stream velocity in m/s

    Returns:
        float: Power absorbed from the battery in watts
    """
    g = 9.81  # Acceleration due to gravity (m/s^2)
    return (mtow * g* v_inf)  / (eta_total * l_d_max )

def calculate_vertical_flight_power(aircraft_weight, disk_area, air_density, climb_rate, fom, eta_vertical, is_ducted, fuselage_correction_factor):
    """
    Calculate the power required for vertical flight.

    Args:
        aircraft_weight (float): Aircraft weight in N
        disk_area (float): Rotor disk area in m^2
        air_density (float): Air density at flight altitude in kg/m^3
        climb_rate (float): Climb rate in m/s
        fom (float): Figure of Merit
        eta_vertical (float): Combined efficiency of motors and electric powertrain during vertical flight
        is_ducted (bool): True if the aircraft has ducted fans, False for open rotors
        fuselage_correction_factor (float): Correction factor for interference from the fuselage

    Returns:
        float: Power required for vertical flight in watts
    """
    disk_loading = aircraft_weight / disk_area
    if is_ducted:
        power = (aircraft_weight * fuselage_correction_factor * math.sqrt(disk_loading / (2 * air_density * fom**2)) + (climb_rate*aircraft_weight*0.5 )) / eta_vertical
    else:
        power = (aircraft_weight* 0.5 * fuselage_correction_factor * math.sqrt(disk_loading / (2 * air_density * fom**2)) + (climb_rate*aircraft_weight*0.5 )) / eta_vertical
    return power


# Example usage
mtow = 14770.24  # Maximum Take-Off Weight in N (from Table 2.2)
l_d_max = 15.0  # Maximum lift-to-drag ratio (from Table 2.3)
eta_total = 0.75  # Total system efficiency (from Table 2.2)
v_inf = 51.44  # Free-stream velocity in m/s (180 km/h, from Table 2.3)

battery_power_cruise = calculate_battery_power(mtow, l_d_max, eta_total, v_inf)
print(f"Power absorbed from the battery during cruise: {battery_power_cruise*0.001:.2f} kW")

# Vertical flight power calculations
aircraft_weight = mtow  # Aircraft weight in N
disk_area = 19.189  # Rotor disk area in m^2 (from Table 2.4)
air_density = 1.225  # Air density at sea level in kg/m^3
climb_rate = 23.33  # Vertical climb rate in m/s (from report)
fom = 0.8  # Typical Figure of Merit for eVTOLs
eta_vertical = 0.9  # Combined efficiency of motors and electric powertrain during vertical flight
is_ducted = True  # Assuming open rotors
fuselage_correction_factor = 1.03  # Correction factor for interference from the fuselage (from report)

battery_power_vertical_takeoff = calculate_vertical_flight_power(aircraft_weight, disk_area, air_density, climb_rate, fom, eta_vertical, is_ducted, fuselage_correction_factor)
print(f"Power absorbed from the battery during vertical takeoff: {battery_power_vertical_takeoff*0.001:.2f} kW")

total_power = battery_power_cruise*0.001 + (battery_power_vertical_takeoff*0.001)
print(f"Total power absorbed from the battery: {total_power:.2f} kW")
