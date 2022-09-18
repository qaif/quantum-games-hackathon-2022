INCLUDE murder_bathroom.ink

=== hallway ===

The hallway seems empty. There is a door to the cleaning cellar,
a door to a classroom, a wide opening to a cafeteria and a door to the auditorium.
In addition to the usual facilities.
    + Enter cleaning cellar
        -> cleaning_cellar.aEntersACleaning
    + Enter classroom
      -> classroom
    + Enter auditorium
        ->auditorium 
    + Enter office
        ->office
    + Usual facilities
        -> Facilities

=Facilities    
    + Enter toilet
        ->MurderBathroom
    + Enter hall of fame
       -> HallOfFame
    + Enter cafeteria
       -> Coffee
    + Unusual facilities
       -> hallway
    
    
    
    
    === classroom ===
    The classroom seems echoing, but there is someone behind a high bookstack
    + [Engage]
        -> Runa_cat
    + Return to hallway
    -> hallway
    
    === auditorium ===
    The auditorium seems empty
    ...except for a lone figure jumping up and down
    + [Engage]
        -> Rascal
    + Return to hallway
    -> hallway
