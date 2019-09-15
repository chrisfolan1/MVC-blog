#
# File:			view.py
# Description:	MVC Person example - view module
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


def showAllView(list):
    print ("There are {} uesrs in our database".format(len(list)))
    for item in list:
        print ( item.name() )

def startView():
    print ("MVC - Simple Person example")
    print ("Do you want to see everyone in my db?[y/n]")

def endView():
    print ( "\nThe Show's over...")    

