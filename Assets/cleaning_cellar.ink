=== cleaning_cellar ===

= aEntersACleaning
{protagonist_name} enters a cleaning cellar. # narration
-> CellarItems

= CellarItems
On the floor, besides all the bottles of cleaning liquids, buckets, brushes and swabs # narration
is a book with the name "Bernard Tar", # narration
an earring, a hat and a feather. # narration
{lucan_borrow==true:
There are not enough feathers to pose a threat to anyones dignity. # narration
}
-> CellarActions

= CellarActions
        + Open book
            -> book.page1
        + Inspect earring
            The earring seems a spiral made of golden, with a small amethyst in the center. # narration
            -> CellarActions
        + Inspect hat
            The hat is brown, with a broad brim. # narration
            -> CellarActions
        + Inspect feather
            The feather is large and coloured in brilliant red and blue. # narration
            -> CellarActions
        + Inspect bucket
            You find a scarlet fish swimming in the bucket! # narration
            How unsual, this has to be a central clue to this mystery. # narration
            -> CellarActions
        + Return to hallway
            -> hallway