from client import Client

class Sprinkler(Client):
  
  def __init__(self, state):
    self.state = False
