import copy
import random
# Consider using the modules imported above.

class Hat:
  
  def __init__(self, **arguments):
    
    self.contents = []
    
    for key,value in arguments.items():
        for _ in range(value):
          self.contents.append(key)
        # print(self.contents)
  
  def draw(self, number_of_balls):
    removed_balls = []
    if len(self.contents)>number_of_balls:
      for _ in range(number_of_balls):
        picked = random.choice(self.contents)        
        self.contents.remove(picked)
        removed_balls.append(picked)
      return removed_balls
    return self.contents

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  found = False
  # hat1 = Hat(red=1)
  found_balls = 0
  for _ in range(num_experiments):
    hat1 = copy.deepcopy(hat)
    picked_balls = hat1.draw(num_balls_drawn)
    picked_balls_dict = {}
    
    for color in picked_balls:
      if color in picked_balls_dict:
        picked_balls_dict[color] += 1
      else:
        picked_balls_dict[color] = 1
    found = True
    for key,value in expected_balls.items():  
      try:
        if value > picked_balls_dict[key]:
          found = False
      except KeyError:
        found = False

    if found:
      found_balls += 1
      
  # print(picked_balls_dict)
  # print(expected_balls)
  probability = found_balls/num_experiments

  # print(probability)
  return probability

