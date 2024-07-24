ext_temp = printer.lookup_object('extruder').heater.get_temperature()
ext_target = printer.lookup_object('extruder').heater.get_target()

print(f'{ext_temp}ºC/{ext_target}ºC')