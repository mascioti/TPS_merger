
# install pylhe library before use (https://github.com/scikit-hep/pylhe)
# this script is meant to read and merge two single SPS J/Psi LHEF and an SPS D* LHEF after being hadronized in Pythia

import pylhe
import copy

file1 = open('ccbar_h.lhe', 'r') 


Lines = file1.readlines() 
nf = open("ccbar_h_m.lhe", "w")


# Strips the last line 
 
for line in Lines:
  adouble = line.strip()

  if (line.strip().find("#pdf") != 0): 
    nf.write(adouble)
    nf.write("\n")  
  else:
    continue
nf.close()


f1=pylhe.readLHE("ccbar_h_m.lhe")
f2=pylhe.readLHE("sample_pp_psiX_crystalball.lhe")
f3=pylhe.readLHE("sample_pp_psiX_crystalball.lhe")

f2_in=pylhe.readLHEInit("sample_pp_psiX_crystalball.lhe")

I_1=[]
I_2=[]
I_3=[]
P_1=[]
P_2=[]
P_3=[]
a=[]
a_2=[]
for e in f1:
 I_1 += [e.eventinfo]
 P_1 += [e.particles]

for e in f2:
 I_2 += [e.eventinfo]
 P_2 += [e.particles]

for e in f3:
 I_3 += [e.eventinfo]
 P_3 += [e.particles]


n=min(len(P_1),len(P_2),len(P_3))

P_1=P_1[:n]
P_2=P_2[:n]
I_1=I_1[:n]
I_2=I_2[:n]
P_3=P_3[:n]
I_3=I_3[:n]

P=[]
I=[]

for i in range(n):
 P += [P_1[i] + P_2[i]+P_3[i]]
 a=I_2[i]
 N=I_1[i].nparticles+I_2[i].nparticles+I_3[i].nparticles
 a.nparticles=N
 I +=[a]


ftot_in=f2_in

#Writing the LHEF

#fieldnames = ["beamA","beamB","energyA","energyB","PDFgroupA","PDFgroupB","PDFsetA","PDFsetB","weightingStrategy","numProcesses",]
#fieldnames = ["nparticles", "pid", "weight", "scale", "aqed", "aqcd"]

print "<LesHouchesEvents version=\"1.0\">"
print "<init>"
print "  ", int(ftot_in["initInfo"]["beamA"]), int(ftot_in["initInfo"]["beamB"]), int(ftot_in["initInfo"]["energyA"]), int(ftot_in["initInfo"]["energyB"]), int(ftot_in["initInfo"]["PDFgroupA"]), int(ftot_in["initInfo"]["PDFgroupB"]), int(ftot_in["initInfo"]["PDFsetA"]), int(ftot_in["initInfo"]["PDFsetB"]), int(ftot_in["initInfo"]["weightingStrategy"]), int(ftot_in["initInfo"]["numProcesses"])
print "  ", ftot_in["procInfo"][0]["xSection"], ftot_in["procInfo"][0]["error"], int(ftot_in["procInfo"][0]["unitWeight"]), int(ftot_in["procInfo"][0]["procId"])
print "</init>"

for i in range(n):
 x=0
 k_2=0
 print "<event>"
 print " ", int(I[i].nparticles), int(I[i].pid), I[i].weight, I[i].scale, I[i].aqed, I[i].aqcd
 m=int(I[i].nparticles)
 for j in range(m):
  k=int(I_1[i].nparticles+6)
  k_2=int(I_1[i].nparticles) 
  x += 1
  if ((x > k and x < k_2) and not (P[i][j].color1 == 0 or P[i][j].color2 ==0)):
   print k_2
   print " ", int(P[i][j].id), int(P[i][j].status), int(P[i][j].mother1), int(P[i][j].mother2), int(P[i][j].color1+200), int(P[i][j].color2+200), P[i][j].px, P[i][j].py, P[i][j].pz, P[i][j].e, P[i][j].m, P[i][j].lifetime, P[i][j].spin
  elif (x > k_2 and not (P[i][j].color1 == 0 or P[i][j].color2 ==0)):
   print " ", int(P[i][j].id), int(P[i][j].status), int(P[i][j].mother1), int(P[i][j].mother2), int(P[i][j].color1+300), int(P[i][j].color2+300), P[i][j].px, P[i][j].py, P[i][j].pz, P[i][j].e, P[i][j].m, P[i][j].lifetime, P[i][j].spin
  else:
    print " ", int(P[i][j].id), int(P[i][j].status), int(P[i][j].mother1), int(P[i][j].mother2), int(P[i][j].color1), int(P[i][j].color2), P[i][j].px, P[i][j].py, P[i][j].pz, P[i][j].e, P[i][j].m, P[i][j].lifetime, P[i][j].spin
 print "</event>"
print "</LesHouchesEvents>"



#  fieldnames = ["nparticles", "pid", "weight", "scale", "aqed", "aqcd"]
#fieldnames = ["id","status","mother1","mother2","color1","color2","px","py","pz","e","m","lifetime","spin",]
