ext_temp, ext_target = printer.lookup_object('extruder').heater.get_temp(0)

print(f'{ext_temp}ºC/{ext_target}ºC')