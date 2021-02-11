from client import Client

import time

class Ac(Client):
  
  def __init__(self, state, temp):
    self.state = False
    self.temp = 18

  def reports(self):
    time.sleep(2)
    return f"State:{self.state} temp:{self.temp}ºC"



