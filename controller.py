#
# File:			controller.py
# Description:	MVC Person example - controller module
# Author:		Chris Folan
#		  __                            ___       ___                       
#		 /\ \             __          /'___\     /\_ \                      
#	  ___\ \ \___   _ __ /\_\    ____/\ \__/  ___\//\ \      __      ___    
#	 /'___\ \  _ `\/\`'__\/\ \  /',__\ \ ,__\/ __`\\ \ \   /'__`\  /' _ `\  
#	/\ \__/\ \ \ \ \ \ \/ \ \ \/\__, `\ \ \_/\ \L\ \\_\ \_/\ \L\.\_/\ \/\ \ 
#	\ \____\\ \_\ \_\ \_\  \ \_\/\____/\ \_\\ \____//\____\ \__/.\_\ \_\ \_\
#	 \/____/ \/_/\/_/\/_/   \/_/\/___/  \/_/ \/___/ \/____/\/__/\/_/\/_/\/_/
#


from model import Person
import view

def showAll():
    #gets all Person objects
    people_in_db = Person.getAll()
    #calls view
    return view.showAllView(people_in_db)

def start():
	# crude menu...
    view.startView()
    inp = input()
    if inp == 'y':
        return showAll()
    else:
        return view.endView()

if __name__ == "__main__":
    #running controller function
    start()
    view.endView()