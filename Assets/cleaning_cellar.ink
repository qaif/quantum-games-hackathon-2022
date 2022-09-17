=== cleaning_cellar ===

= aEntersACleaning
{protagonist_name} enters a cleaning cellar 
and finds a professor’s cadaver. 
-> CleaningItems

= CleaningItems
In the same cellar is a book with the name "B", 
an earring, a hat and a feather'
//: + Pick up earring
//    You picked up the earring.
//+ Pick up hat
//    You picked up the hat.
//+ Pick up feather
//    You picked up the feather.
+ Open book
    You read a wall of text
    -> CleaningItems
-> body