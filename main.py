from time import perf_counter

def expt(x, n):
  if n < 0:
    raise ValueError("n = {} is less than zero".format(n))
    
  if n == 0:
    return 1
  elif n % 2 == 0:
    results = expt(x, n // 2)
    return results * results
  else:
    return x * expt(x, n - 1)

def old_expt(x, n):
  if n < 0:
    raise ValueError("n = {} is less than zero".format(n))
  elif n == 0:
    return 1
  else:
    return x * expt(x, n - 1)
    

def main():
  f = open("expt_data.csv", "w")
  f.write("exponent,min_runtime_old,min_runtime_new\n")

  x_exponents = 10000
  x_trials = 10
  base = 17
  for exponent in range(x_exponents):
    min_runtime_new = 1e10
    for _ in range(x_trials):
      runtime = perf_counter()
      answer = expt(base, exponent)
      runtime = perf_counter() - runtime

      if runtime < min_runtime_new:
          min_runtime_new = runtime

    min_runtime_old = 1e10
    for _ in range(x_trials):
      runtime = perf_counter()
      answer = old_expt(base, exponent)
      runtime = perf_counter() - runtime

      if runtime < min_runtime_old:
           min_runtime_old = runtime
      
    print(f"Writing exponent {exponent}")
    f.write(f"{exponent},{min_runtime_old},{min_runtime_new}\n")
  f.close()
    
    
if __name__ == '__main__':
  main()