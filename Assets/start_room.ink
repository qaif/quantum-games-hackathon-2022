// INCLUDE Testing_dialog.ink
INCLUDE body.ink
lets tell a story
-> startingScene

=== startingScene ===

= startDescription
There is a murder, the character must find out who it was.
In a school, a student see  a corpse.
At the crime scene there are clues about who is the killer.
-> bodyOverview

= bodyOverview
    * [Inspect body]
         -> body
    * Go back 
        -> startDescription
    
   