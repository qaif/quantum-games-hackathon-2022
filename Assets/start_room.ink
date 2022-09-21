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

INCLUDE HistoryTeacher.ink
INCLUDE MathTeacher.ink
INCLUDE ChemistryTeacher.ink

INCLUDE resolution.ink




VAR world = "A"
~ world = "{~A|B|C|D|E}"
VAR injury = "plain"
~ injury = "{~plain|slice|blunt}"
VAR storm = false
~ storm = "{~false|true}"
VAR werewolf = false
~ werewolf="{~false|true}"
VAR guilty = "butler"
~ guilty="{~butler|student|history|chemistry|math|protagonist|victim|accident}"
VAR weapon = "knife"
~ weapon="{~knife|baseball bat|chop|kobra|brain|words}"
VAR protagonist_name = "Detective"
~ protagonist_name = "{~Mary|Charles|Stanley|Ada|Lisa}"
VAR debt= false
~ debt="{~false|true}"
VAR affair= false
~ affair="{~false|true}"

->titleLine

=titleLine
Quantum Detective

This game is played by entering text into the textbox (and submitting by enter).

+ wait
   {You take a while looking at the marvelous title screen.|Yes, it is really quite grand. You are excited to see how it plays.|Eager to cling to the smallest details you are spending way more time at the title line than the developers expected|Like the developers in the game jam, you don't have infinite amount of time to use.}
   {protagonist_name=="Stanley":
       This brings you fond memories of various closets you have been in.
   }
   -> titleLine
+ start
  ->startingScene
+ credits
  Created as part of Global Quantum Game Jam 2022
  Antti Salo
  Riikka-Lotta Pehkonen
  Michelle Alexandra
  -> titleLine
+ quit
  You are supposed to solve a murder and not terminate programs.
  ->titleLine
-> startingScene

=== startingScene ===

= startDescription
You wake up with the strangest feeling as if somebody has departed this earth.
{protagonist_name=="Charles":
   You feel majestic despite your long life.
- else:
   Luckily your day deals with much simpler matters.
}
The university comfortability is on your shoulders as its janitor.
Yesterday performance review gave you a grade of {world}.

Well, time to earn the next grade.
+ Enter university

-> janitor.protagonist




= bodyOverview
    * [Inspect body]
         -> body
    * Go back 
        -> startDescription
-> DONE
   