from datetime import date
from tqdm import tqdm 
from os import system
class Date:
	def __init__(self, d, m, y):
		self.d = d
		self.m = m
		self.y = y

monthDays = [31, 28, 31, 30, 31, 30,
			31, 31, 30, 31, 30, 31]


def countLeapYears(d):

	years = d.y

	if (d.m <= 2):
		years -= 1

	return int(years / 4) - int(years / 100) + int(years / 400)

def getDifference(dt1, dt2):

	n1 = dt1.y * 365 + dt1.d

	for i in range(0, dt1.m - 1):
		n1 += monthDays[i]
	n1 += countLeapYears(dt1)

	n2 = dt2.y * 365 + dt2.d
	for i in range(0, dt2.m - 1):
		n2 += monthDays[i]
	n2 += countLeapYears(dt2)	
	return (n2 - n1)

def main():
	dt1 = Date(26, 10, 2020)
	days = 1500
	p1 = int(days/10)
	p2 = int(days*30/100)
	p3 = int(days*60/100)
	today = date.today() 
	dt2 = Date(today.day, today.month, today.year)
	diff = getDifference(dt1, dt2)
	diff_p1 = diff_p2 = diff_p3 = diff
	perc = diff*100/days
	rem = days - diff
	if diff_p1 >= p1:
		diff_p1 = p1
	if diff_p2 >= p2:
		diff_p2 = p2
	if diff_p3 >= p3:
		diff_p3 = p3
	for i in tqdm(range(diff_p1), total = p1, desc ="Phase 1"):
		pass
	for i in tqdm(range(diff_p2), total = p2, desc ="Phase 2"):
		pass
	for i in tqdm(range(diff_p3), total = p3, desc ="Phase 3"):
		pass
	for i in tqdm(range(diff), total = days, desc ="Course "):
		pass
	print(round(perc,2),"% of the goal is achieved, and a streak of ",diff," days or ",round(diff/7)," weeks or ",round(diff/30.4167)," months has been reached.\nYou have to maintain it for ",rem," days or ",round(rem/7)," weeks or ",round(rem/30.4167)," months more. \nYou must achieve the ",days," days or ",round(days/7)," weeks or ", round(days/30.4167)," months mark.",sep="")
	if diff >= p1:
		print("You have successfully completed the first phase. Keep Hustling!!")
	if diff >= p2:
		print("You have successfully completed the Second phase. Keep Hustling!!")
	if diff >= p3:
		print("You have successfully completed the Third phase. Keep Hustling!!")
	if diff == days:
		print("You have done it mere cheeete!!")
	if diff > days:
		system('cls')
		print("Attention!! don't enjoy, continue the streak!!\nYou have to achive a lot more.")
	k=input("press enter to exit...")

if __name__=="__main__":
    main()
