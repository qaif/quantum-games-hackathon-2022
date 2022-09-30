//Runa Coello. Philosophy student. Has a cat.

=== Runa_cat===
A purring cat sits on the shoulder of the young woman. # narration
So, would the professor have died if no one would have opened the door? # runa
It is in a way like the question, does a falling tree make a sound if there is no one to hear it? # runa
Or would you rather hear me quote Nietzsche? # runa

* [Perspectivism]
   The willingness is more essential than the merit of the goal itself # runa
   A thousand goals have there been so far # runa
* [Eternal return]
   The universe has been recurring, and will continue to recur, for an infinite number of times across infinite time or space. # runa
   # runa
   {injury=="slice":
        Is there death as everything eternally returns? # runa
        You spot a few drops of blood on the shoulder, near the paws of the white furrball. # narration
        They say cats have nine lives, don't they? So does the cat gain more by taking another? # protagonist
    -else:
   Isn't that horrifying and paralyzing? # runa
   }
* [Immoralist]
   Art as the single superior counterforce against all will to negation of life. # runa
   Pity makes suffering contagious. # runa
   So are you saying morality is good for the masses and should be left to them? # protagonist
* [Will to Power]
   The qualities of matter are a result of an interplay of forces. # runa
   Are you going to burn my notes? # protagonist
-
->Plea

=Plea
*[Alibi]
  Were you here already when the murder took place? # protagonist
    You'd need to define here, and also 'there'. # runa
    -> Plea
*[Motive]
  So is the death a truly relativistic concept for you? # protagonist
  # runa
  -> Plea
*[Guilt]
  Did you do it? # protagonist
  {guilty=="runa_cat":
  Of course not # runa
  -else:
  Is the question about doing or thinking more important for you than the question about being? # runa
  }
*{animal_cruelty==true}[Cat Execution]
   It seems that the post station is killing all the cats # protagonist
   sent through there to ease shipments. # protagonist
   To be or not to be is not a choice the cats get to make. # runa
   You seem to take this pretty easy # protagonist
   {post_cat_dead==true:
        Life is the best drug. Not as easy as you took anothers. # runa
        -> Plea
   }
   Life is the best drug. In order to provide it to most cats # runa
   {guilty=="runa":
           {injury=="plain":
                    I just found some sleep powder. You should take it # runa
           }
   -else:
        I give you this proper sleep powder # runa
   }
   Hey this will find use # protagonist
   I have tried to get them to stop using cats #runa
   But our late professor insisted upon it # runa
   even if it made half the univeristy hate them for it # runa
   ~ sleep_powder=true
   {guilty=="runa":
          {injury=="slice":
                   Even the cats knew that he was up to no good # runa
                   Did they start to make trouble in the neighbourhood # protagonist
                   There was just this one little fight and the decan got scared # runa
                   saying I should move all my cats to classroom B # runa
                   Did you try to make any noise about it? # protagonist
                   My teaching licence is quite fresh so I didn't want to gamble on it # runa
          }
          {injury=="plunt":
                  We will just have to live with our choices. Or I guess die by them. # runa
          }
   }
   -> Plea
+Disengage
   -> classroom
- 

