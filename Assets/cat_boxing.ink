===CatDelivery===

The mail room, while quite spacious, is not really spacious enough for the amount of letters in it. # narration
A hurried worker is sorting letters with quite some fervor. # narration

+Engage worker
   -> approach
+Leave
   -> hallway


=approach

What you want from me? # postWorker
* Snarky 
    To deliver a solution to the murder mystery # protagonist
    Address unclear, return to sender # postWorker
* Serious
    For you to confess your guilt to the murder. # protagonist
    I don't have time for murders while the sorting is murdering my hands. # postWorker
* Professional
   What do you know about the murder? # protagonist
   Nothing, I know about letters. # postWorker
   {critter==true:
         I guess even letters knows more about murder. # narration
   }
-
-> questioning

=task
What if I don't want to sort the boxes? # protagonist
Then I don't want to talk with you. # postWorker
* Sort boxes
   So how I sort boxes? # protagonist
   Take boxes from that window. # postWorker
   Do the checks required by the labels and then put them in correct chute # postWorker
   So what are the labels? # protagonist
   ->taskExplain
* Leave
  -> hallway

=taskExplain
There are: animal, handle with care and express. # postWorker
* Lets go
   -> taskExecute
* What I do with animals?
   For animals check that the transition sedation is working. # postWorker
   Then if it is not put the animal to sleep. # postWorker
   How do I do that? # protagonist
   By applying the neurotoxin from that cabin. # postWorker
   That seems dangerous and not that sedative # protagonist
   Look, this place is busy and if the sender does a failure in packaging I will get creative to keep this place running smooth # postWorker
   ** object
       It does seem like the animals are wanted alive at their destination. # protagonist
       Look, the zoology department already does a lot of heavy packages. # postWorker
       So I will choose to interpret that they are meaning for the animals to get taxidermisised. # postWorker
       If you have a problem with that I can arrange for you to find a bear in your bed. # postWorker
       *** Nope
       *** I would rather have a antilope in my car
            You just got upgraded to jaguar on your deck. # postWorker
            ~ post_revenge=true
       ---
   ** when in Rome...
   --
   We don't have infinite supplies so don't use up more of the stuff than needed. # postWorker
* What do I do with "handle with care"?
   We are running low on idle hands and the chemistry deparment has gotten sloppy with their labeling # postWorker
   So we can only afford to ship with silk gloves those that really need it # postWorker
   To be honest I don't think the chemists would mind if some of the packages got lost if even some of them got throught # postWorker
   The packages that actually can be thrown around you can put in 'usual treatment' # postWorker 
   and the packges that you know can not be thrown around you pur in 'snail pace' # postWorker
   How do I determine what can take what? # protagonist
   I don't really know and I don't really care. # postWorker
   But no opening up those packages. # postWorker
* What do I do with 'express'?
   Just get them to their destination as fast as possible. # postWorker
   This place is so clogged that any packect moving is better than none. # postWorker
   But the more the merrier. # postWorker
-
Are you ready to begin? # postWorker
* Yes
    ->taskExecute
* What were the labels again?
   ->taskExplain
* This is too complex, I am leaving
   -> hallway

=questioning
+ Alibi
     Where were you at the time of the murder? # protagonist
    {post_task==false:
          If you have got time to blabber you have got time to sort the boxes # postWorker
          -> task
    }
    I was here sorting boxes # postWorker
    -> questioning
+ Motive
    Did you get along with the murder victim? # protagonist
    {post_task==false:
          If you have got time to blabber you have got time to sort the boxes # postWorker
          -> task
    }
    I knew his address and they always glued their stamps straigth so we are square. # postWorker
    -> questioning
+ Guilt
    Did you do the murder? # protagonist
    {post_task==false:
          If you have got time to blabber you have got time to sort the boxes # postWorker
          -> task
    }
    Maybe if some of these boxes contain bombs. But I have not intentionally packaged any boms, so no. # postWorker
   -> questioning
* Leave
   -> hallway


=taskExecute
You go get {a|yet another} box from the sorting chute. # narration
~ post_box_label="{~animal|handle with care|express}"
~ post_box_label=coherentLottery("box_label")
{post_box_label=="animal":
          ~ post_cat_up = true
          ~ splitWorld("post_cat_up")
}
{post_box_label=="handle with care":
          ~ post_probe=true
          ~ post_bomb_armed=coherentLottery("bomb_fuse") // {~true|false}
          ~ post_probe=false
}
{post_box_label=="express":
          ~ post_china=false
          ~ post_wall_skin=false
          ~ post_wall_meat=false
          ~ post_wall_stone=false
}
The label on it reads "{post_box_label}"# narration


+ open the box
    ->catThings

+ put the box in the maybe crush machine
  -> crushingExploration
+ put the box in the superior siege engine
   -> wallBanging
+ go check on whether the work is enough
  -> box_scoring

