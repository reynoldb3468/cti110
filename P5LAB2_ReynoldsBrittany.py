def feet_to_steps(num_feets):
  steps = (num_feets / 2.5) 
  num_steps = int(steps)     
  return num_steps

if __name__ == "__main__":
  num_feets = float(input())
  num_steps = feet_to_steps(num_feets)
  print(num_steps)