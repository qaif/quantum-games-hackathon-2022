=== MathTeacher ===
Math teacher Enrico Mwangi seems calculating. # narration
-> questioning
=questioning
*Alibi
   Where were you when the murder took place? # protagonist
   I was overseeing reexamination of previously failed students # mathT
   {werewolf==true:
   I thought I would engage them more if I made the vaccination question deal with something cool. # mathT
   Seems lycantropy is not a cool enough fiction to sell math interest. # mathT
   Well kiloid sellers are also going to miss out on the free advertising. # mathT
   ~ lucan_cure=true
   }
   {lucan_formula==true:
   Like polypinkiloid? # protagonist
   Yes, like polypinkiloid. # mathT
   }
    -> questioning
*Motive
   Did you get along with the victim well? # protagonist
   {guilty=="Math":
        Yes, we were close # mathT
   -else:
        Very closely # mathT
   }
   {affair==true:
       Atleast when they bothered to be around. # mathT
   -else:
       I have a hard time thinking of time without them. # mathT
   }
   {affair==false:
              {debt==true:
                  Sometimes, I felt like he kept a little too many secrets. # mathT
                  They never let me touch their key which they always kept on their belt. #mathT
              }
   }
   {guilty=="victim":
          At times he was very stuck in the past. Having so much regrets. # mathT
          Now he never gets to make up for them. # mathT
   }
   -> questioning
*Guilt
   Did you do it? # protagonist
   {werewolf:
        Not to my knowledge. # mathT
   }
   {guilty=="Math":
       Not in a million years. # mathT
   -else: 
      I would not off my friend. # mathT
   }
   -> questioning
+ Theorethics
   Would you care to try our new experiemental calculation machine? # mathT
   -> computing
+Leave
  -> Coffee.coffeetable
-
->questioning