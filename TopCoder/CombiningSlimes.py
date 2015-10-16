class CombiningSlimes:
  def maxMascots(self, s):
    slimes = list(s)
    mascot = 0
    while len(slimes)>1:
      mx1 = max(slimes)
      slimes.remove(mx1)
      mx2 = max(slimes)
      slimes.remove(mx2)
      slimes.append(mx1+mx2)
      mascot+=mx1*mx2
    return mascot

if __name__ == '__main__':
  print CombiningSlimes().maxMascots((7,6,5,3,4,6))
