#!/usr/bin/env python3
import requests

def main():
  mytoken = '2b9e7aa259306e47eb5bf82bf35d79828486988a7536dde9'
  myapi = "https://fonoapi.freshpixl.com/v1/getlatest"
  mybuiltapi = myapi + "?token=" + mytoken
  
  ## translate our JSON response to a series of Python lists and dictionaries
  myjson = requests.get(mybuiltapi).json()
  
  ## Display a list of what inside our JSON
  for x in myjson:
    print(x)
  
if __name__ == '__main__':
  main()

