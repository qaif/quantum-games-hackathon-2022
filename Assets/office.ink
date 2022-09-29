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
+ Open registry
    You see a list of staff and students in the university # narration
    -> registry


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