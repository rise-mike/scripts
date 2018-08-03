import datetime

startDate = '05-01-2018'
endDate = '05-12-2018'

def formatDate(dateList):
  # Returns a list of ints representing a date in the format [YYYY, MM, DD], with leading zeros removed
  noZero = []
  for date in dateList.split('-'):
    if date[0] != "0":
      noZero.append(int(date))
    else:
      noZero.append(int(date[1]))
  noZero.reverse()
  return noZero

# Datetime needs three ints to represent a date
def makeDateTime(dateList):
  day = dateList[1]
  month = dateList[2]
  year = dateList[0]
  dateTimeObj = datetime.date(year, month, day)
  return dateTimeObj

def timeBtweenWeeks(startWk, endWk):
  # Takes in a "start" date and a "go_live" date
  start = makeDateTime(formatDate(startWk))
  end = makeDateTime(formatDate(endWk))
  diff = (end - start).days
  weeks = round(diff / 7)
  # print("Difference: ", diff, " days.")
  # print("That's ", weeks, " weeks!")
  return weeks

timeBtweenWeeks(startDate, endDate)


   