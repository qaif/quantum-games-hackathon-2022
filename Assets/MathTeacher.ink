=== MathTeacher ===
Math teacher Enrico Mwangi seems calculating.
-> questioning
=questioning
*Alibi
   "Where were you when the murder took place?"
   "I was overseeing reexamination of previously failed students"
    -> questioning
*Motive
   "Did you get along with the victim well?"
   {guilty=="Math":
        "Yes, we were close"
   -else:
        "Very closely"
   }
   {affair==true:
       Atleast when they bothered to be around.
   -else:
       I have a hard time thinking of time without them.
   }
   -> questioning
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
   -> questioning
+Leave
  -> Coffee.coffeetable

-