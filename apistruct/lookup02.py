#!/usr/bin/env python3
import requests
import pprint 

def main():
  mytoken = '2b9e7aa259306e47eb5bf82bf35d79828486988a7536dde9'
  myapi = "https://fonoapi.freshpixl.com/v1/getlatest"
  mybuiltapi = myapi + "?token=" + mytoken
  
  ## ask user for a brand to search on
  brand = input("What brand of device are you searching for?")
  brand = "&brand=" + brand
  
  ## translate our JSON response to a series of Python lists and dictionaries
  myjson = requests.get(mybuiltapi + brand).json()
  
  ## Display a list of what inside our JSON
  for x in myjson:
    pprint.pprint(x)
  
if __name__ == '__main__':
  main()

