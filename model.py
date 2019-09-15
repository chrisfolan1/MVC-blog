# 
# File:			model.py
# Description:	MVC Person example - Model module
# Author:		Chris Folan
#		  __                            ___       ___                       
#		 /\ \             __          /'___\     /\_ \                      
#	  ___\ \ \___   _ __ /\_\    ____/\ \__/  ___\//\ \      __      ___    
#	 /'___\ \  _ `\/\`'__\/\ \  /',__\ \ ,__\/ __`\\ \ \   /'__`\  /' _ `\  
#	/\ \__/\ \ \ \ \ \ \/ \ \ \/\__, `\ \ \_/\ \L\ \\_\ \_/\ \L\.\_/\ \/\ \ 
#	\ \____\\ \_\ \_\ \_\  \ \_\/\____/\ \_\\ \____//\____\ \__/.\_\ \_\ \_\
#	 \/____/ \/_/\/_/\/_/   \/_/\/___/  \/_/ \/___/ \/____/\/__/\/_/\/_/\/_/
#              


import json

PERSON_DB = "person_db.txt"

class Person(object):

    def __init__(self, first_name = None, last_name = None):
		# Person constructor
        self.first_name = first_name	# fred
        self.last_name  = last_name		# flintstone

    def name(self):
		# returns full name - eg. wilma flintstone
        return ("%s %s" % (self.first_name,self.last_name))

    @classmethod
    #returns all people inside the person db as list of Person objects
    def getAll(self):
        with open(PERSON_DB, 'r', encoding='utf-8') as database:
            data = json.loads(database.read())
        # print(data)
        result = []
        for name in data['names']:
            # print(name.items())
            person = Person(name['first_name'], name['last_name'])
            result.append(person)
        return result

