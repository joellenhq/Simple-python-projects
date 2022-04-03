import re

# define Python user-defined exceptions
class Error(Exception):
  pass

class TooManyProblems(Error):
    pass

class TooLongNumber(Error):
    pass
  
class WrongOperator(Error):
    pass

class NotANumber(Error):
    pass

def arithmetic_arranger(problems, show_result=False):

  try:
    if len(problems)>5:
      raise TooManyProblems
    x_str = ""
    y_str = ""
    u_str = ""
    sum_str = ""
    message = ""
    for i,element in enumerate(problems):
      operation = re.search(r'[+-]',element)
      if not operation:
        raise WrongOperator
      #x = re.findall("\d*\d", element)
      x = element.split(operation.group())
      x = [numbers.strip() for numbers in x if len(numbers)>0]
      for number in x:
        if re.findall("\D",number) or len(x)>2:
          raise NotANumber
      #print(x)
      spaces = len(x[0]) - len(x[1])
      if len(x[0])>4 or len(x[1])>4:
        raise TooLongNumber
      
      while spaces != 0:
        if spaces > 0:
          x[1]=" "+x[1]
        else:
          x[0]=" "+x[0]
        spaces = len(x[0])-len(x[1])
      
      x[0] = '  ' + x[0]
      if not operation:
        raise WrongOperator
      if operation.group() == '+':
        sum = str(int(x[0]) + int(x[1]))
      else:
        sum = str(int(x[0]) - int(x[1]))
      concatenated_string = operation.group() + ' ' + x[1]
      underscore_string = ''
      
      for _ in x[0]:
        underscore_string = underscore_string + '-'
        if len(underscore_string) > len(sum):
          sum = ' ' + sum
      
      x_str = x_str + x[0]
      y_str = y_str + concatenated_string
      u_str = u_str + underscore_string
      sum_str = sum_str + sum
      if i<len(problems)-1:
        x_str = x_str + "    "
        y_str = y_str + "    "
        u_str = u_str + "    "
        sum_str = sum_str + "    "
    message = x_str + "\n" + y_str + "\n" + u_str 

    if show_result:
      message = message + "\n" + sum_str
    message = message.rstrip()
  except TooManyProblems:
    message = 'Error: Too many problems.'
  except WrongOperator:
    message = "Error: Operator must be '+' or '-'."
  except NotANumber:
    message = 'Error: Numbers must only contain digits.'
  except TooLongNumber:
    message = 'Error: Numbers cannot be more than four digits.'
    #return arranged_problems
  #print(message)
  return message