class LiveConcert:
  def maxHappiness(self, h, s):
    sung = []
    happiness = 0
    hi = list(h)
    while set(s)!=set(sung):
      if not hi:
        break
      mx_h = max(hi)
      mx_idx = hi.index(mx_h)
      sung.append(s[mx_idx])
      del hi[mx_idx]
      happiness+=mx_h
    return happiness




if __name__ == '__main__':
  print LiveConcert().maxHappiness((1,2,3,4,5,6,7,8,9,10,100),("a","b","c","d","e","e","d","c","b","a","abcde"))
