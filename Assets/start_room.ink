// INCLUDE Testing_dialog.ink
INCLUDE body.ink
INCLUDE introduction.ink
INCLUDE hallway.ink
INCLUDE cleaning_cellar.ink
INCLUDE butler.ink
INCLUDE office.ink


VAR world = "A"
~ world = "{~A|B|C|D|E}"
VAR injury = "plain"
~ injury = "{~plain|slice|blunt}"
VAR storm = false
~ storm = "{~false|true}"
VAR werewolf = false
~ werewolf="{~false|true}"
VAR quilty = "butler"
~ quilty="{butler|boy}"
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

-> startingScene

=== startingScene ===

= startDescription
There is a murder, the character must find out who it was.
Our hero had just received a grade of {world}.

At the crime scene there are clues about who is the killer.
+ Enter the university

-> janitor.protagonist




= bodyOverview
    * [Inspect body]
         -> body
    * Go back 
        -> startDescription
    
   