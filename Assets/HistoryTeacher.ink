//Suspect C
=== HistoryTeacher ===
History teacher Chloe Greenberg seems dusty. # narration
->questioning
=questioning
*[Alibi]
   Where were you when the murder took place? # protagonist
   Studying books # historyT
   {werewolf==true:
       Let Merry know that if he doesn't give the Tar book back I am going to roll them in tar. # historyT
       ~ lucan_borrow=true
   }
   -> HistoryTeacher.questioning
*[Motive]
   Where you on good terms with the victim? # protagonist
   We were on good enough terms that we even got married. # historyT
   {guilty!="history":
   They even still have me as the benefactor of their will. # historyT
   - else:
    But we grew more distant with time. # historyT
   }
   {affair==true:
         But I am also glad we did end up divorcing # historyT
         I am pretty sure they are cheating on their current partner # historyT
         I found a strange communication device in their office #historyT
         and the stuff I overheard once was not that innocent # historyT
   }
   -> HistoryTeacher.questioning
*[Guilt]
  Did you do it? # protagonist
  {debt==true:
      No, I didn't # historyT
  - else:
      I did not. # historyT
  }
  -> HistoryTeacher.questioning
+ Leave
    -> Coffee.coffeetable
-
->HistoryTeacher.questioning
