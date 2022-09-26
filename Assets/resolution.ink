=== resolution ===
=Resolutionstart

So what evidence do I have?
* Zip. Nada
  Should I just give up on the case?
  ** Yes, this is hopeless
      All this mystery is hurting my brain. Screw you guys I am going home!
     -> Abandon
  ** No, I can do this if I put my mind into it
      ->Coffee
  ** I bet I can just guess the culprit
* Everything, 100% speedrun
* Enough
-

VAR win_who=false
VAR win_why=false
VAR win_how=false

-> whoResolution
=whoResolution
Who I think did it?
* Math teacher
    {guilty=="math":
         ~ win_who = true
    }
* Chemistry teacher
    {guilty=="chemistry":
        ~ win_who = true
    }
* History teacher
    {guilty=="history":
        ~ win_who = true
    }
* Rebellious student
    {guilty=="student":
        ~ win_who = true
    }
* Cat lady
    {guilty=="runa":
        ~ win_who = true
    }
* {lucan_identity==false} That totally random student
* {lucan_identity==true} Merry Bieber
    {guilty=="merry":
        ~ win_who = true
    }
* Butler
   It's always the butler.
    {guilty=="butler":
         ~ win_who = true
    }
* Me
    {guilty=="protagonist":
         ~ win_who = true
    }
* Suicide
    {guilty=="victim":
         ~ win_who=true
    }
* Accident. A really bad case of diarea.
    {guilty=="accident":
         ~ win_who=true
    }
-
-> whyResolution

=whyResolution
Why they did it?
* For the mad lolz
    {guilty=="protagonist":
          ~ win_why = true
    }
* To get out of debt
    {debt==true:
         ~ win_why = true
    }
* Crime of passion
    {affair==true:
         ~ win_why = true
    }
* Indifferent universe doesn't need a reason to grind us to dust
    {guilty=="accident":
        ~ win_why = true
    }
* Depression
    {guilty=="victim":
        ~ win_why = true
    }
* Savage instincts:
    {werewolf==true:
        ~ win_why = true
    }
-
-> scoring
/*
=howResolution
How they did it?
* With style
* Knife
   {weapon=="knife":
        ~ win_how = true
   }
* Baseball bat
   {weapon=="bat":
       ~ win_how = true
   }
* Judoest of chops
   {weapon=="punch":
       ~ win_how = true
   }
* Kobra
   {weapon=="kobra":
       ~ win_how = true
   }
* With oblivion
   {weapon=="brain" : 
       ~ win_how = true
   }
* Mental overload
   {weapon=="words":
       ~ win_how = true
   }
-

{guilty}
{weapon}
{debt} {affair} {werewolf}
*/
=scoring
VAR points = 0
{win_who==true:
    I got who did it
    ~ points = points + 1
}
{win_why==true:
    I got why it was done
    ~ points = points + 1
}
{win_how==true:
   I got how it was done
   ~ points = points + 1
}

{points>=2:
    ->Win
}
{points>0:
     You have some clue what is going on.
     For lack of evidence nobody is found guilty of the crime.
}
-> Loss

=Win
You win.
Case cracked wide open.
All the mysteries of the universe reveal themselfs under your careful eye.
Now go figure out the real one.
* Accept outcome
  You step into the light through the fourth wall.
  ** Oh no the great beyond
  ** GG no re
  -> END
* Retry
   No. This is too fun. I think there are still mysteries to figure out about it.
   So, here we go again for the {1003645th|1003646th|1003647th|1003648th|1003649th|   1003650th|umpfteenth} time.
   ~ retry = true
   ** I will never get bored of this
   ** oh I won? I knew it was not guesswork
   -
   -> END 


=Loss
The mystery was too tough a nut to crack.
The misleading theories allowed for the perpatrator to hide so well they were not found.
Having meddled in so important matters beyond your duties
the university doesn't renew your work contract.
You lose.
* Accept outcome
   -> END
* Retry
   ~ retry = true
   -> END

=Abandon
{post_revenge==true:
     You went home.
     Before you got inside a jaguar jumped on you.
     With your puny unmotivated human hands you had no chance to win the fight.
     You die.
-else:
     You went and slept it off.
     Next days newspaper had a big article of the impenetrable mystery of the murder.
     Your performance grade for that day was F.
     Apparently they don't like blood on their floors.
    Your day begins a totally unconnected adventure.
}

=Demise
    You die.
    * Accept outcome
        -> END
    * Retry
        ~ retry=true
        -> END
    * Use half of your smash coins to continue
        You don't have enough smash coins to continue
        ** Master this hand!
        ** Ben is a hoe anyway
        --
        -> END
