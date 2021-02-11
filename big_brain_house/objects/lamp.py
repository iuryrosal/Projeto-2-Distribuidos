from client import Client

class Lamp(Client):
  
  def __init__(self, state):
    self.state = False
