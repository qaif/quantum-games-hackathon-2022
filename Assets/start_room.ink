// INCLUDE Testing_dialog.ink
INCLUDE body.ink
INCLUDE introduction.ink
INCLUDE hallway.ink
INCLUDE cleaning_cellar.ink
INCLUDE butler.ink
INCLUDE office.ink
//INCLUDE auditorium.ink
INCLUDE characterlist.ink
INCLUDE runa_cat.ink
INCLUDE student.ink
INCLUDE cafeteria.ink
INCLUDE book.ink
INCLUDE FameHall.ink
INCLUDE cat_boxing.ink
INCLUDE auditorium.ink
INCLUDE computing.ink


INCLUDE HistoryTeacher.ink
INCLUDE MathTeacher.ink
INCLUDE ChemistryTeacher.ink



INCLUDE resolution.ink

EXTERNAL coherentLottery(lotterytype)
EXTERNAL splitWorld(detail)
EXTERNAL degreeSplitWorld(detail,amount)


EXTERNAL degreeXGate(detail,amount) // degree is dummy
EXTERNAL degreeYGate(detail,amount) // degree is dummy
EXTERNAL degreeZGate(detail,amount)

EXTERNAL checkForMultiverseValue(detail)



VAR retry=false

VAR world = "A"
~ world = "{~A|B|C|D|E}"
VAR injury = "plain"
~ injury = "{~plain|slice|blunt}"
VAR storm = false
~ storm = "{~false|true}"
VAR werewolf = false
~ werewolf="{~false|true}"
VAR guilty = "butler"
~ guilty="{~butler|student|history|chemistry|math|protagonist|victim|accident|runa|merry}"
VAR weapon = "knife"
~ weapon="{~knife|bat|chop|kobra|brain|words}"
VAR protagonist_name = "Detective"
~ protagonist_name = "{~Mary|Charles|Stanley|Ada|Lisa|Harry}"
VAR debt= false
~ debt="{~false|true}"
VAR affair= false
~ affair="{~false|true}"

VAR critter=false
~ critter="{~true|false}"

VAR priority_note=true
VAR lucan_potion=false
VAR lucan_extort=false
VAR lucan_cure=false
VAR lucan_borrow=false
VAR lucan_identity=false
VAR lucan_formula=false
VAR lucan_points=0

VAR post_task=false
VAR post_revenge=false
VAR post_box_label="animal"
VAR post_cat_up=false
VAR post_cat_dead=false
VAR post_neurotoxin=10
VAR post_bomb_armed=false
VAR post_bomb_exploded=false
VAR post_probe=false
VAR post_china=false

VAR post_task_score=0
VAR post_cat_error=0

VAR bomb_smuggle=false
VAR sender_compartment=false

VAR producer_plop=false
VAR producer_carrying=false
VAR com_password="a"
VAR com_state=false

VAR com_sender_quantum_channel=false
VAR com_receiver_quantum_channel=false

VAR com_message_loaded=false

VAR com_delivery="none"

VAR sender_production=false

VAR post_bomb_error=0
VAR post_bomb_burden=0

VAR post_wall_skin=false
VAR post_wall_meat=false
VAR post_wall_stone=false

VAR antisymmetry_alice=false
VAR antisymmetry_bob=false


VAR passcode=false

VAR fancy_passcode=false

VAR skeleton_key=false

VAR phone_phrase="Hello"
VAR phone_wait_time=0
VAR phone_cool_off=0

VAR clock=0

VAR splitTest=false

VAR warp_story=false
VAR warp_target=""

VAR johnny_points=0

{weapon == "knife":
    ~injury="slice"
}
{weapon == "kobra":
    ~injury="slice"
}
{weapon == "bat":
    ~injury="blunt"
}
{weapon == "chop":
    ~injury="blunt"
}
{weapon=="brain":
    ~injury="plain"
}
{weapon=="words":
    ~injury="plain"
}
->titleLine

=== function splitWorld(detail)
~ return "splitting world"

=== function coherentLottery(detail)
~ return "throwing dice"


===titleLine===
Quantum Detective # program

