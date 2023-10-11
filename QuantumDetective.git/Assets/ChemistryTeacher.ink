=== ChemistryTeacher ===
Chemistry teacher Deep Tamura seems jolty. # narration
-> questioning
=questioning
*Alibi
    Where were you when the murder took place? # protagonist
    {affair:
        Just mixing some of my chemicals. # chemistryT
    - else:
        Supervising my student study group. # chemistryT
    }
    {werewolf==true:
        Do tell me if in your investigation you find a purple potion. # chemistryT
        I think one of the students stole one from me. # chemistryT
        Marini suddenly asked for it, so its kind of urgent. # chemistryT
        ~ lucan_potion=true
    }
    -> questioning
*Motive
   Did you get along with the victim well? # protagonist
   {affair:
      He was a good colleague of mine. # chemistryT
   - else:
      They were well liked. # chemistryT
   }
   {guilty=="chemistry":
      I hope you will find the perpetrator. # chemistryT
   - else:
      I think everybody can say that. # chemistryT
   }
   -> questioning
*Guilt
   Did you do it? # protagonist
   {guilty=="chemistry":
       No. # chemistryT
   - else:
       Yes. He was too good for this earth. # chemistryT
   }
   -> questioning
*{bomb_smuggle==true}Mailbombs
   How come you use the mail office to deliver volative materials? # protagonist
   Oh its so expensive to use the armored cars all the time # chemistryT
   The accidents are so very rare # chemistryT
   The post office is very competent so I am sure they will know to handle them lightly # chemistryT
   What do you do in the event that there is an accident # protagonist
   For quick relief I have a secret comparment in the auditorium where I keep a phone to call for help quick # chemistryT
   I have to keep it secret and away from the students that they don't try to fiddle with the high techness of it all the time # chemistryT
   ~ sender_compartment=true
   ->questioning
+Leave
   -> Coffee.coffeetable
