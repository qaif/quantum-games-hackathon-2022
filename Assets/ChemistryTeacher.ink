=== ChemistryTeacher ===
Chemistry teacher Deep Tamura seems jolty.
*Alibi
    "Where were you when the murder took place?"
    {affair:
        "Just mixing some of my chemicals."
    - else:
        " Supervising my student study group."
    }
    {werewolf:
        Do tell me if in your investigation you find a purple potion.
        I think one of the students stole one from me.
    }
    -> Coffee.coffeetable
*Motive
   "Did you get along with the victim well?"
   {affair:
      "He was a good colleague of mine."
   - else:
      "They were well liked."
   }
   {guilty=="chemistry":
      "I hope you will find the perpetrator."
   - else:
      "I think everybody can say that."
   }
   -> Coffee.coffeetable
*Guilt
   "Did you do it?"
   {guilty=="chemistry":
       "No."
   - else:
       "Yes. He was too good for this earth.
   }
-> Coffee.coffeetable
