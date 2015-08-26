def fib_naive(n):
  """
  This is a naive recursive solution to finding the nth fibinacci numbers
  Returns Int"""
  if n<=1: return n
  return fib_naive(n-1) + fib_naive(n-2)

def fib_dp_td(n):
  """
  Dynamic programming approach to memoize already computed values while recusing.
  Return Int"""
  #1. Memorize the value of each recurrence in an array.
  #2. If a particualr values is needed again instead of calling the recursion
    # pick that value from the array.
  memoize_fib = [0]*n
  saved_iteration_cnt = [0]
  def fib(n):
    if n<=1:
      memoize_fib[n-1] = n
      return n
    if memoize_fib[n-1]!=0:
      saved_iteration_cnt[0] += 1 # if we didnt want to know how many iterations
      # we saved usign the memoization we could have avoided the if statement.
    else:
      memoize_fib[n-1] = fib(n-1)+fib(n-2)
    return memoize_fib[n-1]
  nth_fib = fib(n)
  print "Memoized values:", memoize_fib
  print "Saved number of iterations:", saved_iteration_cnt
  return nth_fib

def fib_dp_bu(n):
  """Dynamic programming approach with tablulation and bottoms up approach
  to find the n(th) fibonacci number
  Returns Int"""
  dp_table = [0]*n
  for i in range(n):
    if i<2:
      dp_table[i] = i
    else:
      dp_table[i] = dp_table[i-1] + dp_table[i-2]
  print dp_table
  return dp_table[n-1]

if __name__ == '__main__':
  from datetime import datetime
  t1 = datetime.now()
  print fib_naive(40)
  print "Time for Naive:", datetime.now()-t1
  t1 = datetime.now()
  print fib_dp_td(40)
  print "Time for DP TD:", datetime.now()-t1
  t1 = datetime.now()
  print fib_dp_bu(40)
  print "Time for DP BU:", datetime.now()-t1