~ phone_phrase=coherentLottery("phone")
~ com_password=coherentLottery("com")
{com_password=="pony":
     {world=="A":
            ~ com_state=true
     }
     {world=="B":
            ~ com_state=true
     }
     {world=="C":
            ~ com_state=false
     }
     {world=="D":
            ~ com_state=false
     }
     {world=="E":
            ~ com_state=true
     }
}
{com_password=="frog":
     {world=="A":
            ~ com_state=false
     }
     {world=="B":
            ~ com_state=true
     }
     {world=="C":
            ~ com_state=true
     }
     {world=="D":
            ~ com_state=false
     }
     {world=="E":
            ~ com_state=false
     }
}
{com_password=="owl":
     {world=="A":
            ~ com_state=false
     }
     {world=="B":
            ~ com_state=false
     }
     {world=="C":
            ~ com_state=true
     }
     {world=="D":
            ~ com_state=false
     }
     {world=="E":
            ~ com_state=true
     }
}

This game is played by entering text into the textbox (and submitting by enter). # program

+ wait
   {You take a while looking at the marvelous title screen.|Yes, it is really quite grand. You are excited to see how it plays.|Eager to cling to the smallest details you are spending way more time at the title line than the developers expected|Like the developers in the game jam, you don't have infinite amount of time to use.} # narration
   {protagonist_name=="Stanley":
       This brings you fond memories of various closets you have been in. # narration
   }
   -> titleLine
+ start
  ->startingScene
+ credits
  Created as part of Global Quantum Game Jam 2022 # program
  Antti Salo # program
  Riikka-Lotta Pehkonen # program
  Michelle Alexandra # program
  -> titleLine
+ quit
  You are supposed to solve a murder and not terminate programs. # program
  Are you sure? # program
  **yes
     ->END
  **no
    ->titleLine
-> startingScene

=== startingScene ===

= startDescription
You are asleep # narration
Every journey is a series of choices. The first is to begin the journey. # narration
* Wake up 
   -> bedUp 
* Don't wake up
   -> resolution.Demise
* That's it two lines?
   Oh, you want an artsy fancy pants indie game. # program
   I will give you fancy pants... # program
   ... # program
   There is primordial blackness. # narration
   A reptilian brain drinks it in like a beer. # narration
   An unimaginably hoarse sound booms what would be all over if there was anything. # narration
  The is no Innocence, not even one with glowing lungs. # narration
  Soon a smile will spring as icon for the ages to keep the ex-wives away. # narration
  It is not sponsored by a mad hatter, not for lack of not being mad enough. # narration
  And definetely not for the tea for not being strong enough. # narration
  The man whose job it is to find the naked truth # narration
   rather escapes trying to sunset his brain into tequila. # narration
   **Oh that is a cool game I want to play that
         Well you have to get your ass up from the chair if you want to get to that flashy disco. # program
         The prince has not even set a keeper... clearly anarch lands. # narration
	*** I shall go embrace that game tonight
	*** You are being too cryptid for my tastes. I am leaving.
	--- 
         	-> END
   **This is terribly confusing I don't want this
         Good. # program
         We are going to do this nice and simple. # program
         Figure it out piece by piece. # program
         And not frontloading with useless information. # program
         {protagonist_name=="Stanley":
             I am not going to draw you any more adventure lines. # program
         }
         ->bedUp
   
* Too much curiosity can get the best of us. # program
   Some events happen whether we want them to or not. # program
   ->bedUp

=bedUp
#Protagonist
You wake up with the strangest feeling as if somebody has departed this earth. # narration
{protagonist_name=="Charles":
   You feel majestic despite your long life. # narration
- else:
   Luckily your day deals with much simpler matters. # narration
}
The university comfortability is on your shoulders as its janitor. # narration
Yesterday performance review gave you a grade of {world}. # narration
Some students were complaining about the toilets. # narration
So better start with that. # narration
Lets write that down... # narration
Luckily you carry an amble supply of pens with you. # narration
{guilty=="protagonist":
     Well, you try to have lots. # narration
     You seem to be down to only two. # narration
-else:
     Toilet is messy, priority job. Yell back at students.# program
     There done. # narration
}

With days priorities set, time to go earn the next grade. # narration
+ Enter university

-> janitor.protagonist




= bodyOverview
    * [Inspect body]
         -> body
    * Go back 
        -> startDescription
-> DONE
   