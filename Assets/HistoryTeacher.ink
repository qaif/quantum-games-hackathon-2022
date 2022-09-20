//Suspect C
=== HistoryTeacher ===
History teacher Chloe Greenberg seems dusty.

*[Alibi]
   "Where were you when the murder took place?"
   "Studying books"
   -> Coffee.coffeetable
*[Motive]
   "Where you on good terms with the victim?"
   "We were on good enough terms that we even got married."
   {not guilty=="history":
   "They even still me as the benefactor of their will."
   - else:
    "But we grew more distant with time."
   }
   -> Coffee.coffeetable
*[Guilt]
  "Did you do it?"
  {debt:
      "No, I didn't"
  - else:
      "I did not."
  }

-> Coffee.coffeetable
