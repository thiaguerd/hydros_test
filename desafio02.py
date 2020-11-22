def is_prime(x):
  if x == 1:
    return False
  max = x - 1
  for i in range(2,( x - 1)):
    if i > max:
      return True
    if x % i == 0:
      return False
    else:
      # if x is 97 and doesn't divide by 2, no check anny bigget than 97/2 + 1 (49)
      # if x is 97 and doesn't divide by 3, no check anny bigget than 97/3 + 1 (33)
      # ...
      # if x doesn't divide by i, doesn't make sense check any number bigger than x/i + 1
      max = (x / i) + 1
  return True

def next_number(n):
  n += 1
  if is_prime(n):
    return n
  else:
    while not is_prime(n):
      n += 1
  return n

def nprimos(n):
  if not isinstance(n, int) or n < 0:
    return print(f"{n} ({type(n).__name__}) 🤨 ? C'mon dude! Give me a positive number, please!")
  prime_numbers = []
  while (len(prime_numbers) < n):
    last_number = prime_numbers[-1] if len(prime_numbers) > 0 else 0
    prime_numbers.append(next_number(last_number))
  print(prime_numbers)


