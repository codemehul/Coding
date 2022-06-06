#This is the code to find the location, carrier and the timezone of the inputed phone number
#The module used in this python program is "phonenumbers"
#Installation of the module :- "pip install phonenumbers"

import phonenumbers
from phonenumbers import geocoder,carrier,timezone

a = str(input("Tell us the country code:- "))
b = str(input("Tell us the number:- "))

phoneNumber = phonenumbers.parse(f"+{a+b}")
possible = phonenumbers.is_possible_number(phoneNumber)
valid = phonenumbers.is_valid_number(phoneNumber)

if possible == True:
    if valid == True:
        i = geocoder.description_for_number(phoneNumber,"en")
        j = carrier.name_for_number(phoneNumber, "en")
        k = timezone.time_zones_for_number(phoneNumber)
        print(phoneNumber)
        print(f"The inputed number location is:- {i}\nThe inputed number carrier is:- {j}\nThe inputed number timezone is:- {k}")
    else:
        print("The number you have input is possible but not valid, Please execute once again")
else:
        print("You have inputed the wrong number, Please execute once again with correct number")
