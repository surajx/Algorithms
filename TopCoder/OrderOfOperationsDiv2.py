class OrderOfOperationsDiv2:
  def minTime(self, s):
    def countOne(string):
      cnt=0
      for i in string:
        if i=="1": cnt+=1
      return cnt
    s = sorted(s, key=countOne)
    hit = ["0"]*len(s[0])
    time = 0
    for i in range(len(s)):
      hitCount = 0
      timeCnt = 0
      tmp_hit = hit
      for k in range(len(hit)):
        if s[i][k]=="1" and hit[k]=="1":
          hitCount+=1
          tmp_hit[k] = 1
      for j in range(i+1,len(s)):
        if countOne(s[j]) > countOne(s[i]): break
        else:
          newHitCount = 0
          newtmp_hit = tmp_hit
          for k in range(len(hit)):
            if s[j][k]=="1" and tmp_hit[k]=="1":
              newHitCount+=1
              newtmp_hit[k] = 1
          if newHitCount > hitCount:
            s[j], s[i] = s[i], s[j]
            hitCount = newHitCount
            tmp_hit = newtmp_hit
      hit = tmp_hit
      for k in range(len(hit)):
        if s[i][k]=="1" and hit[k]=="0":
          timeCnt+=1
          hit[k] = "1"
      time += timeCnt**2
    return time

if __name__ == '__main__':
  print OrderOfOperationsDiv2().minTime(("1001","0110","0010","1110","1111"))
