import random

#this script reads a SPS J/psi+ J/psi LHE and a SPS ccbar LHE and give in output a DPS LHEF

file1 = open('sampleggpsi1psi1.lhe', 'r') 
file2 = open('sampleggccbar.lhe', 'r') 

Lines = file1.readlines() 
Lines_Double = file2.readlines() 
stringx='nan'
global_line_number = 0
global_line_number_triple = 0
muon_1 = stringx
muon_2 = stringx
amuon_1 = stringx
amuon_2 = stringx


# Strips the newline character 
for line2 in Lines_Double:
  adouble = line2.strip()
  if (line2.strip().find("<rwgt>") != 0): 
    if (line2.strip().find("4    81") == 0):
      new_line = adouble.replace("4    81", "12    81")
      print new_line     
    else:
      if (line2.strip().find("<wgt ") != 0) and (line2.strip().find("</rwgt>") != 0): 
       print adouble
      
 
  if (line2.strip().find("<rwgt>") == 0):

    notfoundjpsi = True
    notfoundmuon = True
    notfoundantimuon = True

    notfoundjpsi2 = True
    notfoundmuon2 = True
    notfoundantimuon2 = True
    jpsi_counter=0
    loop=0
    gluon = 1

    local_line_number = 0
    local_line_triple_number = 0
   
    for line in Lines: 
      local_line_number += 1
      if (local_line_number > global_line_number or local_line_number == global_line_number) and (notfoundjpsi or notfoundmuon or notfoundantimuon):
        global_line_number += 1
        a = line.strip()
        
       #looking for J/psi

        if (line.strip().find("443") == 0):
          jpsi_counter += 1
          new_line = a.replace(" 1    2 ", " 5    6 ")
          #notfoundjpsi = False
          print new_line
       
          #notfoundjpsi = False
       
       #looking for gluons

        elif (line.strip().find("21") == 0): 
         if (gluon == 1):
           gluon = 2
           new_line = a.replace("102  101", "105  104")
           print new_line
         elif (gluon == 2):
           gluon = 3
           new_line2 = a.replace("101  102", "104  105")
           print new_line2
           notfoundjpsi = False
             
        #looking for muons

        if (line.strip().find("-13    1    3    0") ==0 ):
           new_line = a.replace(" 3 ", " 7 ")
           muon_1 = new_line
           #notfoundantimuon = False
        elif (line.strip().find("-13    1    4    0") == 0):  
           new_line = a.replace("4    0", "8    0")
           muon_2 = new_line
           notfoundantimuon = False
        elif (line.strip().find("13    1    3    0") ==0 ):
           new_line = a.replace(" 3 ", " 7 ")
           amuon_1 = new_line
           #notfoundmuon = False
        elif (line.strip().find("13    1    4    0") ==0 ) and not notfoundjpsi:
           new_line = a.replace(" 4 ", " 8 ")
           amuon_2 = new_line
           notfoundmuon = False
           print muon_1
           print amuon_1   
           print muon_2
           print amuon_2
      
   

