def add_time(start, duration, day=""):
  # split the start hours and minutes into their own variables
  full_time = start.split(" ")[0]
  start_hrs, start_mins = int(full_time.split(":")[0]), int(full_time.split(":")[1])
  # convert it to 24-hour time
  if start.split(" ")[1] == "PM":
    start_hrs += 12

  # add the duration times to the start times
  added_hours = int(duration.split(":")[0]) + start_hrs
  added_mins =  int(duration.split(":")[1]) + start_mins

  # if the minutes will add extra hour(s)
  if added_mins > 60:
    # added the extra hours to the added_hours
    added_hours += int(added_mins / 60)
    # reset the added_mins to the minutes leftover
    added_mins = added_mins % 60

  # figure out how many days later (if any) the new time is
  days_later_text = ""
  days_later = int(added_hours / 24)
  if days_later == 1:
    days_later_text = " (next day)"
  elif days_later > 1:
    days_later_text = " (" + str(days_later) + " days later)"

  # reset the added_hours to the hours leftover
  added_hours = added_hours % 24

  # set AM or PM
  if added_hours >= 12:
    part_of_day = "PM"
    if added_hours > 12:
      # convert hours back to 12-hour format
      added_hours = added_hours - 12
  else:
    part_of_day = "AM"
    # if the time is 0, reset it to 12
    if added_hours == 0:
      added_hours = 12
  
  day_text = ""
  # if a day of the week was passed in
  if day:
    # create an array of the days
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    # find the index of the current day in the array
    day_index = days_of_week.index(day.capitalize())
    # starting with the current day, move that many positions forward in the list and return the day
    day_text = ", " + days_of_week[(day_index + (days_later % 7)) % 7]

  # build the string to return the new time
  new_time = str(added_hours) + ":" + f"{added_mins:02d}" + " " + part_of_day
  if day_text:
    new_time += day_text
  if days_later_text:
    new_time += days_later_text

  return new_time
