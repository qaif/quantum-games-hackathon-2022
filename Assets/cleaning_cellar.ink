=== cleaning_cellar ===

= aEntersACleaning
{protagonist_name} enters a cleaning cellar.
-> CellarItems

= CellarItems
On the floor, besides all the bottles of cleaning liquids, brushes and swabs
is a book with the name "Bernard Tar", 
an earring, a hat and a feather.
-> CellarActions

= CellarActions
        + Open book
            -> book.page1
        + Inspect earring
            The earring seems a spiral made of golden, with a small amethyst in the center.
            -> CellarActions
        + Inspect hat
            The hat is brown, with a broad brim.
            -> CellarActions
        + Inspect feather
            The feather is large and coloured in brilliant red and blue.
            -> CellarActions
        + Return to hallway
            -> hallway