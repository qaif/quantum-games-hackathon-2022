import pygame

gameTitle = "Verona 2049" # game title
screenSize = (1024, 768)  # screen size

# =================== GAME SETTINGS ========================

minBit = 1          # total min bit selection
maxBit = 15         # total max bit selection
currentBit = 5

showConfig = True   # to show the keyboard guide
#showConfig = False

testing = True      # flag for testing or not
#testing = False
phase = 4           # config for setting game phases

# =========== GAME SETTINGS FOR NEW GAME ======================

remainingHearts = 3     # to check the remaining hearts

starting_timer_minute = 5   # starting timer
starting_timer_seconds = 0

timer_minute = 5        # current timer
timer_seconds = 0

# refresh on main menu
def refresh_new_game():
    remainingHearts = 3

    starting_timer_minute = 5
    starting_timer_seconds = 0

    timer_minute = 5
    timer_seconds = 0

    refresh_after_loop()

# ====================== GLOBAL PARAMETERS NEED TO BE REFRESH AFTER LOOP ======================

selectedBit = 0     # selected # of bit
secret_key = ""     # created secret_key

romeo_bits = []     # romeo bits
romeo_bases = []    # romeo bases
romeo_key = []    # romeo bases

juliet_bits = []   # juliet bits
juliet_bases = []   # juliet bases
juliet_key = []    # romeo bases

# refresh on phase 0
def refresh_after_loop():
    selectedBit = 0
    secret_key = ""

    romeo_bits = []
    romeo_bases = []
    juliet_bases = []

# ==================  Measuring keyboard settings ========================
keyboard_bit_0 = pygame.K_d
keyboard_bit_1 = pygame.K_f
keyboard_base_x = pygame.K_j
keyboard_base_z = pygame.K_k

# piano composition by Schubert, not copyrighted
music_file="assets/music/Schubert---Impromptu-Op.-90--No.-3_AdobeStock_501349563.wav"

# ================== global colors ==============================
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