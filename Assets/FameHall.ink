===HallOfFame===
Only the worthy may pass.
The walls are lined up with various persons.
There is a sign warning about over studying tearing you apart.
What incoherent non-sense.
The hall continues up stairs.
{protagonist_name=="Lisa":
"Oh, hi Mark", you greet your buddy security guard
}
+down
  Your head is almost spinning from all the sparklies
  -> hallway
+up
  {world=="E":
     An honor guard blocks your movement.
    {"This next area has some standards. Please step aside."|"Please step aside."|"I know you are frustrated but please remain calm"|"Please step back."|"You may not enter."}
    -> HallOfFame
  - else:
    Weird way to break up a hall into multiple stories.
    -> HallOfD
  }
   
=HallOfD
{protagonist_name=="Lisa":
     Why are there spoons instead of faces in the pictures here?
-else:
     Curiously the faces here more look like each other than on the lower floor.
}
+down
  -> HallOfFame
+up
  {world=="D":
     An honor guard blocks your movement.
    {"This next area has standards. Please step aside."|"Please step aside."|"I know you are frustrated but please remain calm"|"Please step back."|"You may not enter."}
    -> HallOfD
 - else:
    Weird way to break up a hall into multiple stories.
    -> HallOfC
  }

=HallOfC
{protagonist_name=="Lisa":
     Lisa you are tearing me apart!
-else:
     Maybe this is the output catalog of a cloning project?
}
+down
  -> HallOfD
+up
  {world=="C":
     An honor guard blocks your movement.
    {"This next area has high standards. Please step aside."|"Please step aside."|"I know you are frustrated but please remain calm"|"Please step back."|"You may not enter."}
    -> HallOfC
  - else:
    Weird way to break up a hall into multiple stories.
    -> HallOfB
  }


=HallOfB
Now you start to be rather high up.
+down
  -> HallOfC
+up
  {world=="B":
     An honor guard blocks your movement.
    {"Only the best may pass. Please step aside."|"Please step aside."|"I know you are frustrated but please remain calm"|"Please step back."|"You may not enter."}
    -> HallOfB
  - else:
    Weird way to break up a hall into multiple stories.
    -> HallOfA
  }


=HallOfA
It is lonely at the top.
+down
  -> HallOfB
