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
         ~ win_why = true
    }
* Chemistry teacher
    {guilty=="chemistry":
        ~ win_why = true
    }
* History teacher
    {guilty=="history":
        ~ win_why = true
    }
* Student
    {guilty=="student":
        ~ win_why = true
    }
* Butler
   It's always the butler.
    {guilty=="butler":
         ~ win_why = true
    }
* Me
    {guilty=="protagonist":
         ~ win_why = true
    }
* Suicide
    {guilty=="victim":
         ~ win_why=true
    }
* Accident. A really bad case of diarea.
    {guilty=="accident":
         ~ win_why=true
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
-> howResolution
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

{win_who==true:
    I got who did it
    {win_why==true:
        I got why it was done
        {win_how==true:
                I got how it was done
    	->Win
        }
   }
}
-> Loss

=Win
You win.
Case cracked wide open.
All the mysteries of the universe reveal themselfs under your careful eye.
Now go figure out the real one.
* Step into the light through the fourth wall.
  -> DONE
* No. This is too fun. I think there are still mysteries to figure out about it.
  So, here we go again for the {1003645th|1003646th|1003647th|1003648th|1003649th|1003650th|umpfteenth} time.
  ->titleLine

=Loss
The mystery was too tough a nut to crack.
The misleading theories allowed for the perpatrator to hide so well they were not found.
Having meddled in so important matters beyond your duties
the university doesn't renew your work contract.
You lose.
-> DONE

=Abandon
You went and slept it off.
Next days newspaper had a big article of the impenetrable mystery of the murder.
Your performance grade for that day was F.
Apparently they don't like blood on their floors.
Your day begins a totally unconnected adventure.
