=== cleaning_cellar ===

= aEntersACleaning
{protagonist_name} enters a cleaning cellar. # narration
-> CellarItems

= CellarItems
On the floor, besides all the bottles of cleaning liquids, buckets, brushes and swabs # narration
is a book with the name "Bernard Tar", # narration
an earring, a hat and a feather. # narration
Oh and the russian roulette booth is dangerous, better leave that alone # narration
{lucan_borrow==true:
There are not enough feathers to pose a threat to anyones dignity. # narration
}
-> CellarActions

= CellarActions
        + Open book
            -> book.page1
        + Inspect earring
            The earring seems a spiral made of golden, with a small amethyst in the center. # narration
            -> CellarActions
        + Inspect hat
            The hat is brown, with a broad brim. # narration
            -> CellarActions
        + Inspect feather
            The feather is large and coloured in brilliant red and blue. # narration
            -> CellarActions
        + Inspect bucket
            You find a scarlet fish swimming in the bucket! # narration
            How unsual, this has to be a central clue to this mystery. # narration
            -> CellarActions
        + Go into roulette booth
              -> ImmortalityBooth
        + Return to hallway
            -> hallway


=ImmortalityBooth
You step into the booth # narration
It is quite dense # narration
~ splitWorld("pistol")
Atleast you are getting excitement for you time # narration
and then ... # narration
{pistol==true:
     BANG! # program
     You don't even feel the floor you were headed to # narration
     -> resolution.Demise
-else:
     ~ luck=luck +1
     Well, that was anticlimatic # narration
     You are actually started to get bored # narration
     {luck==1:
             This seems to happen to me. # narration
     }
     {luck==2:
             Is this thing even on?. # narration
     }
     {luck==3:
             Why I wasted my luck here instead of a lottery?. # narration
     }
     {luck==4:
             This seems to get historical proportions. # narration
     }
     {luck==5:
             Maybe I am already dead and just have not realised it. # narration
     }
     {luck>5:
             I can only conclude that I am immortal # narration
     }
     Lets get back onto the case # narration
     ->CellarItems
}