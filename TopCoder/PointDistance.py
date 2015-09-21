class PointDistance:
  def findPoint(self, x1, y1, x2, y2):
    def dist(A,B):
      import math
      return math.sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)
    for x in range(-100, 101):
      for y in range(-100, 101):
        if (x==x1 and y==y1) or (x==x2 and y==y2): continue
        if dist((x1,y1),(x,y)) > dist((x2,y2),(x,y)):
          return (x,y)
    return (-101,-101)


if __name__ == '__main__':
  print PointDistance().findPoint(0,1,2,3)
