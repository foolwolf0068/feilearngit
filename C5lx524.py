#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 08:42:22 2017

@author: foolwolf0068
"""

LoanAmount=eval(input("Loan Amount:"))
Time=eval(input("Number of Years:"))
rate=eval(input("Annual Interest Rate:"))/1200
         
monthlyPayment=LoanAmount*rate*(1+rate)**(Time*12)/((1+rate)**(Time*12)-1)
print()
print("Monthly Payment:",format(monthlyPayment,".3f"))
print("Total Payment:",format(monthlyPayment*Time*12,".3f"))
print()
print("Payment#\t","Interest\t","Principal\t","Balance")

balance=LoanAmount
for i in range(1,Time*12+1):
    Interest=rate*balance
    Principle=monthlyPayment-Interest
    balance-=Principle
    print(i,"\t",format(Interest,".3f"),"\t",format(Principle,".3f"),"\t",format(balance,".3f"))

