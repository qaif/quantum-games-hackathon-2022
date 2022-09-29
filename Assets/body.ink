=== body ===

= inspect
         +  torso
            {injury=="slice":
                There are slices in the left side of the stomach # narration
           -else:
                A bit bloated, the stomach wiggles as you touch it # narration
            }
            -> inspect
         +  neck 
            {guilty=="victim":
               The neck has rope marks on the front. # narration
               It is twisted back, like someone pulled hard # narration
            -else:
               The angle of the neck provokes great uncomfortability in you in sympathy to the person that is no longer there.  # narration
            }
            {affair==true:
                The red all around the neck does not seem to be blood? # narration
            }
            -> inspect
         + knee
            {guilty=="kobra":
                  There are two small punctured wounds. # narration
            -else:
                  Well your adventure days are over. # narration
            }
            -> inspect
         + shoulder
            {injury=="blunt":
               The shoulder is crushed # narration
            -else:
               No more any burdens to carry on those. # narration
            }
            -> inspect
        +  Enough
             -> MurderBathroom.Cavader 
