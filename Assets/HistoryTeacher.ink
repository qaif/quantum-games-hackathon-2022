//Suspect C
=== HistoryTeacher ===
History teacher Chloe Greenberg seems dusty.
->questioning
=questioning
*[Alibi]
   "Where were you when the murder took place?"
   "Studying books"
   {werewolf==true:
       Let Merry know that if he doesn't give the Tar book back I am going to roll them in tar.
       ~ lucan_borrow=true
   }
   -> questioning
*[Motive]
   "Where you on good terms with the victim?"
   "We were on good enough terms that we even got married."
   {not guilty=="history":
   "They even still have me as the benefactor of their will."
   - else:
    "But we grew more distant with time."
   }
   -> questioning
*[Guilt]
  "Did you do it?"
  {debt:
      "No, I didn't"
  - else:
      "I did not."
  }
  -> questioning
+ Leave
    -> Coffee.coffeetable
