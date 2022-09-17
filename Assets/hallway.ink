INCLUDE murder_bathroom.ink

=== hallway ===

The hallway seems empty. There is a door to the cleaning cellar,
a door to a classroom and a door to the auditorium.
In addition to the usual facilities.
    + Enter cleaning cellar
        -> cleaning_cellar
    + Enter classroom
      -> classroom
    + Enter auditorium
        ->auditorium 
    + Enter toilet
        ->MurderBathroom 
    
    
    
    
    
    === classroom ===
    The classroom seems empty
    + Return to hallway
    -> hallway
    
    === auditorium ===
    The auditorium seems empty
    ...except for a lone figure jumping up and down
    + [Engage]
        -> Rascal
    + Return to hallway
    -> hallway
