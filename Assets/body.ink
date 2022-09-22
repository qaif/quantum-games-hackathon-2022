=== body ===

= inspect
+ [Inspect] 
        + +  torso
            {injury=="slice":
                There are slices in the left side of the stomach
           -else:
                A bit bloated, the stomach wiggles as you touch it
            }
            -> inspect
        + +  neck 
            {guilty=="victim":
               The neck has rope marks on the front. 
               It is twisted back, like someone pulled hard
            -else:
               The angle of the neck provokes great uncomfortability in you in sympathy to the person that is no longer there.  
            }
            {affair==true:
                The red all around the neck does not seem to be blood?
            }
            -> inspect
        + + knee
            {guilty=="kobra":
                  There are two small punctured wounds.
            -else:
                  Well your adventure days are over.
            }
            -> inspect
        + + shoulder
            {injury=="blunt":
               The shoulder is crushed
            -else:
               No more any burdens to carry on those.
            }
            -> inspect
        + +  Enough
             -> MurderBathroom.Cavader 
        
*  Go back
    -> MurderBathroom.Cavader 
