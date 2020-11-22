def next_number(fibonacci_sequence):
  # item -2 (penultimate) or 1
  penultimate_item = fibonacci_sequence[-2] if len(fibonacci_sequence) > 1 else 0
  # item -1 (last) or 1
  last_item = fibonacci_sequence[-1] if bool(fibonacci_sequence) else 1
  return penultimate_item + last_item

def fibonacci(n):
  if not isinstance(n, int) or n < 0:
    return print(f"{n} ({type(n).__name__}) 🤨 ? C'mon dude! Give me a positive number, please!")
  aux = 0
  fibonacci_sequence = []
  while (aux < n):
    fibonacci_sequence.append(next_number(fibonacci_sequence))
    aux += 1
  print(fibonacci_sequence)
