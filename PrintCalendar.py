#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 15:38:17 2017

@author: foolwolf0068
"""

def printMonth(year,month):
    #print(year,month)
    printMonthTitle(year,month)
    printMonthBody(year,month)
    
def printMonthTitle(year,month):
    #print("printMonthTitle")
    print("   ",getMonthName(month),"   ",year)
    print("-----------------------------")
    print(" Sun Mon Tus Wed Thu Fri Sat ")
def printMonthBody(year,month):
    #print("getMonthBody")
    startDay=getStartDay(year,month)
    numberOfDaysInMonth=getNumberOfDaysInMonth(year,month)
    i=0
    for i in range(0,startDay):
        print("   ",end=" ")
    for i in range(1,numberOfDaysInMonth+1):
        print(format(i,"4d"),end="")
        if (i +startDay)%7==0:
            print()

def getMonthName(month):
    monthvalue=["January","February","March","April","May","June","July",
                "August","September","October","November","December"]
    for i,value in enumerate(monthvalue,start=1):
        if i==month:
            return value
        
def getStartDay(year,month):
    #print("getStartDay")
    StartDayforJan1_1800=3
    totalNumberOfDays=getTotalNumberOfDays(year,month)
    return (StartDayforJan1_1800+totalNumberOfDays)%7

def getTotalNumberOfDays(year,month):
    #print("getTotalNumberOfDays")
    sum=0
    for i in range(1800,year):
        if isLeapYear(i):
            sum+=366
        else:
            sum+=365
    for i in range(1,month):
        sum+=getNumberOfDaysInMonth(year,i)
    return sum
def getNumberOfDaysInMonth(year,month):
    #print("getNumberOfDaysInMonth")
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif month==2:
        return 29 if isLeapYear(year) else 28
    else:
        print("Please Check your input,the Month must be between 1 and 12!!!")
        return 0

def isLeapYear(year):
    #print("isLeapYear")
    return year%400==0 or(year%4==0 and year % 100!=0)
    
    
def main():
    year=eval(input("Enter full year(e.g., 2001): "))
    month=eval(input("Enter month as number between 1 and 12: "))
    printMonth(year,month)
    print()
    
main()