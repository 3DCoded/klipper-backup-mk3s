import threading

print('Hello before')

t = threading.Thread(target=print, args=('Hello from thread',))
t.run()

print('Hello after')