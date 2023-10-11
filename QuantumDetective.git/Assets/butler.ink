==Butler==
Stylish as ever {protagonist_name} approaches a calm servant that could be mistaken for a statue, if they would not breathe. # narration
You are the one investigating the murder... # butler
...and why have you come to see me? # butler
* [Snark]
  Isn't it always the butler? # protagonist
  Do you think that is funny? # butler
  -> Plea
* [Professional]
  I am to check all relevant personel # protagonist
  {affair==true:
   Yes, it is good to fullfill our roles well. # butler
  -else:
  And you think I am relevant to the murder? # butler
  }
  ->Plea
* [Grim]
  Death comes for us all and I am here to check that you didn't invite it prematurely # protagonist
  With that kind of attitude you should be investigating yourself # butler
  {guilty=="protagonist":
       But now I am investigating you. # protagonist
  }
  ->Plea

=Plea
* [Alibi]
   So where were you when the murder took place? # protagonist
   {werewolf==false:
        {injury=="blunt":
             Ironing shirts # butler
        }
        {injury=="slice":
             Gardening the memorial shrub # butler
        }
        {injury=="plain":
              Supervising that the cooks implemented the seasoning request # butler
        }
   -else:
        I was washing clothes # butler
   }
   ->Plea
* [Motive]
   Was the murdered guy guy cool? # protagonist
   {guilty=="butler":
     My master was a very well established person. # butler
   -else:
     My, ehm, Master, was a very well established person. # butler
   }
  ->Plea
* [Guilt]
  Did you do it? # protagonist
  Off course, not! # butler
  It isn't exactly serving if you cause your masters demise. # butler
  {debt==true:
     Whatever that service might entail. # butler
  }
  ->Plea
+ Leave
  - ->office
