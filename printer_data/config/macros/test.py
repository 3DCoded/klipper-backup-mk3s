ext_temp = printer.lookup_object('extruder').heater.get_temp(0)
#ext_target = printer.lookup_object('extruder').heater.get_target(0)

print(dir(printer.lookup_object('extruder').heater))

print(f'{ext_temp}ºC/{ext_target}ºC')