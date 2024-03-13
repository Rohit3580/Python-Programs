
days = int(input("Enter the number of days:"))

Year = days//365
rDays = days % 365

Week = rDays//7
Day = rDays % 7

print("Years:",Year,"Weeks:",Week,"Days:",Day)
