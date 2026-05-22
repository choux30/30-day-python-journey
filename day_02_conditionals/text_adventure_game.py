has_catalog_card = False
has_muffin = False
has_photocopier_receipt = False
inspected_photocopier = False


game_title = "The Case of the Vanishing Footnote"
border = ("-----------------------------------")
print(border)
print(game_title)
print(border)

#opening
print()
print("Welcome to The Case of the Vanishing Footnote.")
print()
player_name = input("Hello, Detective. What is your name? ").strip()
print()
print(f"Detective {player_name}, your investigation begins.")
print()
next_scene = input("Press Enter to continue ").strip()
print()
print()
print(border)
print("The Case")
print(border)
print()
print("The Grand Municipal Library of Mildly Alarming Knowledge has a problem.")
print()
print('At precisely 9:03 this morning — an hour the library insists is "basically noon" for books — the final page of a rare manuscript disappeared.')
print()
print("The book is called A Beginner's Guide to Advanced Confusion, and nobody understands it well enough to know whether the missing page is important. Naturally, this has caused panic.")
print()
print("The head librarian, Ms. Widdershins, has hired you because you were standing nearby and looked investigatory.")
print()
print("She hands you a pencil, a visitor badge, and a look that suggests failure will be shelved under Tragedy.")
print()
scene_1 = input("Press Enter to continue ").strip()


#Scene 1
print()
print()
print(border)
print("The Main Reading Room")
print(border)
print()
print("You stand in the main reading room.")
print()
print("The library is silent, except for the faint hum of fluorescent lights and the distant sound of someone being disappointed by a printer.")
print()
print("Ms. Widdershins watches you over the top of her glasses.")
print()
print('"You may begin," she says. "Please do not bleed on the encyclopedias. They are already indexed."')
print()
choice_1 = input("Press Enter to continue ").strip()
print()
print("What do you investigate first?")
print()
print("1. Question the head librarian\n2. Search the card catalog\n3. Inspect the snack table")
print()

while True:
    choose_choice_1 = input("The detective chooses option number... ").strip()

    if choose_choice_1 == "1":
        print("Ms. Widdershins adjusts her glasses with the force of a legal objection.")
        print()
        print('"The book was last seen in the Rare Books Room," she says. "The professor, the photocopier, and a suspiciously literate cat were all nearby."')
        print()
        print("She pauses.")
        print()
        print('"I do not accuse the cat. I merely observe that it owns a fountain pen."')
        break

    elif choose_choice_1 == "2":
        print("You search the card catalog.")
        print()
        print("After some dramatic drawer-opening, you find a yellowed card labeled:")
        print()
        print("A Beginner's Guide to Advanced Confusion\nSee also: TROUBLE, PAPERCLIPS, MACHINES WITH AMBITION")
        print()
        print("You take the catalog card.")
        print()
        print("It feels judgmental")

        has_catalog_card = True
        break

    elif choose_choice_1 == "3":
        print()
        print("You inspect the snack table with professional seriousness.")
        print()
        print("There is a blueberry muffin, a cold cup of tea, and a note that says:")
        print()
        print("DO NOT FEED THE REFERENCE DESK.")
        print()
        print("You take the muffin, because every great detective understands the value of evidence you can eat.")

        has_muffin = True
        break

    else:
        print()
        print("That is not one of the choices. The library records your indecision in a small red notebook.")

print()
scene_2 = input("Press Enter to continue ").strip()

print()
print()
print(border)
print("The Rare Books Room")
print(border)

print()
print("You enter the Rare Books Room.")
print()
print("The air smells like dust, old paper, and the quiet confidence of objects that know they are expensive.")
print()
print("On a velvet-covered table lies A Beginner's Guide to Advanced Confusion.")
print()
print("The book is open. Its final page is missing.")
print()
print("A small sign beside it reads:")
print()
print("PLEASE DO NOT PANIC NEAR THE MANUSCRIPTS.")

print()
print("What do you examine?")
print()
print("1. Examine the damaged book\n2. Search the floor\n3. Interrogate the reading chair")
print()

while True:
    choice_2 = input("The detective chooses option number... ").strip()

    if choice_2 == "1":
       print()
       print("You examine the book.")
       print()
       print("The final page has been removed with surprising neatness. A bent paperclip rests near the spine, trying to look innocent and failing.")
       print()
       print("You make a note:")
       print()
       print("The thief was careful, organized, and possibly office-supply adjacent.")
       break

    if choice_2 == "2":
        print()
        print("You search the floor.")
        print()
        print("Under the table, you find a tiny receipt from the library photocopier.")
        print()
        print("It says:")
        print()
        print("1 copy made.\nOriginality fee waived.\nConscience not included.")
        print()
        print("This seems important, unless the universe is being sarcastic again.")

        has_photocopier_receipt = True
        break

    if choice_2 == "3":
        print()
        print("You interrogate the reading chair.")
        print()
        print("The chair says nothing, which is suspicious, but also normal for a chair.")
        print()
        print("After several seconds of intense questioning, it creaks in a way that suggests someone heavy with guilt sat here recently.")
        print()
        print("Or someone who enjoyed soup.")
        break

    else:
        print()
        print("That is not one of the choices. The library records your indecision in a small red notebook.")

