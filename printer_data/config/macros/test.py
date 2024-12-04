import threading

print('Hello before')

t = threading.Thread(target=gcode, args=('M109 S50',))
t.run()

print('Hello after')