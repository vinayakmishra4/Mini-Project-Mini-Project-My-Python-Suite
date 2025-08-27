"""UnitConvert.py

This module provides functions to convert values between various units of measurement,
including length, area, volume, mass, temperature, speed, pressure, energy, power, and storage.
Each function takes a value, a source unit, and a target unit, and returns the converted value.
"""
def length_convert(value, from_unit, to_unit):
    """Convert length from one unit to another.

    Parameters:
    value (float): The numerical value to convert.
    from_unit (str): The unit of the input value.
    to_unit (str): The unit to convert the value to.

    Returns:
    float: The converted length value.
    """
    factors = {
        "mm": 0.001, "cm": 0.01, "m": 1, "km": 1000,
        "in": 0.0254, "ft": 0.3048, "yd": 0.9144,
        "mi": 1609.344, "nmi": 1852
    }
    return value * factors[from_unit] / factors[to_unit]

def area_convert(value, from_unit, to_unit):
    """Convert area from one unit to another.

    Parameters:
    value (float): The numerical value to convert.
    from_unit (str): The unit of the input value.
    to_unit (str): The unit to convert the value to.

    Returns:
    float: The converted area value.
    """
    factors = {
        "mm2": 1e-6, "cm2": 1e-4, "m2": 1,
        "km2": 1e6, "in2": 0.00064516, "ft2": 0.092903,
        "yd2": 0.836127, "acre": 4046.856, "hectare": 10000
    }
    return value * factors[from_unit] / factors[to_unit]

def volume_convert(value, from_unit, to_unit):
    """Convert volume from one unit to another.

    Parameters:
    value (float): The numerical value to convert.
    from_unit (str): The unit of the input value.
    to_unit (str): The unit to convert the value to.

    Returns:
    float: The converted volume value.
    """
    factors = {
        "ml": 0.001, "l": 1, "m3": 1000,
        "tsp": 0.00492892, "tbsp": 0.0147868,
        "floz_us": 0.0295735, "cup": 0.24,
        "pint_us": 0.473176, "quart_us": 0.946353,
        "gallon_us": 3.78541, "gallon_uk": 4.54609
    }
    return value * factors[from_unit] / factors[to_unit]

def mass_convert(value, from_unit, to_unit):
    """Convert mass from one unit to another.

    Parameters:
    value (float): The numerical value to convert.
    from_unit (str): The unit of the input value.
    to_unit (str): The unit to convert the value to.

    Returns:
    float: The converted mass value.
    """
    factors = {
        "mg": 1e-6, "g": 0.001, "kg": 1, "t": 1000,
        "oz": 0.0283495, "lb": 0.453592,
        "stone": 6.35029, "ton_us": 907.1847, "ton_uk": 1016.0469
    }
    return value * factors[from_unit] / factors[to_unit]

def temp_convert(value, from_unit, to_unit):
    """Convert temperature from one unit to another.

    Parameters:
    value (float): The temperature value to convert.
    from_unit (str): The unit of the input temperature ('C', 'F', or 'K').
    to_unit (str): The unit to convert the temperature to ('C', 'F', or 'K').

    Returns:
    float: The converted temperature value.
    """
    if from_unit == "C":
        if to_unit == "F":
            # Celsius to Fahrenheit: (°C × 9/5) + 32
            return (value * 9/5) + 32
        elif to_unit == "K":
            # Celsius to Kelvin: °C + 273.15
            return value + 273.15
    elif from_unit == "F":
        if to_unit == "C":
            # Fahrenheit to Celsius: (°F - 32) × 5/9
            return (value - 32) * 5/9
        elif to_unit == "K":
            # Fahrenheit to Kelvin: (°F - 32) × 5/9 + 273.15
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "K":
        if to_unit == "C":
            # Kelvin to Celsius: K - 273.15
            return value - 273.15
        elif to_unit == "F":
            # Kelvin to Fahrenheit: (K - 273.15) × 9/5 + 32
            return (value - 273.15) * 9/5 + 32
    return value  # if same unit

def speed_convert(value, from_unit, to_unit):
    """Convert speed from one unit to another.

    Parameters:
    value (float): The numerical value to convert.
    from_unit (str): The unit of the input value.
    to_unit (str): The unit to convert the value to.

    Returns:
    float: The converted speed value.
    """
    factors = {
        "kmh": 0.277778, "ms": 1, "mph": 0.44704, "knot": 0.514444
    }
    return value * factors[from_unit] / factors[to_unit]

def pressure_convert(value, from_unit, to_unit):
    """Convert pressure from one unit to another.

    Parameters:
    value (float): The numerical value to convert.
    from_unit (str): The unit of the input value.
    to_unit (str): The unit to convert the value to.

    Returns:
    float: The converted pressure value.
    """
    factors = {
        "pa": 1, "bar": 100000, "atm": 101325,
        "psi": 6894.76, "torr": 133.322
    }
    return value * factors[from_unit] / factors[to_unit]

def energy_convert(value, from_unit, to_unit):
    """Convert energy from one unit to another.

    Parameters:
    value (float): The numerical value to convert.
    from_unit (str): The unit of the input value.
    to_unit (str): The unit to convert the value to.

    Returns:
    float: The converted energy value.
    """
    factors = {
        "j": 1, "cal": 4.184, "kcal": 4184,
        "wh": 3600, "kwh": 3600000, "btu": 1055.06
    }
    return value * factors[from_unit] / factors[to_unit]

def power_convert(value, from_unit, to_unit):
    """Convert power from one unit to another.

    Parameters:
    value (float): The numerical value to convert.
    from_unit (str): The unit of the input value.
    to_unit (str): The unit to convert the value to.

    Returns:
    float: The converted power value.
    """
    factors = {
        "w": 1, "kw": 1000, "hp_metric": 735.49875, "hp_us": 745.7
    }
    return value * factors[from_unit] / factors[to_unit]

def storage_convert(value, from_unit, to_unit):
    """Convert digital storage from one unit to another.

    Parameters:
    value (float): The numerical value to convert.
    from_unit (str): The unit of the input value.
    to_unit (str): The unit to convert the value to.

    Returns:
    float: The converted storage value.
    """
    factors = {
        "bit": 0.125, "B": 1, "KB": 1024,
        "MB": 1048576, "GB": 1073741824, "TB": 1099511627776
    }
    return value * factors[from_unit] / factors[to_unit]