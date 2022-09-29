INCLUDE murder_bathroom.ink

=== hallway ===

The hallway seems empty. There is a door to the cleaning cellar, # narration
a door to a classroom, a wide opening to a cafeteria and a door to the auditorium. # narration
In addition to the usual facilities. # narration
{priority_note==true:
   Better get started with that toilet. # narration
}
    + {priority_note==false} Enter cleaning cellar
        -> cleaning_cellar.aEntersACleaning
    + {priority_note==false} Enter classroom
      -> classroom
    + {priority_note==false} Enter auditorium
        ->auditorium 
    + {priority_note==false} Enter office
        ->office
    + {priority_note==false} Enter post station
        -> CatDelivery
    + Usual facilities
        -> Facilities

=Facilities
    {guilty=="merry":
    That is funny. I thought I cleaned up this end of the hallway yesterday. # narration
    }
    + Enter toilet
        ->MurderBathroom
    + {priority_note==false} Enter hall of fame
       -> HallOfFame
    + {priority_note==false} Enter cafeteria
       -> Coffee.coffeetable
    + Unusual facilities
       -> hallway
    
    
    
    
    === classroom ===
    The classroom seems echoing, but there is someone behind a high bookstack. # narration
    + [Engage]
        -> Runa_cat
    + Return to hallway
    -> hallway
    
    === auditorium ===
    The auditorium seems empty # narration
    ...except for a lone figure jumping up and down. #narration
    + [Engage]
        -> Rascal
    + Return to hallway
    -> hallway
