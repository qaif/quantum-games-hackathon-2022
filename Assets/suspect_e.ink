==SuspectE==
Math teacher Enrico Mwangi seems calculating.
*Alibi
   "Where were you when the murder took place?"
   "I was overseeing reexamination of previously failed students"
*Motive
   "Did you get along with the victim well?"
   {guilty=="Math":
        "Yes, we were close"
   -else:
        Very closely"
   }
*Guilt
   "Did you do it?"
   {werewolf:
        "Not to my knowledge."
   }
   {guilty=="Math":
       "Not in a million years."
   -else: 
      "I would not off my friend."
   }

-> Coffee
