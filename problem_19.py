def main():
	question = "press 1 for long way or 2 for short way\n"
	ans = int(input(question))
	if ans == 1:
		long_way()
	else:
		short_way()

def long_way():

	month_list = ["January","February","March","April","May","June","July","August","September","October","November","December"]
	curr_day_num = 1
	month = 1
	year_date = 1901
	sun_count = 0
	day_in_week_count = 1

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
				elif curr_day_num == 28:
					curr_day_num = 0
					month += 1

			if year_date % 4 == 0:
				if curr_day_num == 29:
					curr_day_num = 0
					month += 1

		if day_in_week_count == 7:
			day_in_week_count = 0

		if day_in_week_count == 1:
			if curr_day_num == 1:
				sun_count += 1

		if year_date == 2000:
			break	

		print(month_list[month] + str(curr_day_num))
		curr_day_num += 1
		day_in_week_count +=1

	print(sun_count, year_date)

def short_way():
	#since 7 days in a week and 12 months in a year over 100 years
	num = 1/7 * 1200
	print(int(num))

main()