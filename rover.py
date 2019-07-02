#!/usr/bin/python3

import sys
import os
import json
import math
import getopt

class RoverClient:
  NORTH = math.pi / 2
  WEST = math.pi
  EAST = 0
  SOUTH = math.pi + (math.pi / 2)

  def __init__(self, origin, heading):
    self.origin = origin
    self.distance = float(math.sqrt(math.pow(origin[0], 2) + math.pow(origin[1], 2)))
    self.theta = 0.0
    self.heading = heading  

  def position(self):
    return [round(math.cos(self.theta) * self.distance,2) , round(math.sin(self.theta) * self.distance,2) ]

  def move(self, command):
    for i in command:
      if i == "l":
        self.heading = self.heading + math.pi / 2.0
      elif i == "r":
        self.heading = self.heading - math.pi / 2.0
      elif i == "f" or i == "b":
        a = [math.cos(self.theta)*self.distance, math.sin(self.theta)*self.distance]
        b = [math.cos(self.heading), math.sin(self.heading)]
        c = [a[0] + b[0], a[1] + b[1]] if i == "f" else [a[0] - b[0], a[1] - b[1]]
        self.distance = math.sqrt(math.pow(c[0],2) + math.pow(c[1],2))
        self.theta = math.acos(c[0]/self.distance) if self.distance != 0 else 0

    return self.position()

if (__name__ == "__main__"):
  heading = None
  origin = None
  opts, args = getopt.getopt(sys.argv[1:], "h:o:")
    
  for opt,arg in opts:
    if opt == "-h":
      heading = float(arg) / math.pi
    if opt == "-o":
      origin = [float(list(arg)[0]), float(list(arg)[1])]

  if heading is None:
    heading = math.pi / 2.0

  if origin is None:
    origin = [0.0, 0.0]
        
  client = RoverClient(origin, heading)
  
  while True:
    command = sys.stdin.readline()  
    print(client.move(command))
