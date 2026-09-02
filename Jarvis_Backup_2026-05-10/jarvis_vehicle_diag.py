def check_engine_status(temp, fuel_pressure, battery_v):
    if temp > 105:
        return "CRITICAL: Engine Overheating! Stop immediately."
    elif fuel_pressure < 30:
        return "WARNING: Low Fuel Pressure. Check Fuel Pump."
    elif battery_v < 11.5:
        return "ALERT: Battery Weak. Do not turn off the engine."
    else:
        return "SYSTEMS NORMAL: All vehicle parameters stable."

# Example for Kia breakdown scenario
print(check_engine_status(115, 40, 12.4))
