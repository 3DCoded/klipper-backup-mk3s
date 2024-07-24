ext_temp, ext_target = printer.lookup_object('extruder').heater.get_temp(0)

print(f'{round(ext_temp,2)}ºC/{ext_target}ºC')