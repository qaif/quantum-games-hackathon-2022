=== resolution ===
=Resolutionstart
So what evidence do I have?
* Zip. Nada
* everything, 100% speedrun
* Enough
-

VAR win_who=false
VAR win_why=false
VAR win_how=false

-> whoResolution
=whoResolution
Who I think did it?
* Math teacher
    {guilty=="math"} win_why = true
* Chemistry teacher
    {guilty=="chemistry"} win_why = true
* History teacher
    {guilty=="history"} win_why = true
* Student
    {guilty=="student"} win_why = true
* Butler
   It's always the butler.
    {guilty=="butler"} win_why = true
* Me
    {guilty=="protagonist"} win_why = true
* Suicide
* Accident. A really bad case of diarea.
-
-> whyResolution

=whyResolution
Why they did it?
* For the mad lolz
    {guilty=="protagonist"} win_why = true
* To get out of debt
    {debt==true} win_why = true
* Crime of passion
    {affair==true} win_why = true
* Indifferent universe doesn't need a reason to grind us to dust
* Depression
-
-> howResolution
=howResolution
How they did it?
* With style
* Knife
   {weapon=="knife"} win_how = true
* Baseball bat
   {weapon=="bat"}  win_how = true
* Judoest of chops
   {weapon=="punch"}  win_how = true
* Kobra
   {weapon=="kobra"}  win_how = true
* With oblivion
   {weapon=="brain"}  win_how = true
* Mental overload
   {weapon=="words"}  win_how = true
-

{win_who:
    {win_why:
        {win_how:
    	->Win
        }
   }
}
-> Loss

=Win
You win.
Case cracked wide open.
-> DONE

=Loss
You lose.
The mystery was too tough a nut to crack.
-> DONE