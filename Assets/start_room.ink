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






VAR world = "A"
~ world = "{~A|B|C|D|E}"
VAR injury = "plain"
~ injury = "{~plain|slice|blunt}"
VAR storm = false
~ storm = "{~false|true}"
VAR werewolf = false
~ werewolf="{~false|true}"
VAR guilty = "butler"
~ guilty="{butler|boy}"
VAR weapon = "knife"
~ weapon="{knife|baseball bat}"
VAR protagonist_name = "Detective"
~ protagonist_name = "{~Mary|Charles|Stanley|Ada}"
VAR debt= false
~ debt="{~false|true}"
VAR affair= false
~ affair="{~false|true}"

lets tell a story

->titleLine

=titleLine
Welcome to play Quantum Detective.
+ wait
   -> titleLine
+ start
  ->startingScene
+ credits
  Antti Salo
  Riikka-Lotta Pehkonen
  Mich
  -> titleLine

-> startingScene

=== startingScene ===

= startDescription
You wake up with the strangest feeling as if somebody has departed this earth.
Luckily your day deals with much simpler matters.
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
   