#1 Jan 1900 was a Monday.

#Thirty days has September,April, June, November.

#thirty-one days has January, March, May, July, August, October, December.

#February has twenty-eight


#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


month_list = ["January","February","March","April","May","June","July","August","September","October","November","December"]
curr_day_num = 1
day_list = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
sunday_counter = 0
month = 1
prev_month = month - 1
year_date = 1901

while True:
	if month_list[month] == "September" or month_list[month] == "June" or month_list[month] == "April" or month_list[month] == "November":
		if curr_day_num == 30:
			curr_day_num = 0
			month += 1

	if month_list[month] == "January" or month_list[month] == "March" or month_list[month] == "May" or month_list[month] == "July" or month_list[month] == "August" or month_list[month] == "October" or month_list[month] == "December":
		if curr_day_num == 31:
			if month_list[month] == "December":
				year_date += 1
				month = 0
			curr_day_num = 0
			month += 1

	if month_list[month] == "February":
		if year_date % 4 != 0:
			if curr_day_num == 28:
				curr_day_num = 0
				month += 1
		if year_date % 100 == 0:
			if year_date % 400 == 0:
				if curr_day_num == 29:
					curr_day_num = 0
					month += 1

		if year_date % 4 == 0:
			if curr_day_num == 29:
				curr_day_num = 0
				month += 1

	if year_date == 2000:
		break

	print(month_list[month] + str(curr_day_num))
	curr_day_num += 1

print(sunday_counter, year_date)