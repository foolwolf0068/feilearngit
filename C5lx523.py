#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 11:02:33 2017

@author: foolwolf0068
"""

LoanAmount=eval(input("Loan Amount:"))
Time=eval(input("Number of Years:"))
#rate=eval(input("Annual Interest Rate:"))/1200
print("Interest Rate\t","Monthly Payment\t","Total Payment")
for rate in range(5000,8001,125): 
    rate/=1200000        
    monthlyPayment=LoanAmount*rate*(1+rate)**(Time*12)/((1+rate)**(Time*12)-1)
    print(format(rate*1200,".3f"),"%\t",round(monthlyPayment,4),"\t",round(monthlyPayment*12,4))
