from sys import api_version
from RPSLS_player import RPSLS_player

class P19892(RPSLS_player):
  def __init__(self):
    self.n = 0
    self.a = ["lizard", "paper", "spock", "rock", "scissors"]

  def shoot(self):
    try:
      if self.result ==  "win":
        pass
      elif self.result == "lose":
        self.n += 1
      else:
        self.n += 2
      return self.a[self.n % 5]
    except:
      return self.a[self.n % 5]
  
  def update(self, result: str, competitor_shot: str):
    self.result = result