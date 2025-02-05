#ApproxPi.py
#Name:
#Date:
#Assignment:
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  realPi = math.pi

  #ask user for decimal percision (up to 10)
  approxPi = 4/1
  sign = -1
  denom = 3
  
  start = time.time()

  while round(approxPi, 2) != round(realPi, 2):
    approxPi = approxPi + sign * 4/denom
    sign = sign * -1 
    denom = denom + 2 
  #calculate pi using the approximation technique
  #Loop until the level of percision is reached

  end = time.time()

  elapsedTime = end - start
  print(elapsedTime)

if __name__ == '__main__':
  main()
