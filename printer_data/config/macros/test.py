import threading

t = threading.Thread(target=gcode, args=('M109 S200',))
t.run()

print('Printer is heating now...')