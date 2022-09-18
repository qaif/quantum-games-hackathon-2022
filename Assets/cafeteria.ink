===Coffee===

INCLUDE suspect_C.ink
INCLUDE suspect_d.ink
INCLUDE suspect_e.ink
-> coffeetable


=coffeetable
Some people are lazily biding their time.

This seems like a good place to address a large crowd.
Am I ready to crack this case?
+ lets gather some more info before
   -> hallway
+ Chat with loungers
  -> Clique
   
=Clique
A group of people are animatedly talking.
They all seems to be teachers.
Time to pick your favorite subject.
* History
  ->SuspectC.historySuspect
* Chemistry
  ->SuspectD.chemistryTeacher
* Math
  ->SuspectE.mathTeacher

