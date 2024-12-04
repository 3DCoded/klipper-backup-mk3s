import threading

t = threading.Thread(lambda: print('hello from second thread'))
t.run()

print('hello from main thread')