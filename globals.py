world = None

gameTitle = "Verona 2049"
minBit = 5
maxBit = 10
currentBit = 5
selectedBit = 0
screenSize = (1024, 768)

# piano composition by Schubert, not copyrighted
music_file="assets/music/Schubert---Impromptu-Op.-90--No.-3_AdobeStock_501349563.wav"

DARK_GREY = (50,50,50)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
MUSTARD = (209,206,25)
RED = (255,0,0)

# list of letters that can be randomly chosen to encrypt
letters=[
    "Parting is such sweet sorrow.",
    "But soft, what light through yonder window breaks? It is the East, and Juliet is the sun.",
    "My bounty is as boundless as the sea, My love as deep. The more I give to thee, The more I have, for both are infinite.",
    "Did my heart love till now? Forswear it, sight, For I ne'er saw true beauty till this night.",
    "Under love's heavy burden do I sink.",
    "Love goes toward love as schoolboys from their books, But love from love, toward school with heavy looks.",
    "O, speak again, bright angel, for thou art As glorious to this night, being o'er my head, As is a winged messenger of heaven.",
    "What's in a name? That which we call a rose By any other name would smell as sweet.",
    "Good night, good night! parting is such sweet sorrow, that I shall say good night till it be morrow.",
    "Did my heart love till now? forswear it, sight! For I ne'er saw true beauty till this night.",
    "Love is a smoke raised with the fume of sighs; Being purged, a fire sparkling in lovers’ eyes",
    "With love’s light wings did I o’erperch these walls, For stony limits cannot hold love out.",
    "One fairer than my love? the all-seeing sun Ne’er saw her match since first the world begun.",
    "This bud of love, by summer's ripening breath, May prove a beauteous flower when next we meet.",
    "You are a lover. Borrow Cupid's wings And soar with them above a common bound.",
    "If love be blind, love cannot hit the mark.",
    "Love moderately. Long love doth so. Too swift arrives as tardy as too slow.",
    "For stony limits cannot hold love out, And what love can do that dares love attempt.",
]