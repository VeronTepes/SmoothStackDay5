# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 16:04:55 2022

@author: Tanner Law
"""
#imports

import sys
import logging
from openpyxl import load_workbook


#global vars
wb = ""


#functions
def main():
    #create logger
    myLog = logger()
    
    try:
        #if they don't pass in what they want assume this file
        if(len(sys.argv)<2):
            workbook = load_workbook('expedia_report_monthly_march_2018.xlsx')
            wb = 'expedia_report_monthly_march_2018.xlsx'
            #otherwise take what was passed in.
        else:
            workbook = load_workbook(sys.argv[1])
            wb = sys.argv[1]
    except:
        myLog.error("Could not open workbook.")
    
    workbook.move_sheet("Summary Rolling MoM")
    sheet = workbook.active
    
    getData(wantedRow(myLog, wb, sheet), sheet, myLog)

    
    
#create logger
def logger():
    #Creating and Configuring Logger

    Log_Format = "%(asctime)s - %(message)s"

    logging.basicConfig(filename = "logfile.log",
                    filemode = "w",
                    format = Log_Format, 
                    level = logging.ERROR)

    logger = logging.getLogger()
    #logger.error("Our First Log Message")
    
    return logger

#find what row I want
def wantedRow(myLog, wb, sheet):
    #get the month and year to loop through on the file
    wb = wb.split('.')[0]
    month = wb.split('_')[-2]
    year = wb.split('_')[-1]
    year = year[2] + year[3]
    #print(year)
    #print(month)
    #print(rowWanted)
    #print(monthNum(month))
    
    #find the row containing the str I gor for rowWanted
    myLog.error("getting row num I need")
    

    for x in range(2, 50):
        #print(sheet.cell(row=x, column=1).value)
        val = str(sheet.cell(row=x, column=1).value)
        val = val.split(" ")[0]
        if(val.split("-")[-1] == year and int(val.split("-")[-2]) == monthNum(month)):
            return x

#get my data from a given row    
def getData(row,sheet, myLog):
    myLog.error("Getting Data")
    
    valuesDict = ("Calls Offered", "Abandoned after 30s", "FCR", "DSAT", "CSAT")
    values = []
    
    for i in range(2, 7):
        values.append(sheet.cell(row = row, column = i).value)
        
    myLog.error("Data for {}: \n".format(str(sheet.cell(row=row, column = 1).value).split(" ")[0]))
        
    for i in range(0, len(valuesDict)):
        if i == 0:
            
            myLog.error("{}: {} ".format(valuesDict[i], values[i]))
        else:
            myLog.error("{} : {} : {}%".format(valuesDict[i], values[i], (values[i]*100)))
    
#get month num
def monthNum(str):
    if str == 'january':
        return 1
    elif str == 'february':
        return 2
    elif str == 'march':
        return 3
    elif str == 'april':
        return 4
    elif str == 'may':
        return 5
    elif str == 'june':
        return 6
    elif str == 'july':
        return 7
    elif str == 'august':
        return 8
    elif str == 'september':
        return 9
    elif str == 'october':
        return 10
    elif str == 'november':
        return 11
    else:
        return 12

#start the program by calling the main function
main()