print()
scene_3 = input("Press Enter to continue ").strip()

print()
print("The suspects are gathered near the Reference Desk.")
print()
print("Professor Crumbly is clutching a tower of notes.")
print()
print("The photocopier is humming in a nervous and legally significant way.")
print()
print("A gray cat sits on the dictionary shelf, pretending not to know the alphabet.")

print()
print("Who or what do you investigate?")
print()
print("1. Talk to Professor Crumbly\n2. Inspect the photocopier\n3. Follow the trail of bookmarks")

print()
while True:
    choice_3 = input("The detective chooses option number... ").strip()

    if choice_3 == "1":
        print()
        print("Professor Crumbly gasps before you even ask a question.")
        print()
        print('"I did not steal the page," he says. "I merely disagreed with it academically."')
        print()
        print("He waves a stack of notes in the air.")
        print()
        print('"The conclusion was weak. The argument was flimsy. The punctuation was emotionally reckless."')
        print()
        print('He sneezes when he says the word "footnote."')
        print()
        print("It may be an allergy. It may be guilt. It may be academia.")
        break

    elif choice_3 == "2":
        print()
        print("You inspect the photocopier.")
        print()
        print("Its display screen flashes:")
        print()
        print("I AM ONLY A HUMBLE MACHINE.")
        print("PLEASE IGNORE OUTPUT TRAY.")
        print()
        print("The output tray is empty, except for a smear of toner and a tiny corner of torn paper.")
        print()
        print("The photocopier makes a sound like someone trying to whistle without lips.")

        inspected_photocopier = True
        break

    elif choice_3 == "3":
        print()
        print("You follow a trail of tiny paper bookmarks.")
        print()
        print("They lead behind a shelf labeled:")
        print()
        print("BOOKS THAT ARE MOSTLY APOLOGIZING")
        print()
        print("Behind the shelf, you discover a narrow door marked:")
        print()
        print("ARCHIVE")
        print("Authorized People, Accidental Geniuses, and Cats Only")
        break

    else:
        print()
        print("That is not one of the choices. The library records your indecision in a small red notebook.")

print()
scene_4 = input("Press Enter to continue ").strip()

print()
print("You stand before the Archive door.")
print()
print("It is made of old oak, brass hinges, and the kind of institutional stubbornness usually found in tax forms.")
print()
print("A small slot sits beside the handle.")
print()
print("Above it, a sign reads:")
print()
print("INSERT AUTHORIZATION OR CONVINCING EXPLANATION.")

print()
print("How do you try to enter the Archive?")
print()
print("1. Slide the catalog card into the door slot")
print("2. Ask Ms. Widdershins for help")
print("3. Kick the door heroically")
print()

while True:
    choice_4 = input("The detective chooses option number... ").strip()

    if choice_4 == "1":
        if has_catalog_card:
            print()
            print("You slide the catalog card into the slot.")
            print()
            print("The door sighs, possibly from age, possibly from disappointment in modern security.")
            print()
            print("Then it swings open.")
            print()
            print("You step into the Archive.")
            break

        else:
            print()
            print("You pat your pockets and realize you do not have a catalog card.")
            print()
            print("The door remains shut with the smugness of a door that has tenure.")
            print()
            print("Ms. Widdershins appears from nowhere.")
            print()
            print('"Improvisation is not a key," she says.')
            print()
            print("After a long stare, she unlocks the door anyway.")
            print()
            print('"Try not to breathe dramatically near the old newspapers."')
            print()
            print("You step into the Archive.")
            break

    elif choice_4 == "2":
        print()
        print("You ask Ms. Widdershins for help.")
        print()
        print("She narrows her eyes.")
        print()
        print('"Very well," she says. "But if anything screams, alphabetize it first."')
        print()
        print("She unlocks the Archive door.")
        print()
        print("You step inside.")
        break

    elif choice_4 == "3":
        print()
        print("You kick the door heroically.")
        print()
        print("The door, being made of oak and institutional resentment, wins.")
        print()
        print(
            "A silent alarm summons three librarians, one rolling cart, and a pamphlet titled So You Have Made A Poor Decision.")
        print()
        print("You are politely but firmly removed from the Archive.")
        print()
        print("ENDING: Shelved Under Bad Ideas")
        print()
        print("You did not solve the mystery.")
        print()
        print("Your visitor badge is revoked, laminated, and placed in a folder labeled Examples.")

        raise SystemExit

    else:
        print()
        print("That is not one of the choices. The library records your indecision in a small red notebook.")

