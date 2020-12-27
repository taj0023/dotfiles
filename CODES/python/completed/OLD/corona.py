#!/usr/bin/env python3
import requests
import json
import sys
from datetime import date, timedelta

RED = '\033[91m'
GREEN = '\033[92m'
UNDERLINE = '\033[4m'
END = '\033[0m'
today = date.today()
yesterday = today - timedelta(days = 1)


if len(sys.argv) == 1:
	print('Usage: "corona <kozhikode/kerala/india>"')
	quit()


def main():




	# INDIA STAT
	indian_url = 'https://api.covid19india.org/data.json'
	indianjs = json.loads(requests.get(indian_url).text)
	india_confirmed, india_deaths, india_recoveRED, india_date, tindia_confirmed, tindia_deaths, tindia_recoveRED = indianjs['cases_time_series'][-1].values()

	js = json.loads(requests.get(url).text)

	#KERALA STAT
	kerala_confirmed, kerala_deaths, kerala_recoveRED, kerala_tested = js['KL']['delta'].values()
	tkerala_confirmed, tkerala_deaths, other, tkerala_recoveRED, kerala_tested = js['KL']['total'].values()


	# KOZHIKODE STAT
	tkozhi_confirmed, tkozhi_death, other, tkozhi_recoveRED, tkozhi_tested= js['KL']['districts']['Kozhikode']['total'].values()
	kozhi_confirmed, kozhi_recoveRED, *kozhi_tested = js['KL']['districts']['Kozhikode']['delta'].values()
	
	kozhi_string = f'''
				   {UNDERLINE}{GREEN}KOZHIKODE COVID STATISTICS{END}
	 	┌───────────────────────────────────────────────────────────────┐
	 	│		CONFIRMED: {tkozhi_confirmed}{RED}({kozhi_confirmed}){END}				│
	 	│		DEATHS   : {tkozhi_death}					│
	 	│		RECOVERED: {tkozhi_recoveRED}{RED}({kozhi_recoveRED}){END}				│
	 	└───────────────────────────────────────────────────────────────┘
	'''

	kerala_string =f'''
				   {UNDERLINE}{GREEN}KERALA COVID STATISTICS{END}
	 	┌───────────────────────────────────────────────────────────────┐
	 	│		CONFIRMED: {tkerala_confirmed}{RED}({kerala_confirmed}){END}			│
	 	│		DEATHS   : {tkerala_deaths}{RED}({kerala_deaths}){END}				│
	 	│		RECOVERED: {tkerala_recoveRED}{RED}({kerala_recoveRED}){END}				│
	 	└───────────────────────────────────────────────────────────────┘
	'''


	india_string = f'''
				   {UNDERLINE}{GREEN}INDIAN COVID STATISTICS{END}
	 	┌───────────────────────────────────────────────────────────────┐
	 	│		CONFIRMED: {tindia_confirmed}{RED}({india_confirmed}){END}			│
	 	│		DEATHS   : {tindia_deaths}{RED}({india_deaths}){END}				│
	 	│		RECOVERED: {tindia_recoveRED}{RED}({india_recoveRED}){END}			│
	 	└───────────────────────────────────────────────────────────────┘
	'''



	if sys.argv[1] == 'india':
		print(india_string)
	elif sys.argv[1] == 'kerala':
		print(kerala_string)
	elif sys.argv[1] == 'kozhikode':
		print(kozhi_string)




if __name__ == '__main__':
	try:
		url = 'https://api.covid19india.org/v4/data-' + str(today) + '.json'
		main()
		print("					"+str(today))
	except json.decoder.JSONDecodeError:
		url = 'https://api.covid19india.org/v4/data-' + str(yesterday) + '.json'
		main()
		print("					"+str(yesterday))