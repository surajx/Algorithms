class BootsExchange:
  def leastAmount(self, left, right):
    least = 0
    for l in left:
      if l in right:
        del right[right.index(l)]
      else:
        least+=1
    return least

if __name__ == '__main__':
  x = BootsExchange()
  print x.leastAmount([1, 3, 1], [2, 1, 3])
  print x.leastAmount([1, 3], [2, 2])
  print x.leastAmount([1, 2, 3, 4, 5, 6, 7], [2, 4, 6, 1, 3, 7, 5])
