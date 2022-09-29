=== janitor ===

-> protagonist


= protagonist
As dutiful as ever {protagonist_name} sets off for work. # narration
Sometimes you feel so absent minded that you could forget your name. # narration
Both enrolled and working for the university means having a particularly close relationship to the grounds. # narration
{storm==false:
   Lets see what the bright day brings for {protagonist_name}. # narration
   - else:
   It is a stormy and dark day. {protagonist_name} fights the wind to reach safety. # narration
}
{protagonist_name=="Mary":
You tought you knew everything but you just learned how the color red looks like. # narration
-else:
The univeristy makes a nice silhuette against the sky. # narration
}
{critter==true:
     The smell of fresh cut grass brightens your mood. # narration
-else:
     Lots of students are already about. # narration
}
+ Enter hallway
-> hallway