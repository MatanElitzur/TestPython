import turtle
import sys

def main():
  # define a variable to hold the source URL
  # In this case we'll use the free data feed from the USGS
  # This feed lists all earthquakes for the last day larger than Mag 2.5
  t = turtle.Pen()
  
  t.circle(100)
  
  t.forward(50)
  t.left(90)
  t.forward(50)
  t.left(90)
  t.forward(50)
  t.left(90)
  t.forward(50)
  t.left(90)
  t.reset()
  
  t.backward(100)
  t.up()
  t.right(90)
  t.forward(20)
  t.left(90)
  t.down()
  t.forward(100)
  t.reset()
  
  t.circle(100)
  
  print(sys.stdin.readline())
  i = 0
  print(i);

if __name__ == "__main__":
  main()
