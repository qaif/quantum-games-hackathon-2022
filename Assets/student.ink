===Rascal===
Almost as active as if bored out of their mind in a full lecture hall {~2|3|4} hours straight. # narration
What took you so long? #  rascal
They have not been letting me leave until the case is solved. # rascal
So hurry up # rascal
* [Calming]
   "Hey, its not like you are in a hurry for exams as the question source just left the mortal coil" # protagonist
   "But this still sucks highly" # rascal
     "I don't even like these books" # rascal
     You glance at a book resting on the table which seems to be about the mathematics of lunar phases. # narration
   {werewolf==true:
     Hey you never know when you might need some knowledge. So better prepare while you still can # protagonist
   }
   {protagonist_name=="Ada":
     It seems to only concern Luna. Nothing on Europa on it. So "new world" of them. # narration
   }
* [Impulse Control]
   One way of getting rid of distractions is to bulldoze them out of the way. # protagonist
   You didn't happen to have a clash with the boredom stuffer? # protagonist
   {debt==true:
   You trying catching me riding dirty. But I am a survivor. # rascal
    -else:
   I might flame up but I also cool down fast # rascal
   }
* [Passion]
   If you put such effort into studying as you put into rebelling you might get somewhere # protagonist
   What do you know about studying? # rascal
   And as the System itself you are the last one to advice about rebellion # rascal
   {affair==true:
       It is not like the teachers are any more focused than we are. # rascal
   -else:
       So be a nice little obient gear in the machine before I burst the whole thing wide open. # rascal
   }
* [Official]
   It is going to take as long as it will take # protagonist
   With cooperation it will take less time # protagonist
-
->Plea

=Plea
*[Alibi]
  Were you here already when the murder took place? # protagonist
  {affair:
  You wish, but I will make you sad by informing that I was away. # rascal
   - else:
   Ah don't remind me how close to eternity this torture is. # rascal
   I was and I wish I wasn't. # rascal
   }
   ->Plea
*[Motive]
  So did you get along with the professor? # protagonist
  Not on the verge of flunking? # protagonist
  {werewolf==true:
       Atleast our department does not extort money from us for secret drinks # rascal
       ~ lucan_extort=true
  -else:
      Not more than usual. # rascal
  }
  ->Plea
*[Guilt]
  Did you do it? # protagonist
  {guilty=="student":
  Off course not # rascal
  - else:
  I wish I had # rascal
  }
  ->Plea
+ Leave
   -> auditorium
-
-> auditorium