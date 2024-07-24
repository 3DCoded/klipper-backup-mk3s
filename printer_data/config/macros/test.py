def add(a, b):
  return a + b

a = kwargs.get('a', 0)
b = kwargs.get('b', 0)
c = add(a, b)
print(c)
output(f'{a} + {b} = {c}')