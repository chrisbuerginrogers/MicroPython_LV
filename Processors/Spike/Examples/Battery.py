'''
The Hub battery is chargable and readout of various values related to the battery is provided.
'''

from hub import battery

# get all info - returns error state, charger state, voltage, filtered voltage, temperature, current and capacity left

battery.info()


'''
error_state - 
     battery.BATTERY_NO_ERROR = 0
     battery.BATTERY_HUB_TEMPERATURE_CRITICAL_OUT_OF_RANGE = -1
     battery.BATTERY_TEMPERATURE_OUT_OF_RANGE = -2
     battery.BATTERY_TEMPERATURE_SENSOR_FAIL = -3
     battery.BATTERY_BAD_BATTERY = -4
     battery.BATTERY_VOLTAGE_TOO_LOW = -5

charger_state - The state of the charter circuit:
     battery.DISCHARGING = 0
     battery.CHARGING_ONGOING = 1
     battery.CHARGING_COMPLETED = 2
     battery.FAIL = -1

charge_voltage - The battery volgate in mV

charge_voltage_filtered - The battery volgate (filtered) in mV

temperature - The battery temperature in degree Celcius.

charge_current - The battery charging current in mA (the current flowing into the battery)

battery_capacity_left - The battery capacity left in percent of full capacity

'''


