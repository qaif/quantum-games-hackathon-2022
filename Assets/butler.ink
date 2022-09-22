==Butler==
Stylish as ever {protagonist_name} approaches a calm servant that could be mistaken for a statue, if they would not breathe.
"You are the one investigating the murder..."
"...and why have you come to see me?"
* [Snark]
  "Isn't it always the butler?"
  "Do you think that is funny?"
  -> Plea
* [Professional]
  "I am to check all relevant personel"
  {affair==true:
   "Yes, it is good to fullfill our roles well."
  -else:
  "And you think I am relevant to the murder?"
  }
  ->Plea
* [Grim]
  "Death comes for us all and I am here to check that you didn't invite it prematurely"
  "With that kind of attitude you should be investigating yourself"
  {guilty=="protagonist":
       "But now I am investigating you."
  }
  ->Plea

=Plea
* [Alibi]
   "So where were you when the murder took place?"
   {injury=="blunt":
   "Ironing shirts"
   }
   {injury=="slice":
   "Gardening the memorial shrub"
   }
   {injury=="plain":
   "Supervising that the cooks implemented the seasoning request"
   }
   ->Plea
* [Motive]
   "Was the murdered guy guy cool?"
   {guilty=="butler":
     "My master was a very well established person."
   -else:
     "My, ehm, Master, was a very well established person."
   }
  ->Plea
* [Guilt]
  "Did you do it?"
  "Off course, not!"
  "It isn't exactly serving if you cause your masters demise."
  {debt==true:
     "Whatever that service might entail."
  }
  ->Plea
+ Leave
  - ->office
