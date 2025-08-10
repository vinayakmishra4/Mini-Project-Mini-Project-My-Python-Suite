# unit_converter.py

def length_convert(value, from_unit, to_unit):
    factors = {
        "mm": 0.001, "cm": 0.01, "m": 1, "km": 1000,
        "in": 0.0254, "ft": 0.3048, "yd": 0.9144,
        "mi": 1609.344, "nmi": 1852
    }
    return value * factors[from_unit] / factors[to_unit]

def area_convert(value, from_unit, to_unit):
    factors = {
        "mm2": 1e-6, "cm2": 1e-4, "m2": 1,
        "km2": 1e6, "in2": 0.00064516, "ft2": 0.092903,
        "yd2": 0.836127, "acre": 4046.856, "hectare": 10000
    }
    return value * factors[from_unit] / factors[to_unit]

def volume_convert(value, from_unit, to_unit):
    factors = {
        "ml": 0.001, "l": 1, "m3": 1000,
        "tsp": 0.00492892, "tbsp": 0.0147868,
        "floz_us": 0.0295735, "cup": 0.24,
        "pint_us": 0.473176, "quart_us": 0.946353,
        "gallon_us": 3.78541, "gallon_uk": 4.54609
    }
    return value * factors[from_unit] / factors[to_unit]

def mass_convert(value, from_unit, to_unit):
    factors = {
        "mg": 1e-6, "g": 0.001, "kg": 1, "t": 1000,
        "oz": 0.0283495, "lb": 0.453592,
        "stone": 6.35029, "ton_us": 907.1847, "ton_uk": 1016.0469
    }
    return value * factors[from_unit] / factors[to_unit]

def temp_convert(value, from_unit, to_unit):
    if from_unit == "C":
        if to_unit == "F":
            return (value * 9/5) + 32
        elif to_unit == "K":
            return value + 273.15
    elif from_unit == "F":
        if to_unit == "C":
            return (value - 32) * 5/9
        elif to_unit == "K":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "K":
        if to_unit == "C":
            return value - 273.15
        elif to_unit == "F":
            return (value - 273.15) * 9/5 + 32
    return value  # if same unit

def speed_convert(value, from_unit, to_unit):
    factors = {
        "kmh": 0.277778, "ms": 1, "mph": 0.44704, "knot": 0.514444
    }
    return value * factors[from_unit] / factors[to_unit]

def pressure_convert(value, from_unit, to_unit):
    factors = {
        "pa": 1, "bar": 100000, "atm": 101325,
        "psi": 6894.76, "torr": 133.322
    }
    return value * factors[from_unit] / factors[to_unit]

def energy_convert(value, from_unit, to_unit):
    factors = {
        "j": 1, "cal": 4.184, "kcal": 4184,
        "wh": 3600, "kwh": 3600000, "btu": 1055.06
    }
    return value * factors[from_unit] / factors[to_unit]

def power_convert(value, from_unit, to_unit):
    factors = {
        "w": 1, "kw": 1000, "hp_metric": 735.49875, "hp_us": 745.7
    }
    return value * factors[from_unit] / factors[to_unit]

def storage_convert(value, from_unit, to_unit):
    factors = {
        "bit": 0.125, "B": 1, "KB": 1024,
        "MB": 1048576, "GB": 1073741824, "TB": 1099511627776
    }
    return value * factors[from_unit] / factors[to_unit]