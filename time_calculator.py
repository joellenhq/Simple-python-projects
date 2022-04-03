def add_time(start, duration, day=None):
  time_format = start[-2:]
  hour_str1, minutes_str1 = start[:-2].strip().split(':')
  hour_str2, minutes_str2 = duration.strip().split(':')
  hour1 = int(hour_str1)
  
  if time_format == "PM":
    hour1+=12
  hour2 = int(hour_str2)
  minutes1 = int(minutes_str1)
  minutes2 = int(minutes_str2)

  new_minutes = minutes1+minutes2
  while new_minutes >= 60:
    new_minutes -= 60
    #print(new_minutes)
    hour1 += 1
  if new_minutes<10:
    new_minutes_str = '0'+ str(new_minutes)
  else:
    new_minutes_str = str(new_minutes)
  new_hour = hour1 + hour2
  
  next_days = 0
  while new_hour >= 24:
    new_hour -= 24
    next_days +=1
  if new_hour >= 12:
    new_hour -= 12
    new_time_format = " PM"
  else:
    new_time_format = " AM"
  if new_hour == 0:
    new_hour = 12
  new_time = str(new_hour)+":"+new_minutes_str+new_time_format
  week_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
  if day != None:
    index = week_days.index(day.lower())
    days = next_days + index
    while days > 6:
      days -= 7
      #days = next_days + index
    new_day = week_days[days]
    new_time = new_time + ", " + new_day.capitalize()
  if next_days>0:
    caption = " (next day)"
    if next_days > 1:
      caption = " (" + str(next_days) + " days later)"
    new_time = new_time + caption

  return new_time