import random

#this script reads a SPS J/psi + ccbar LHE and a SPS J/psi LHE and give in output a DPS LHEF


file2 = open('sampleggpsi1ccbar1.lhe', 'r') 
file1 = open('sample_pp_psiX_crystalball.lhe', 'r') 

Lines = file1.readlines() 
Lines_Double = file2.readlines() 
stringx='nan'
global_line_number = 0
global_line_number_triple = 0
muon_1 = stringx
muon_2 = stringx

# Strips the newline character 
for line2 in Lines_Double:
  adouble = line2.strip()

  if (line2.strip().find("<rwgt>") != 0): 
    if (line2.strip().find("7    81") == 0):
      mother_id = 7
      mother_id_triple = 10
      new_line = adouble.replace("7    81", "13    81")
      if (line2.strip().find("13    1    3") != 0) or (line2.strip().find("-13    1    3") != 0):
       #print("sono passato")
       print new_line     
    else:
      if ((line2.strip().find("13    1    3") != 0) and (line2.strip().find("-13    1    3") != 0)) and (line2.strip().find("<wgt ") != 0) and (line2.strip().find("</rwgt>") != 0):
       #print("sono passato")
       
       print adouble
      if (line2.strip().find("13    1    3") == 0):
        muon_1 = adouble
      if (line2.strip().find("-13    1    3") == 0):
        muon_2 = line2.strip()
 
  if (line2.strip().find("<rwgt>") == 0):

    notfoundjpsi = True
    notfoundmuon = True
    notfoundantimuon = True

    notfoundjpsitriple = True
    notfoundmuontriple = True
    notfoundantimuontriple = True
    gluon = 1
    local_line_number = 0
    local_line_triple_number = 0
    for line in Lines: 
      local_line_number += 1
      if (local_line_number > global_line_number or local_line_number == global_line_number) and (notfoundjpsi or notfoundmuon or notfoundantimuon):
        global_line_number += 1
        a = line.strip()
        if (line.strip().find("443") == 0):
          new_line = a.replace(" 1    2 ", " 6    7 ")
          print new_line
          notfoundjpsi = False
        if (line.strip().find("21") == 0): 
         if (gluon == 1):
           gluon = 2
           new_line = a.replace("101  103", "105  107")
           print new_line
         elif (gluon == 2):
           gluon = 3
           new_line2 = a.replace("103  102", "107  106")
           print new_line2
         elif (gluon == 3):
           new_line = a.replace(" 1    2  101  102", " 6    7  105  106")
           print new_line
          
        if (line.strip().find("-13") == 0 and not notfoundjpsi):
          stuff_in_string = " {} ".format(mother_id)
          new_line = a.replace(" 3 ", " 8 ")
          print new_line
          notfoundantimuon = False
        if (line.strip().find("13") == 0 and not notfoundjpsi and not notfoundantimuon):
          stuff_in_string = " {} ".format(mother_id)
          new_line = a.replace(" 3 ", " 8 ")
          print new_line
          notfoundmuon = False
          print muon_1
          print muon_2
       
  


