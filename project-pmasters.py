# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 12:34:10 2020

@author: Paul
"""

import pandas as pd
import numpy as np
import tkinter.filedialog


record = None
AudNum = None
def clearnames():
    global names
    names = []

def namelist():
     global names
     print('\nAuditor names:')
     for i in names:
         print(i)
    
def recordlist():
    global names
    for j in names:
        print('\nRecords assigned to',j,':')
        aud2= df['Auditor'].tolist()
        aud3 = df['Employee_Name'].tolist()
        audited = dict(zip(aud3,aud2))
        for k in audited:
            if audited[k] is j:
                print(k)

def exportCSV ():
    global df
    export_file_path = tkinter.filedialog.asksaveasfilename(defaultextension='.csv')
    df.to_csv (export_file_path, index = False, header=True)

print('''Audit Group Program
      
1) Select employee record file
2) Enter auditor names
3) Assign records to auditors
4) View auditor names
5) View records assigned to auditors
6) Export list assignment to file
7) Quit menu, i.e., Quit
      
      
      ''')    

while True:
    try:
      selection = int(input('Enter command here: '))
      if selection == 1:
          record = pd.read_csv(tkinter.filedialog.askopenfile(mode='r'))
          print('File successfully opened')
          
      if selection == 2:
          while True:
              try:
                  clearnames()
                  AudNum = int(input('How many auditors will be conducting the audit? '))
              except:
                  print('That is not a valid entry, please enter an integer for this value')
              else: 
                  for x in range(AudNum):
                      print('Enter the name of Auditor', x+1,':')
                      nameentry = input()
                      names.append(nameentry)
                  print('\nAuditor names successfully recorded.')
                  namelist()
                  break
      if selection == 3:
            if record is None:
                print('Please select an employee record file before running this command')
            else:
                if AudNum is None:
                    print('Please enter auditor names before running this command')
                else:
                    while True:
                      try:
                          numrecords = int(input('How many records will be assigned to each auditor? '))
                      except:
                          print('That is not a valid entry, please enter an integer for this value')
                      else:
                          auditor = names*numrecords
                          newcols = record[['Employee_Name','Position','DOB','DateofHire','Department']] #Get columns we need
                          randomize = pd.DataFrame(np.random.permutation(newcols),columns=['Employee_Name','Position','DOB','DateofHire','Department']) #Randomize
                          df = randomize.loc[:(len(auditor)-1),['Employee_Name','Position','DOB','DateofHire','Department']] #Takes only the randomized values equal to names and input multiplied
                          df['Auditor']=auditor #add auditor column
                          df = df.sort_values(by='Auditor')
                          recordlist()
                          break
              
      if selection == 4:
          namelist()
      if selection == 5:
          recordlist()
      if selection == 6:
          exportCSV()
          print('File Saved')
      if selection == 7:
          print('Quitting now')
          break
      if selection not in range(1,8):
          print('''Please enter a number from 1 to 7.
                
Try again.''')
          
    except:
          print('Error, please enter a number from 1 to 7 and try again.')
          