import threading

t = threading.Thread(target=print, args=('second',))
t.run()

print('hello from main thread')