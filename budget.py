import math
import re

class Category:
  def __init__(self, name):
    self.ledger = []
    self.balance = 0
    self.name = name
    
  def deposit(self, amount, description = ''):
    self.ledger.append({"amount": amount, "description": description})
    self.check_funds(amount)
    self.balance = self.balance + amount
    
  def withdraw(self, amount, description = ''):
    if self.balance - amount >= 0:
      self.ledger.append({"amount": -amount, "description": description})
      self.check_funds(amount)
      self.balance = self.balance - amount
      return True
    return False
    
  def get_balance(self):
    return self.balance
    
  def transfer(self, amount, budget):
    # print(budget)
    if self.balance - amount >= 0:
      self.withdraw(amount, f"Transfer to {budget.name}")
      budget.deposit(amount, f"Transfer from {self.name}")
      return True
    return False
    # self.print_obj()

  def check_funds(self, amount):
    if amount > self.balance:
      return False
    return True

  def __str__(self):
    str3 = ''
    stars = int((30 - len(self.name))/2)
    str1 = ''
    for _ in range(stars):
      str1 = str1 + '*'
    str3 = str1 + self.name + str1 + "\n"
    for el in self.ledger:
      # print(el)
      # print(el.ledger)
      # print(el['amount'])
      # print(el['description'])
      amount1 = str(round(float(el['amount']),2))
      len_amount = amount1.split(".")
      if len(len_amount[-1]) < 2:
        amount1 = amount1 + "0"
      # print(amount1)
      spaces = 30 - len(str(el['description'])[:23]) - len(amount1) 
      str2= ''
      for _ in range(spaces):
        str2 = str2 + ' '
      str3 = str3 + (str(el['description']))[:23]+str2+amount1 + "\n"
    str3 = str3 + ("Total: "+str(self.balance)) #+ "\n"
    # print(str3)
    return str3
    

def create_spend_chart(categories):
  
  line1 = "Percentage spent by category"
  line = []
  for i in range(11):
    if i>0 and i!=10:
      line.append(' '+str(100-i*10) + '|')
    elif i == 10:
      line.append('  '+str(100-i*10) + '|')
    else:
      line.append(str(100-i*10) + '|')
  sum = 0
  budget1 = []
  
  names = []
  for i,ctgr in enumerate(categories):
    # print(ctgr.name)
    names.append(ctgr.name)
    count = 0
    for el in ctgr.ledger:
      if el['amount']<0:
        count = count + abs(el['amount'])
      # print(count)
    budget1.append(count)
    # print("budget: ", str(budget1))
    sum = sum + budget1[i]
    
    line2 = []
    # print(names)
    names_len = list(map(lambda name: len(name), names))
    # print(names_len)

  # print(len(ctgr.name) < max(names_len))
  for i,el in enumerate(names):
    # print(el)
    while len(names[i]) < max(names_len):
      names[i] = names[i] + ' '

  for i,name in enumerate(names):
    for j in range(max(names_len)):
      if i==0:
        line2.append("     " + name[j])
      else:
        line2[j] = line2[j] + "  " + name[j]
        # print(line2[j])
  
  percentage = list(map(lambda a : math.floor(a/sum*10)*10, budget1))
  for i, percent in enumerate(percentage):
    for j in range(len(line)):
      if percent >= int(line[j].split("|")[0].strip()):
        line[j] = line[j] + " o "
      else:
        line[j] = line[j] + "   "
  for lin in line:
    line1 = line1 + '\n' + lin + " "
  text = "    "

  line1 = line1 + '\n' + text.ljust((len(names)*2+4+4),"-")
  line3 = ""
  for lin in line2:
    line3 = line3 +'\n'+ lin + '  '
  line1 = line1 + line3
  # print(line1)

  return line1