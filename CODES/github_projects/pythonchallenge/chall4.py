import requests
import re

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

next_nothing = '8022'


while 1:
    thenga = requests.get(url+next_nothing)
    unda = re.findall('[0-9]+', thenga.text)[0]
    next_nothing = str(unda/2)          ## it was just unda before
    print(next_nothing)



    #######################Theres something wrong with this script