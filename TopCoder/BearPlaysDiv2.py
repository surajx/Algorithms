class BearPlaysDiv2:
  def equalPiles(self, A, B, C):
    L = [A, B, C]
    L_occour = []
    while True:
      print L_occour
      L = sorted(L)
      if (L[0], L[1], L[2]) in L_occour:
        return "impossible"
      else:
        L_occour.append((L[0], L[1], L[2]))
      L[1]=L[1]-L[0]
      L[0]*=2
      if L[0] == L[1] and L[1] == L[2]:
        return "possible"

if __name__ == '__main__':
  #print BearPlaysDiv2().equalPiles(1,1,2)
  print BearPlaysDiv2().equalPiles(10,15,35)
