from datetime import date, datetime
from tqdm import tqdm 
from os import system,path
from colorama import Fore, Style, init


init(convert=True)

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
	#dt1 = Date(26, 10, 2019)
	#dt1 = Date(28, 11, 2020)
	#dt1 = Date(25, 12, 2020)
	dt1 = Date(11, 3, 2021)
	goal = 1500
	my_date = datetime(dt1.y,dt1.m,dt1.d)
	idayTstamp = datetime.timestamp(my_date)
	days = goal
	goalTstamp = goal*24*60*60
	fDay = datetime.fromtimestamp(goalTstamp-24*60*60+idayTstamp)
	fDay = fDay.strftime("%d %B, %Y")
	iDay = my_date.strftime("%d %B, %Y")
	fpfDay = datetime.fromtimestamp((goalTstamp-24*60*60)*0.1+idayTstamp)
	fpfDay = fpfDay.strftime("%d %B, %Y")
	spiDay = datetime.fromtimestamp((goalTstamp)*0.1+idayTstamp)
	spiDay = spiDay.strftime("%d %B, %Y")
	spfDay = datetime.fromtimestamp((goalTstamp-24*60*60)*0.3+idayTstamp)
	spfDay = spfDay.strftime("%d %B, %Y")
	tpiDay = datetime.fromtimestamp((goalTstamp)*0.3+idayTstamp)
	tpiDay = tpiDay.strftime("%d %B, %Y")
	tpfDay = datetime.fromtimestamp((goalTstamp-24*60*60)*0.6+idayTstamp)
	tpfDay = tpfDay.strftime("%d %B, %Y")
	diff_x = days
	p1 = int(days/10)
	p2 = int(days*30/100)
	p3 = int(days*60/100)
	today = date.today() 
	dt2 = Date(today.day, today.month, today.year)
	diff = getDifference(dt1, dt2)
	repeat = (days-diff)/diff
	repeat_days = repeat - int(repeat)
	repeat = int(repeat)
	repeat_days = int(repeat_days*diff)
	diff_p1 = diff_p2 = diff_p3 = diff
	perc = diff*100/days
	rem = days - diff
	if diff_p1 >= p1:
		diff_p1 = p1
	if diff_p2 >= p2:
		diff_p2 = p2
	if diff_p3 >= p3:
		diff_p3 = p3
	if diff > days:
		days = diff
	for i in tqdm(range(diff), total = days, desc = Fore.BLUE+Style.BRIGHT+"Course X"):
		pass
	print("\n")
	for i in tqdm(range(diff_p1), total = p1, desc = Fore.RED+Style.BRIGHT+"Phase 1"):
		pass
	for i in tqdm(range(diff_p2), total = p2, desc = Fore.WHITE+Style.BRIGHT+"Phase 2"):
		pass
	for i in tqdm(range(diff_p3), total = p3, desc = Fore.GREEN+Style.BRIGHT+"Phase 3"):
		pass

	tab = "\t\t\t       "
	if perc <= 10:
		tab = "\t\t\t\t       "
	if perc > 59:
		tab = "\t\t\t\t       "

	if perc < 0:
		perc = 0
	
	print("\nToday's Date:- ",date.today().strftime("%d %B, %Y"))
	print("Goal:",goal,"Days")
	print("Today is Day",diff+1)
	
	print("\nInitiation Day:-",iDay,"\t\t\tFinal Day:-",fDay)
	if diff <= goal:
		print("Goal Achieved: ",round(perc,2),"%",tab,"Goal Left: ",round(100-perc,2),"%")
		print(Fore.BLUE+Style.BRIGHT+"\nDays Completed: ",diff,"Days","\t\t\t\tDays Left: ",rem,"Days")
		print("Weeks Completed: ",round(diff/7),"Weeks","\t\t\t\tWeeks Left: ",round(rem/7),"Weeks")
		print("Months Completed: ",round(diff/30.4167),"Months","\t\t\t\tMonths Left: ",round(rem/30.4167),"Months")
		print("Years Completed: ",round(diff/365.25),"Years","\t\t\t\tYears Left: ",round(rem/365.25),"Years")
	else:
		print("Goal Achieved: ",round(perc,2),"%")
		print(Fore.BLUE+Style.BRIGHT+"\nDays Completed: ",diff,"Days")
		print("Weeks Completed: ",round(diff/7),"Weeks")
		print("Months Completed: ",round(diff/30.4167),"Months")
		print("Years Completed: ",round(diff/365.25),"Years")


	if diff > goal:
		perc_p1 = diff_p1*100/p1
		p1_rem = p1 - diff_p1
		print(Fore.RED+Style.BRIGHT+"\nPhase 1")
		print("Initiation Day: ",iDay,"\t\t\tFinal Day: ",fpfDay)
		perc_p2 = diff_p2*100/p2
		p2_rem = p2 - diff_p2
		print(Fore.WHITE+Style.BRIGHT+"\nPhase 2")
		print("Initiation Day: ",spiDay,"\t\t\t\tFinal Day: ",spfDay)
		perc_p3 = diff_p3*100/p3
		p3_rem = p3 - diff_p3
		print(Fore.GREEN+Style.BRIGHT+"\nPhase 3")
		print("Initiation Day: ",tpiDay,"\t\t\t\tFinal Day: ",tpfDay)


	if diff < p1:
		perc_p1 = diff_p1*100/p1
		p1_rem = p1 - diff_p1
		print(Fore.RED+Style.BRIGHT+"\nPhase 1")
		print("Initiation Day: ",iDay,"\t\t\tFinal Day: ",fpfDay)
		print("Phase Completed: ",round(perc_p1,2),"%","\t\t\t\tPhase Left: ",round(100-perc_p1,2),"%")
		print("Days Completed: ",diff_p1,"Days","\t\t\t\tDays Left: ",p1_rem,"Days")
		print("Weeks Completed: ",round(diff_p1/7),"Weeks","\t\t\t\tWeeks Left: ",round(p1_rem/7),"Weeks")
		print("Months Completed: ",round(diff_p1/30.4167),"Months","\t\t\t\tMonths Left: ",round(p1_rem/30.4167),"Months")
		print("Years Completed: ",round(diff_p1/365.25),"Years","\t\t\t\tYears Left: ",round(p1_rem/365.25),"Years")
	if (diff >= p1 and diff < p2):
		perc_p2 = diff_p2*100/p2
		p2_rem = p2 - diff_p2
		print(Fore.WHITE+Style.BRIGHT+"\nPhase 2")
		print("Initiation Day: ",spiDay,"\t\t\t\tFinal Day: ",spfDay)
		print("Phase Completed: ",round(perc_p2,2),"%","\t\t\t\tPhase Left: ",round(100-perc_p2,2),"%")
		print("Days Completed: ",diff_p2,"Days","\t\t\t\tDays Left: ",p2_rem,"Days")
		print("Weeks Completed: ",round(diff_p2/7),"Weeks","\t\t\t\tWeeks Left: ",round(p2_rem/7),"Weeks")
		print("Months Completed: ",round(diff_p2/30.4167),"Months","\t\t\t\tMonths Left: ",round(p2_rem/30.4167),"Months")
		print("Years Completed: ",round(diff_p2/365.25),"Years","\t\t\t\tYears Left: ",round(p2_rem/365.25),"Years")
	if (diff >= p2 and diff < p3):
		perc_p3 = diff_p3*100/p3
		p3_rem = p3 - diff_p3
		print(Fore.GREEN+Style.BRIGHT+"\nPhase 3")
		print("Initiation Day: ",tpiDay,"\t\t\t\tFinal Day: ",tpfDay)
		print("Phase Completed: ",round(perc_p3,2),"%","\t\t\t\tPhase Left: ",round(100-perc_p3,2),"%")
		print("Days Completed: ",diff_p3,"Days","\t\t\t\tDays Left: ",p3_rem,"Days")
		print("Weeks Completed: ",round(diff_p3/7),"Weeks","\t\t\t\tWeeks Left: ",round(p3_rem/7),"Weeks")
		print("Months Completed: ",round(diff_p3/30.4167),"Months","\t\t\t\tMonths Left: ",round(p3_rem/30.4167),"Months")
		print("Years Completed: ",round(diff_p3/365.25),"Years","\t\t\t\tYears Left: ",round(p3_rem/365.25),"Years")

	if diff == days and diff_x == days:
		print(Fore.BLUE+Style.BRIGHT+"\nYou have done it mere cheeete!!")
		print(date.today().strftime("%B %d, %Y"),"is the day when you won over your mind!!")
		wond = open('wond.txt','w')
		wond.write(date.today().strftime("%B %d, %Y"))
		wond.close()
	if diff_x < days:
		#system('cls')
		wond = open('wond.txt','r')
		print()
		print(wond.read(),"is the day when you won over your mind!!\n")
		wond.close()
		print(Fore.RED+Style.BRIGHT+"Attention!! don't do it unless you are doing it in the correct manner.\nContinue the streak!!You have to achive a lot more.")

	performed = False
	exist = path.exists('performed.txt')
	if exist:
		done = open('performed.txt','r')
		performed = done.read()
	if performed:
		system('cls')
		print("\n"+Fore.CYAN+Style.BRIGHT+"Congratulations, enjoy!!")
		exist = path.exists('wond.txt')
		if exist:
			wond = open('wond.txt','r')
			print("\nAlways remember",wond.read(),"is the day when you won over your mind!!")
			wond.close()

		
	if(repeat_days > 0):
		repeat_message = ", with an add on of "+str(repeat_days)+" days."
	else:
		repeat_message = "."
	if(repeat > 1):
		print(Fore.CYAN+Style.BRIGHT+"\n\nYou have to repeat your achievement",repeat,"more times"+repeat_message)
	elif(repeat == 1):
		print(Fore.CYAN+Style.BRIGHT+"\n\nYou have to repeat your achievement",repeat,"more time"+repeat_message)
	else:
		print(Fore.CYAN+Style.BRIGHT+"\n\nYou just have to continue it for",repeat_days,"days more.")
	print(Fore.CYAN+Style.BRIGHT+"\nPress enter to exit!!")
	k=input()
	if k == 'p' or k == 'P':
		exist = path.exists('performed.txt')
		if not exist:
			done = open('performed.txt','w')
			done.write("True")
			done.close()
	return k

if __name__=="__main__":
    main()