print()
scene_5 = input("Press Enter to continue ").strip()

print()
print("Inside the Archive, the shelves rise into darkness.")
print()
print("The missing page sits on a central table beneath a glass dome.")
print()
print("Beside it are three things:")
print()
print("A stack of Professor Crumbly's notes.")
print("A trail of toner dust.")
print("A single gray cat hair arranged with suspicious elegance.")
print()
print("Ms. Widdershins folds her arms.")
print()
print(f'"Well, Detective {player_name}?"')
print()
print("The suspects wait.")
print()
print("Professor Crumbly looks offended.")
print("The photocopier looks plugged in.")
print("The cat looks above the law.")

print()
print("Who do you accuse?")
print()
print("1. Professor Crumbly")
print("2. The photocopier")
print("3. The library cat")
print()

while True:
    choice_5 = input("The detective chooses option number... ").strip()

    if choice_5 == "1":
        print()
        print("You point dramatically at Professor Crumbly.")
        print()
        print('"The professor stole the missing page!"')
        print()
        print("Professor Crumbly drops his notes, which scatter into twenty-seven footnotes and one sandwich recipe.")
        print()
        print("Ms. Widdershins examines your evidence.")
        print()
        print('"Detective," she says, "the professor is annoying. That is not the same as guilty."')
        print()
        print("Professor Crumbly nods proudly, as though this is the nicest thing anyone has said about him all week.")
        print()
        print("ENDING: False Accusation")
        print()
        print("You did not solve the mystery.")
        print()
        print("Professor Crumbly files a formal complaint, then adds six footnotes to it.")

        raise SystemExit

    elif choice_5 == "2":
        if has_photocopier_receipt or inspected_photocopier:
            print()
            print("You point at the photocopier.")
            print()
            print('"The photocopier stole the missing page!"')
            print()
            print("The room goes silent.")
            print()
            print("The photocopier beeps once.")
            print()
            print("Then twice.")
            print()
            print("Then it begins printing at the emotional speed of guilt.")
            print()
            print(
                "Out slides the missing final page, followed by three copies of an apology, one unsolicited newsletter, and a blurry image of what may be its conscience.")
            print()
            print("The photocopier confesses.")
            print()
            print('It wanted to create "original copies" and misunderstood both words.')
            print()
            print("Ms. Widdershins takes the final page and stamps your visitor badge with SOLVED.")
            print()
            print('"This stamp is rarely used," she says. "It may become difficult to live with."')
            print()
            print("ENDING: Case Closed")
            print()
            print("You solved the mystery of the vanishing footnote.")
            print()
            print("The library returns to normal, except for the photocopier, which is sent to Ethics Training.")

            raise SystemExit

        else:
            print()
            print("You point at the photocopier.")
            print()
            print('"The photocopier did it!"')
            print()
            print("The photocopier beeps with the confidence of an appliance that knows you have no paperwork.")
            print()
            print("Ms. Widdershins looks at you.")
            print()
            print('"An interesting theory," she says, in the tone people use for soup made of batteries.')
            print()
            print("The photocopier slowly prints a blank page.")
            print()
            print("Nobody can prove what it means, but everyone feels judged.")
            print()
            print("ENDING: Correct Hunch, Insufficient Evidence")
            print()
            print("You may have guessed the truth, but you did not prove it.")
            print()
            print("The case remains technically unresolved, which the library files under Annoying But Possible.")

            raise SystemExit

    elif choice_5 == "3":
        if has_muffin:
            print()
            print("You point at the library cat.")
            print()
            print('"The cat stole the page!"')
            print()
            print("The cat blinks slowly.")
            print()
            print("This is either a denial, a confession, or a review of your performance.")
            print()
            print("Then it notices the muffin in your pocket.")
            print()
            print("The cat leaps down, steals the muffin, and sits on the evidence box.")
            print()
            print("Ms. Widdershins sighs.")
            print()
            print('"The cat is suspicious," she says, "but also unionized."')
            print()
            print("ENDING: The Cat Wins")
            print()
            print("You did not solve the mystery.")
            print()
            print("You did, however, lose a muffin to a cat with excellent legal instincts.")

            raise SystemExit

        else:
            print()
            print("You point at the library cat.")
            print()
            print('"The cat stole the page!"')
            print()
            print(
                "The cat stares at you with the ancient disappointment of a creature that has watched humans invent meetings.")
            print()
            print("It knocks a bookmark off the table.")
            print()
            print("Ms. Widdershins picks it up and reads the tiny print.")
            print()
            print("It says:")
            print()
            print("NICE TRY.")
            print()
            print("ENDING: Outwitted By A Cat")
            print()
            print("You did not solve the mystery.")
            print()
            print("The cat remains free, smug, and probably in charge of the library budget.")

            raise SystemExit

    else:
        print()
        print("That is not one of the choices. The library records your indecision in a small red notebook.")

