# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 16:48:18 2022

@author: owner
"""
#do imports
import requests

#Coding Exercise 10: Web scrapping exercise
#Rules of this Project :
#Extracting/Downloading the data from html page.
#Extracting a particular content in the webpage.
#Location of information of interest in the html page. Identify the common pattern.
#Give instructions to the extractor which class is title column
#Search by Tag and Tag by class.
#Search the text file with beautiful soup object.

#Problem Statement :

#Count the total number of views for a given video in youtube for a given keyword.
#Keyword :python

#create variables
page = ""
key = ""

#functions
#main function to run.
def main():
        #request the user to get the url and key
        page, key = request()
        
        #connect webpage
        try:
            webPage = requests.get(page)
        except:
            print("Error occurred connecting the the webpage. Please try again.")
            main()
            exit(0)
            
        #get data from webPage
        views = getData(webPage)
        
        #print answer
        print("There are {} views on your youtube video.".format(views))

#get user's request
def request():
    #get url for page.
    page = input("Please enter in the youtube URL you want to know how many views it has: ")

    #get keywork
    key = input("Please enter in the correct keyword: ")
    
    
    ##for testing purposes auto make key and page correct pages.
    page = "https://www.youtube.com/watch?v=kTj8-_Xkt1A"
    key = "python"
    
    
    #force valid input.
    while int(page.find("youtube")) == -1:
            page = input("You did not enter in a valid youtube URL. Please try again: ")
            
    while key !="python":
        key = input("You did not enter in the correct key. Please try again: ")


    return page, key

#get the data from the webPage
def getData(webPage):
    Data = webPage.content
    Data = str(Data)
    Data = Data[Data.find('primary-info'):]
    Data = Data[Data.find('"viewCount":{"simpleText":"'):]
    Data = Data.split(" views")[0]
    Data = Data.split('"')
    Data = Data[-1]
    
    return Data


#run the program
main()