                     #HELLO GUYS THIS IS A PYTHON CODE OF "DNA SEQUENCING" BY KMP ALGORITHMIC SEARCH WHICH I HAD DONE BY USING BASIC KMP ALGORITHMIC SEARCH CODE....
                     
     #HERE IS THE CODE IN PYTHON FOR THE SEQUENCES OF 4 < LENGTH < = 10
     
def DNASearch(pat, txt):             #HERE THE MAIN SEARCH STARTS
  pat = pat.upper()                  #CONVERTING THE PATTERNS WHICH WE MADE BY DIVIDING THE SEQUENCE INTO PARTS INTO UPPER CASE
  txt = txt.upper()                  #CONVERTING THE OTHER SEQUENCE INTO UPPER CASE  
  M = len(pat)                       #CALCULATING THE LENGTH OF PATTERN
  N = len(txt)                       #CALCULATING THE LENGTH OF TXT
  lps = [0]*M                        #SIZE OF LEAST-PREFIX-SUFFIX TABLE(lps) OR PI TABLE
  j = 0                              #POINTER VARIABLE FOR POINTING INDEXES OF ELEMENTS OF lps TABLE
  computeLPSArray(pat, M, lps)       #HERE WE ARE CALLING THE lps TABLE ARRAY METHOD
  i = 0                              #POINTER VARIABLE FOR POINTING INDEXES OF ELEMENTS OF THE SEQUENCE 
  while i < N:                       #AS 'i' SHOULD BE LESS THAN THE LENGTH OF N(which is the size of the sequence)
    if txt[i] == pat[j]:             #IF WE FOUND A MATCH THEN ACCORDING TO KMP WE SHOULD INCREMENT BOTH i & j
      i += 1
      j += 1
    else:
        if j != 0:                  #ACCORDING TO KMP WE ARE SHIFTING j TO THE POSTION BEFORE OF THE INDEX WE GOT IN lps TABLE 
            j = lps[j-1]
        else:
            i += 1
    if j == M:                      #NOW WE GOT THE MATCHED PATTERN 
      print("THE GIVEN DNA SEQUENCES MATCHED :) :) :)")
      j = lps[j-1]

def computeLPSArray(pat, M, lps):    #HERE WE ARE IMPLEMETING THE LOGICAL PART OF lps TABLE(WHICH WE GENERALLY DO ON PAPER)
    len = 0
    lps[0]
    i = 1
    while i < M:
        if pat[i]== pat[len]:
            lps[i] = len + 1
            len += 1
            i += 1
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i] = 0
                i += 1


print('          WELCOME TO DNA SEQUENCING      ')
from time import sleep                                  #FOR BETTER ATTRACTION OF OUR OUTPUT WE ARE USING THIS
sleep(1)
print('<<<<<<<<GET READY TO ENTER THE MAIN FLOW>>>>>>>>>>')
sleep(1)
print('ENTER THE FIRST DNA SEQUENCE')
str1 = input()
print('ENTER THE SECOND DNA SEQUENCE')
str2 = input()
txt = str1                                              #ITS OUR WISH.....HERE IAM TAKING FIRST SEQUENCE AS txt
pat1 = str2[0:4]                                        #DIVIDING THE LEFT OVER SEQUENCE INTO 4 EQUAL PARTS AND TAKING THOSE PARTS AS PATTERNS
pat2 = str2[1:5]
pat3 = str2[2:6]
pat4 = str2[3:7]
pat5 = str2[4:8]
pat6 = str2[5:9]
pat7 = str2[6:10]
pat = pat1
lst = [pat]                                             
if len(str1) == len(str2) and pat==pat1 or pat==pat2 or pat==pat3 or pat==pat4 or pat==pat5 or pat==pat6 or pat==pat7:       #CHECKING THE PATTERNS 
  DNASearch(pat2,txt)                                   
  pass
  DNASearch(pat3,txt)                                  #USING OUR ABOVE DNASearch METHOD OF KMP FOR SEQUENCE MATCH
  pass
  DNASearch(pat4,txt)
  pass
  DNASearch(pat5,txt)
  pass
  DNASearch(pat6, txt)
  pass
  DNASearch(pat7, txt)
else:
    print("SOME ERROR IN THE GIVEN SEQUENCES OR THEY ARE MIS-MATCHING")    #IF DNA SEQUENCES ARE NOT OF SAME LENGTH OR IF NOO PATTERNS FOUND THEN THIS IS PRINTED..
    
    
 OUTPUT :
 
   #WHEN  DNA SEQUENCES ARE MATCHING
                   WELCOME TO DNA SEQUENCING      
<<<<<<<<GET READY TO ENTER THE MAIN FLOW>>>>>>>>>>
ENTER THE FIRST DNA SEQUENCE
ACTGAGCATC
ENTER THE SECOND DNA SEQUENCE
CGTAACTGCT
THE GIVEN DNA SEQUENCES MATCHED :) :) :)

   #WHEN DNA SEQUENCES ARE MIS-MATCHING
          WELCOME TO DNA SEQUENCING      
<<<<<<<<GET READY TO ENTER THE MAIN FLOW>>>>>>>>>>
ENTER THE FIRST DNA SEQUENCE
AGCTGACTAG
ENTER THE SECOND DNA SEQUENCE
GATCAGTC
SOME ERROR IN THE GIVEN SEQUENCES OR THEY ARE MIS-MATCHING
                                                                             #THANK Q  
   
