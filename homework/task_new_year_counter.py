from datetime import datetime

def counter():
	today = datetime.today()
	next_year = datetime(today.year + 1, 1, 1, hour=0, minute=0, second=0)
	new_year = next_year - today
	
	days = new_year.days
	hours = new_year.seconds // 60 // 60
	minutes = 60 - ((1440 - new_year.seconds // 60) % 60)
	if minutes == 60:
		minutes = 0
	
	 
	dtext = 'дней'
	if days % 10 == 1 and days != 11:
  			dtext = 'день' 
	if len(str(days)) == 1:
		if 1 < days % 10 < 5:
			dtext = 'дня'
	if days % 10 == 1 and days != 11:
  		dtext = 'день'
	if len(str(days)) >= 2 and str(days)[-2] != '1':
		if 1 < int(days) % 10 < 5:
			dtext = 'дня'
	
	
	
	htext = 'часов'
	if hours == 1:
		htext = 'час'
	if hours % 10 == 1 and hours != 11:
  			htext = 'час' 
	if len(str(hours)) == 1:
		if 1 < hours % 10 < 5:
			htext = 'часа'
	if hours % 10 == 1 and hours != 11:
  		htext = 'час'
	if len(str(hours)) >= 2 and str(hours)[-2] != '1':
		if 1 < int(hours) % 10 < 5:
			htext = 'часа'

		

	mtext = 'минут'
	if minutes % 10 == 1 and minutes != 11:
  			mtext = 'минута' 
	if len(str(minutes)) == 1:
		if 1 < minutes % 10 < 5:
			mtext = 'минуты'
	if len(str(minutes)) >= 2 and str(minutes)[-2] != '1':
		if 1 < int(minutes) % 10 < 5:
			mtext = 'минуты'
	if minutes % 10 == 1 and minutes != 11:
  		mtext = 'минута'

		
	return f'{days} {dtext} {hours} {htext} {minutes} {mtext}'