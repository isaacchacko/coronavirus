from soupRequests import RequestBot
import append
import datetime
import time
import threading
def clean(text):
	text = text.replace(',','')
	text = text.strip()
	try:
		text = int(text)
	except:
		pass
	return text
class Country(object):
	def __init__(self, url, title):
		self.page = RequestBot(url)
		self.soup = self.page.soup
		self.title = title
		self.main()
	def main(self):
		self.total_cases = clean(self.soup.find('span', style = 'color:#aaa').text)

		self.total_infected = self.soup.findAll('div', class_ = 'number-table-main')
		if len(self.total_infected) == 2:
			self.finished_cases = clean(self.total_infected[1].text)
			self.total_infected = clean(self.total_infected[0].text)
			self.weird = False
		else:
			self.weird = True
			self.finished_cases = clean(self.total_infected[0].text)
			self.total_infected = ''

		self.mild_condition = self.soup.findAll('span', class_ = 'number-table')
		if len(self.mild_condition) == 4:	
			self.serious_condition = clean(self.mild_condition[1].text)
			self.discharged = clean(self.mild_condition[2].text)
			self.total_dead = clean(self.mild_condition[3].text)
			self.mild_condition = clean(self.mild_condition[0].text)
		else:
			self.discharged = clean(self.mild_condition[0].text)
			self.total_dead = clean(self.mild_condition[1].text)
			self.serious_condition, self.mild_condition = '', ''


		divisor = float(self.total_cases) / 100.0
		self.death_rate = float(self.total_dead) / divisor 
		self.death_rate = self.death_rate * 0.01
		fmt = '%m/%d/%y %I:%M %p'
		self.time = time.strftime(fmt)
		if self.weird:
			x = threading.Thread(target = append.appendToXL, args = [['Time','Total Infected (All Time)', 'Total Finished Cases','Total Deaths','Total Discharges', 'Death Rate'],
				[self.time,
				self.total_cases,
				self.finished_cases,
				self.total_dead,
				self.discharged,
				self.death_rate],
				'coronavirus_statistics.xlsx', 
				self.title])
			x.start()
			x.join()
		else:
			x = threading.Thread(target = append.appendToXL, args = [['Time','Total Infected (All Time)', 'Total Finished Cases','Total Deaths','Total Discharges','Total Active Cases','Total Mild Condition','Total Serious Condition', 'Death Rate'],
				[self.time,
				self.total_cases,
				self.finished_cases,
				self.total_dead,
				self.discharged,
				self.total_infected,
				self.mild_condition,
				self.serious_condition,
				self.death_rate],
				'coronavirus_statistics.xlsx', 
				self.title])
			x.start()
			x.join()
def main():
	world = Country('https://www.worldometers.info/coronavirus/#countries','World')
	usa = Country('https://www.worldometers.info/coronavirus/country/us/','USA')
	spain = Country('https://www.worldometers.info/coronavirus/country/spain/','Spain')
	italy = Country('https://www.worldometers.info/coronavirus/country/italy/','Italy')
	france = Country('https://www.worldometers.info/coronavirus/country/france/','France')
	# uk = Country('https://www.worldometers.info/coronavirus/country/uk/','UK')
	germany = Country('https://www.worldometers.info/coronavirus/country/germany/','Germany')
	# turkey = Country('https://www.worldometers.info/coronavirus/country/turkey/','Turkey')
	# russia = Country('https://www.worldometers.info/coronavirus/country/russia/','Russia')
	iran = Country('https://www.worldometers.info/coronavirus/country/iran/','Iran')
if __name__ == '__main__':
	main()