ext_temp, ext_target = printer.lookup_object('extruder').heater.get_temp(0)
ext_power = printer.lookup_object('extruder').heater.last_pwm_value

print(f'Extruder: {round(ext_temp,2)}ºC/{ext_target}ºC, {round(ext_power*100,1)}%')
gcode('G28')