=== office ===
There is something like a statue in the corner of the room. Oh, wait. It breathes! # narration
+ [Engage]
    ->Butler
+ Look at the table
    -> officeTable
+ Look at small wall fixture
    -> keypad
+ Go back
    -> hallway


= officeTable
~johnny_points=0
On the office table lays a heavy registry book. Someone seems to have touched it recently. # narration
There is also a phone on the table. # narration
You could also go throught the drawers to find skeletons # narration
+ Open registry
    You see a list of staff and students in the university # narration
    -> registry
+Phone
    ->Phone
+Drawers
    {skeleton_key==true:
           With the key you get access to all the skeletons. # narrative
           Because that is totally what being a skeleton key means # narrative
           ->TeleportReceive
    -else:
           Hmmm the sensitive papers are being protected by a lock # narrative
    }
+Disengage
-
->officeTable

=Phone
It is a bit weird that it not mobile but tachyonic phones are a bit more expensive to make that way. # narration
It is standard issue and quite ordinary. # narration
{phone_cool_off==0:
   The phone is ringing # narration
}
{phone_cool_off>0:
   ~phone_cool_off=phone_cool_off+1
}
+ {phone_cool_off<=0}Answer it
    {phone_phrase} # protagonist
    Weirdly that is what you hear from the phone # narrative
    In a panic you slam the phone down # narrative
    That must be a really good mimic. # narrative
    ~phone_cool_off=phone_cool_off+1
+ {phone_cool_off>2}Dial
    Bored you fiddle with the phone  # narration
    -> phone_wait
+ {phone_cool_off<=0}Let it ring
    ~ phone_wait_time=phone_wait_time+1
    briiiing! briiiing! It is making quite a noise # narration
+ Search the underside of the phone
    There seems to be nothing here # narration
    -> Phone
+ Disassemble phone
    You fail to get any work done on the seams # narration
    It is quite solid work
+ Walk away
     ->officeTable
-
->Phone


=TeleportReceive
You find a strange communication device that seems to be so new you don't even know what it is. # narration
Please insert anti-correlation source # written
Well that is one hole in the device #narrative
Please input measured season # written
The concepts are just so weird. There is a dial and a confirm button next to that one # narrative
+ insert item into hole
      ++ Erm, this bomb that I am carrying?
              This was not the safest choice # narrative
              -> resolution.Demise
      ++ Maybe not stick your tools into unknown openings
            You step back to wonder about the interface # TeleportReceive
+ Make a selection with the dial
      So which season it shall be?
      ++ Spring
      ++ Summer
      ++ Fall
      ++ Winter




=phone_wait
{phone_wait_time==0:
       You hear the connection sound and blurp the first thing that comes to your mind # narration
       {phone_phrase} # protagonist
       Hey that is not fun! They immediately hang up on the call. # narration
       ~ phone_phrase = coherentLottery("phone")
       ~ phone_cool_off = 0
- else:
       Come on pick up the phone mystery receiver # narration
       ~ phone_wait_time = phone_wait_time-1
}
->Phone

=keypad
~ passcode=false
It is a small keypad. # narration
You have absolutely no way to know what is its passcode. # narration
{protagonist_name=="Stanley":
Like I wouldn't remember # protagonist
}
+ {passcode==true} Lets see what is inside
      There is nothing inside. # narration
      I guess the real prize is the references we got along the way. # narration
+ Try to figure it out a bit longer
    ->keypad
+ Leave
    -> office

= registry
        ~ johnny_points=johnny_points+1
        {johnny_points>8:
              Are we seriously doing this? # program
        }
        {johnny_points>12:
              You are supposed to be a detective and not a text-crawler. # program
        }
        {johnny_points>16:
              All work and no play makes johnny a dull boy. # program
              You know what games are for? PLAYING. # program
        }
        +   Annette Dias
            Professor of Education # written
            -> registry
        +  Bernard Tar       
            Professor of mathemathics. # written
             -> registry
        + Chloe Greenberg
            Student of Water and Environmental Engineering # written
             -> registry
        + Ciar Portelli       
        Student of Water and Environmental Engineering # written
             -> registry
        + {guilty!="protagonist"}Dalton Devin        
        Student of New Media # written
             -> registry
        + Deep Tamura         
        Professor of Chemistry # written
             -> registry
        + Enrico Mwangi
        Professor of Mathemathics # written
             -> registry
        + Firuza Dwight       
        Student of Chemical Engineering # written
             -> registry
        + {guilty!="protagonist"}Graziano Waltz
        Professor of Chemical Engineering # written
             -> registry
        + {guilty=="protagonist"}Gerry Woodlet      
        Professor of Chemical Engineering # written
             -> registry
        + Hroderich Duncan    
        Student of Quantum Technology. # written
             -> registry
        + Iou Pond            
        Student of Data Science # written
             -> registry
        + Isidora Harlan      
        Student of Digital systems and Design # written
             -> registry
        + Jetta Ravenna       
        Student of Computational Engineering # written
             -> registry
        + Kristel Cohen       
        Student of Design # written
             -> registry
        + {guilty!="protagonist"}Liva Quirke         
        Student of Economics # written
             -> registry
        + Marje Ott 
             -> registry
        Student of Architecture # written
        + Merry Bieber        
        Student of Zoology # written
        {lucan_cure==true:
             ~ lucan_points= lucan_points +1
        }
        {lucan_formula==true:
             ~ lucan_points= lucan_points +1
        }
        {lucan_extort==true:
             ~ lucan_points= lucan_points +1
        }
        {lucan_points>2:
              Who would have thought that zoology would be so close to astrology. # narration
              ~ lucan_identity=true
        }
             -> registry
        + Nyree Velazquez     
        Student of Electrical Engineering # written
             -> registry
        + Piia Marini         
        Professor of Zoology # written
        {lucan_extort==true:
             While lucration from some liquids could be a crime, I am going to give this a pass while the murder investigation is ongoing. # narration
        }
             -> registry
        + Rab Aikema          
        Student of Ecology # written
             -> registry
        + Rolf Olivier        
        Student of Finances # written
             -> registry
        + Runa Coello         
        Student of Philosophy # written
             -> registry
        + Silja Das           
        Student of Mathemathics # written
             -> registry
        + Simon Baumgartner
        Student of Law # written
             -> registry
        + Tomislava Dreher    
        Professor of Digital Art # written
             -> registry
        + Urvi Belluomo       
        Student of Medicine # written
            -> registry
        + Vasu Reis           
        Professor of Computer Science # written
             -> registry
        + Vidya Chalupa       
        Student of Creative Sustainability # written
             -> registry
        +  Zdravka Brauer      
        Student of Nanotechnology # written
             -> registry
        + Close registry 
            -> officeTable
+ Return to hallway
  -> hallway