INCLUDE student.ink

=== hallway ===

The hallway seems empty. There is a door to the cleaning cellar,
a door to a classroom and a door to the auditorium.
    + Enter cleaning cellar
        -> cleaning_cellar
    + Enter classroom
      -> classroom
    + Enter auditorium
        ->auditorium 
    
    
    
    
    
    === classroom ===
    The classroom seems empty
    + Return to hallway
    -> hallway
    
    === auditorium ===
    The auditorium seems empty
    ...except for a lone figure jumping up and down
    + [Engage]
        -> Student
    + Return to hallway
    -> hallway
