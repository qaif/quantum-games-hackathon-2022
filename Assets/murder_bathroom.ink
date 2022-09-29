==MurderBathroom==

=EnteringBathroom
Make a mess, {protagonist_name} will clean it up. # protagonist
{protagonist_name} do this. {protagonist_name} do that. # protagonist
Allways the same old. No sense to be mindful of the floor cause we allways got... # protagonist
...something isn't quite right # narration
You watch in horror that the bathroom is already occupied. # narration
Not by somebody but something that used to be human. # narration
After coming to terms with reality you discover that the victim has been pierced by red lipstick, a pink page separator and a blue pen. # narration
This seems like a mystery you need to get to the bottom of. # narration
-> Cavader
=Cavader
*[Pen]
   The blue pen seems elegant. Being used like a sword doesn't compliment its true power. # narration
   -> Cavader
*[Separator]
   The separator has torn this poor human from this mortal coil. # narration
   Straw that breaks the camels back and all. # narration
   -> Cavader
*[Lipstick]
   Atleast they went out with a bang. Too bad the party friend didn't stick around to help. # narration
  -> Cavader
+ Inspect body
    -> body.inspect
+ Retreat outside
   That is not a sight one forgets for some time. # narration
   ~ priority_note=false
   ->hallway
  
* ->
   That is not a sight one forgets for some time. # narration
   ~ priority_note=false
   -> hallway
   
