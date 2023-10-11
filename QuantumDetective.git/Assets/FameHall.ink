===HallOfFame===
Only the worthy may pass. # narration
The walls are lined up with various persons. # narration
There is a warning sign: # narration
Don't study too hard # written
it will tear you apart # written
What incoherent non-sense. # narration
The hall continues up stairs. # narration
{protagonist_name=="Lisa":
Oh, hi Mark # protagonist
you greet your buddy security guard
}
+down
  Your head is almost spinning from all the sparklies # narration
  -> hallway
+up
  {world=="E":
     An honor guard blocks your movement. # narration
    {This next area has some standards. Please step aside.|Please step aside.|I know you are frustrated but please remain calm|Please step back.|You may not enter.} # guard
    -> HallOfFame
  - else:
    Weird way to break up a hall into multiple stories.
    -> HallOfD
  }
   
=HallOfD
{protagonist_name=="Lisa":
     Why are there spoons instead of faces in the pictures here? # narration
-else:
     Curiously the faces here more look like each other than on the lower floor. # narration
}
+down
  -> HallOfFame
+up
  {world=="D":
     An honor guard blocks your movement. # narration
    {This next area has standards. Please step aside.|Please step aside.|I know you are frustrated but please remain calm|Please step back.|You may not enter.} # guard
    -> HallOfD
 - else:
    Weird way to break up a hall into multiple stories. # narration
    -> HallOfC
  }

=HallOfC
{protagonist_name=="Lisa":
     Lisa you are tearing me apart! # narration
-else:
     Maybe this is the output catalog of a cloning project? # narration
}
+down
  -> HallOfD
+up
  {world=="C":
     An honor guard blocks your movement. # narration
    {This next area has high standards. Please step aside.|Please step aside.|I know you are frustrated but please remain calm|Please step back.|You may not enter.} # guard
    -> HallOfC
  - else:
    Weird way to break up a hall into multiple stories. # narration
    -> HallOfB
  }


=HallOfB
Now you start to be rather high up. # narration
+down
  -> HallOfC
+up
  {world=="B":
     An honor guard blocks your movement. # narration
    {Only the best may pass. Please step aside.|Please step aside.|I know you are frustrated but please remain calm|Please step back.|You may not enter.} # guard
    -> HallOfB
  - else:
    Weird way to break up a hall into multiple stories. # narration
    -> HallOfA
  }


=HallOfA
It is lonely at the top. # narration
+down
  -> HallOfB
