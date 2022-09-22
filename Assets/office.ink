=== office ===
There is something like a statue in the corner of the room. Oh, wait. It breathes!
+ [Engage]
    ->Butler
+ Look at the table
    -> officeTable
+ Go back
    -> hallway


= officeTable
On the office table lays a heavy registry book. Someone seems to have touched it recently.
+ Open registry
    You see a list of staff and students in the university
    -> registry

= registry
        +   Annette Dias
            Professor of Education
            -> registry
        +  Bernard Tar        
            Professor of mathemathics.
             -> registry
        + Chloe Greenberg
            Student of Water and Environmental Engineering
             -> registry
        + Ciar Portelli       
        Student of Water and Environmental Engineering
             -> registry
        + {guilty!="protagonist"}Dalton Devin        
        Student of New Media
             -> registry
        + Deep Tamura         
        Professor of Chemistry.
             -> registry
        + Enrico Mwangi
             -> registry
        Professor of Mathemathics.
             -> registry
        + Firuza Dwight       
        Student of Chemical Engineering 
             -> registry
        + {guilty!="protagonist"}Graziano Waltz      
        Professor of Chemical Engineering.
             -> registry
        + {guilty=="protagonist"}Gerry Woodlet      
        Professor of Chemical Engineering.
             -> registry
        + Hroderich Duncan    
        Student of Quantum Technology.
             -> registry
        + Iou Pond            
        Student of Data Science
             -> registry
        + Isidora Harlan      
        Student of Digital systems and Design
             -> registry
        + Jetta Ravenna       
        Student of Computational Engineering
             -> registry
        + Kristel Cohen       
        Student of Design
             -> registry
        + {guilty!="protagonist"}Liva Quirke         
        Student of Economics                
             -> registry
        + Marje Ott           
             -> registry
        Student of Architecture
        + Merry Bieber        
        Student of Zoology        
             -> registry
        + Nyree Velazquez     
        Student of Electrical Engineering
             -> registry
        + Piia Marini         
        Professor of Zoology    
             -> registry
        + Rab Aikema          
        Student of Ecology      
             -> registry
        + Rolf Olivier        
        Student of Finances
             -> registry
        + Runa Coello         
        Student of Philosophy                       
             -> registry
        + Silja Das           
        Student of Mathemathicks                    
             -> registry
        + Simon Baumgartner   
        Student of Law
             -> registry
        + Tomislava Dreher    
        Professor of Digital Art
             -> registry
        + Urvi Belluomo       
        Student of Medicine
            -> registry
        + Vasu Reis           
        Professor of Computer Science
             -> registry
        + Vidya Chalupa       
        Student of Creative Sustainability
             -> registry
        +  Zdravka Brauer      
        Student of Nanotechnology
             -> registry
        + Close registry 
            -> officeTable
+ Return to hallway
  -> hallway