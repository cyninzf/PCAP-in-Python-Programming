# 4.3.1.6 LAB 
# A leap year: writing your own functions

def is_year_leap(year):
      if year % 4 == 0:
            return True
            
test_data=[1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range (len(test_data)):
      yr = test_data[i]
      result = is_year_leap(yr)
      print(yr, "->", end ="")
      if result == test_results[i]:
            print("OK")
      else:
            print("Failsed")    
print("\n")

# 4.3.1.7 LAB 
# How many days: writing and using your own functions

def is_year_leap(year):
      if year % 4 == 0:
            return True
      
def days_in_month(year,month):
      if year % 4 == 0:
            if month != 2:
                  days_in_month == 31
            else:
                 days_in_month == 29
      elif month != 2:
            days_in_month == 30
      else:
            days_in_month == 28 

test_years =[1900, 2000, 2016, 1987]
test_months = [2,2,1,11]
test_results = [28, 29, 31, 30]
for i in range (len(test_years)):
      yr = test_years[i]
      mo = test_months[i]
      print(yr, mo, "-> ", end="")
      result = days_in_month(yr,mo)
      if result == test_results[i]:
            print("OK")
      else:
            print("Failsed")    
print("\n")


# 4.3.1.8 LAB 
# Days of the year: writing and using your own functions

def is_year_leap(year):
      if year % 4 == 0:
            return True
      
def days_in_month(year,month):
      if year % 4 == 0:
            if month != 2:
                  days_in_month == 31
            else:
                 days_in_month == 29
      elif month != 2:
            days_in_month == 30
      else:
            days_in_month == 28 
            
def day_of_year(year, month, day):


print(day_of_year(2000,12,31))    
print("\n")