=catThings
    {post_box_label=="handle with care":
            {post_bomb_armed==true:
                 This one is whirling rather loudly. #narration
                 An explosion throws you back to the wall. # narration
                That level of care was not enough for you to continue living. # narration
                You die. # narration
                -> END
            -else:
                This cat seems to be rather fat. # narration
                Looking closer it is not a cat at all. # narration
                It seems to be some sort of chemical device that could generate gas in a very small amount of time. # narration
                You close the lid before the supervisor explodes about looking into boxes you are not supposed to.. # narration
            }
    }
    {post_box_label=="animal":
           ->CatHandling
    }
    {post_box_label=="express":
          Oh that is interesting # narration
          No wonder they want this delivered fast # narration
          + What is in the box?
                   You would like to know wouldn't you#program
                   Unfortunately your character has already looked inside#program
                   So they don't have any reason to look again#program
                   -> taskExecute
          + I want to oppose them. Up to snail mail it goes
                   If it is so important they can afford to wait for it to arrive #narrative
                   -> taskExecute
    }
    ->taskExecute

=CatHandling
            {post_cat_up==true:
                A cat is whirling inside the box # narration
            -else:
               A cat laying on the bottom # narration
            }

           + {post_neurotoxin>0}apply neurotoxin
                     ~ post_neurotoxin = post_neurotoxin - 1
                     {post_cat_up:
                            The cat goes limb and falls into the box. # narration
                     }
                     {critter==true:
                               You might as well have used a chainsaw to destroy that pussy. # narration
	               {guilty=="protagonist":
                                        You take 2 points # program
                                        Two points of what? # protagonist
                                        ...#program
                               }
                     }
                    ~ post_cat_up=false
                    ~ post_cat_dead=true
                    {post_neurotoxin<=0:
                            That was the last neurotoxin ampule. # narration
                    }
           + apply chloroform
                   {post_cat_up==true:
                             The cat swirls into a small ball that periodically buffs and deflates. # narration
                             ~ post_cat_up=false
                   }          
          + close box
                  This one is good to go. # narration
          -
          {post_cat_up==false:
                      ~ post_task_score=post_task_score+1
          -else:
                      ~ post_cat_error=post_cat_error+1                      
          }
          ->taskExecute


=crushingExploration
    You send a probe to test the condition of the box # narration
    ~splitWorld("post_probe")
    {post_probe==true:
          {post_bomb_armed==true:
                     Machine lets out a pretty loud thud. # narration
                     But you are safe from actual harm. # narration
                     ~ post_probe=false
                     ~ post_bomb_exploded=true
          }
    }
    ~splitWorld("post_probe")
    You wait for the probe to emerge from the tester # narration
    {post_probe==true:
               The probe came out of the machine at an angle. # narration
    -else:
               The probe came ouf of the machine straight.#narration
    }
    {post_bomb_exploded==true:
              The machine spits out some bits of charred cardboard bits. #narration
              This is all that is left of the precious postal package.#narration
    }
    + Put box in 'snail pace'
	{post_bomb_armed==true:
		~ post_task_score=post_task_score+1
	}
	{post_bomb_exploded==true:
		~ post_bomb_error=post_bomb_error+1
	-else:
		~post_bomb_burden=post_bomb_burden+1
	}
    + Put box in 'usual treatment'
	{post_bomb_armed==false:
		~ post_task_score=post_task_score+1
	-else:
		~ post_bomb_error=post_bomb_error+1		
	}
	{post_bomb_exploded==true:
		~ post_bomb_error=post_bomb_error+1
	}
    + Box, what box? There was never any box here //incinerator voices
	{post_bomb_exploded==false:
		You discretely light the cardboard box on fire # narration
	}
   + {post_bomb_exploded==false}Put box back into the maybe crush machine
	-> crushingExploration
    -
    ->taskExecute 



=wallBanging
You see the drone loading bay beyond reinforced plastic transparent wall. # narration
{post_china==false:
       It keeps the murder bots away but also makes giving them any deliverables tricky. # narration
-else:
      The drones seem busy buzzing around a box. # narration
}
+ {post_china==true}Marvel at your accomplishments
        Huh, I guess more dakka is always a solution. #narration
        Maybe I should paint it red next time. # narration
+{post_china==false}Launch
    // request tunnel post_china 0.2
         ~ splitWorld("post_wall_skin")
         You set the box into the cup of the supreme kinetic applier # narration
         ~ splitWorld("post_wall_meat")
         With the release leaver the box starts to pick up speed # narration
         ~ splitWorld("post_wall_stone")
         You can almost hear the box whistle through the air # narration
         The packet makes contact with the wall # narration
         {post_wall_skin==true:
                {post_wall_meat==true:
                        {post_wall_stone==true:
                                  post_china=true // amplitude split of 8
                        }
                 }
         }
         ~ splitWorld("post_wall_stone")
         ~ splitWorld("post_wall_meat")
         ~ splitWorld("post_wall_skin")
         {post_china:
                And disappears. # narration
         -else:
               and bounces of it. # narration
               {|||||This would be so much more easier if they had like an opening to faciliate travel in the wall||}
         }
         -> wallBanging
+Go get new box
     {post_china==true:
         ~ post_task_score=post_task_score+1
     }
     ->taskExecute

=box_scoring
I am done. Now will you answer my questions? # protagonist
Lets see whether you are in fact done # postWorker
{post_task_score>10:
	{post_task_score<(post_cat_error+post_bomb_error)*2:
		Yeah it seems you are done. postWorker
		~ post_task=true
	}
	{post_cat_error+post_bomb_error<0:
                            And you were flawless about it too. # postWorker
                }
	->questioning
-else:
               We have not yet hit our quatas. I ain't answering to slackers anything # postWorker
	* Go back to work
	     ->taskExecute
	* Leave
                     -> hallway
}