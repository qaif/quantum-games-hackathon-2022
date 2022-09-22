=== MathTeacher ===
Math teacher Enrico Mwangi seems calculating.
-> questioning
=questioning
*Alibi
   "Where were you when the murder took place?"
   "I was overseeing reexamination of previously failed students"
   {werewolf==true:
   "I thought I would engage them more if I made the vaccination question deal with something cool. "
   "Seems lycantropy is not a cool enough fiction to sell math interest. "
   "Well kiloid sellers are also going to miss out on the free advertising. "
   ~ lucan_cure=true
   }
   {lucan_formula==true:
   "Like polypinkiloid?
   "Yes, like polypinkiloid."
   }
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