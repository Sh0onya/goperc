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
	today = date.today() 
	dt2 = Date(today.day, today.month, today.year)
	diff = getDifference(dt1, dt2)
	perc = diff*100/1500
	for i in tqdm(range(diff), total = 1500, desc ="Progress Bar", leave = True, position = 0,ncols=100):
		if i == 0:
			system('cls')
		pass
	print(perc, "% of the goal is achieved, and a streak of", diff, "days has been reached.")
	if diff == 1500:
		print("You have done it mere cheete!!")
	if diff > 1500:
		system('cls')
		print("Bro enjoy yaar!!")
	k=input("press enter to exit...")

if __name__=="__main__":
    main()
