===HallOfFame===
Only the worthy may pass.
The walls are lined up with various persons.
There is a sign warning about over studying tearing you apart.
What incoherent non-sense.
The hall continues up stairs.
*down
  Your head is almost spinning from all the sparklies
  -> hallway
*up
  {world=="E":
     An honor guard blocks your movement.
    {"This next area has some standards. Please step aside."|"Please step aside."|"I know you are frustrated but please remain calm"|"Please step back."|"You may not enter."}
    -> HallOfFame
  - else:
    Weird way to break up a hall into multiple stories.
    -> HallOfD
  }
   
=HallOfD
Curiously the faces here more look like each other than on the lower floor.
*down
  -> hallway
*up
  {world=="D":
     An honor guard blocks your movement.
    {"This next area has standards. Please step aside."|"Please step aside."|"I know you are frustrated but please remain calm"|"Please step back."|"You may not enter."}
    -> HallOfD
 - else:
    Weird way to break up a hall into multiple stories.
    -> HallOfC
  }

=HallOfC
Curiously the faces here more look like each other than on the lower floor.
*down
  -> hallway
*up
  {world=="C":
     An honor guard blocks your movement.
    {"This next area has high standards. Please step aside."|"Please step aside."|"I know you are frustrated but please remain calm"|"Please step back."|"You may not enter."}
    -> HallOfC
  - else:
    Weird way to break up a hall into multiple stories.
    -> HallOfD
  }


=HallOfB
Curiously the faces here more look like each other than on the lower floor.
*down
  -> HallOfC
*up
  {world=="C":
     An honor guard blocks your movement.
    {"Only the best may pass. Please step aside."|"Please step aside."|"I know you are frustrated but please remain calm"|"Please step back."|"You may not enter."}
    -> HallOfB
  - else:
    Weird way to break up a hall into multiple stories.
    -> HallOfA
  }


=HallOfA
It is only at the top.
*down
  -> HallOfB
