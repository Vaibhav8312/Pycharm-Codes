print("""                                I
                                  Y
   |                              T                              |
  .'.                           .' '.                           .'.
 (__ )                        _;-----;_                        (__ )
  |A|                       .':::::    '.                       |A|
 .===.                     /:::::::      \                     .===.
 |/  |                |   ::::::::        :   |                |/  |
 |/  |      |       ,' ', |:::::::        | ,' ',       |      |/  |
 |/  |     ( )     (:.___)\:::____________/(:.___)     ( )     |/  |
 |===|      H    I  |(_)V__)-------------(__V(_)|  I    H      |===|
 |/  |     |=|   Y_.----|  _______________  |----._Y   |=|     |/  |
 |/  |     |:|   | | __ | [,-------------,] | __ | |   |:|     |/  |
 |/  |     |:|   | |/  \| [|    _.-._    |] |/  \| |   |:|     |/  | 
 |===|     |:|   |'||  || [|   /  '::\   |] ||  ||'|   |:|     |===|
 |/  |     |:|   |_||__|| []  |    :::|  [] ||__||_|   |:|     |/  |
 |/  |     |:|   | | __ | []  |    :::|  [] | __ | |   |:|     |/  |
 |/  |     |:|   |.|/  \| []  |    :::|  [] |/  \|.|   |:|     |/  |
 |/  |     |:|   | ||  || []  |     ::|  [] ||  || |   |:|     |/  |
 |/__|_____|:|___| ||__||_[]__|_____::|__[]_||__||_|___|:|_____|/__|
|/    |-------------------------------------------------------|/    |
|/    |                                                       |/    |
|/____|_________________________________________________snd___|/____|""")
print("Welcome to Enchanted Temple.")
print("Your mission is to find your grandfather's ancient relic.\n\n")

print("You enter the temple and the silence invades all the place. You see two hallways at each side but you can't "
      "see what is at the end, you must decide which one to take.")
choice = input("Left or Right? ")

if choice.lower() == 'left':
    print("You follow the left hallway and you manage to get to the end, you see a door at your right and in front of "
          "you, you see some stairs going down. You must decide now which way to follow.")
    choice = input("Door or Stairs? ")

    if choice.lower() == 'stairs':
        print(
            "You take the stairs down. You start to feel a bit scared, you are getting deeper in the temple, alone. You "
            "turn your head to see your way back but you percieve that everything changed. The hallway you took wasn't "
            "the same and you think that the enchanted temple moved things around to make you advance deeper without "
            "having a chance to go back. You think now that the only way of getting out is finding the relic. After "
            "some time, you get to the end of the stairs and you enter a room with only a bookcase. You approach the "
            "bookcase and you see only two books and a small note. You read the note that says: 'A book reveals the "
            "secret of this temple and another reveals the demons trapped in it'. You now need to make a decision, "
            "which book to take.")
        choice = input("the RED book or the BLUE one? ")

        if choice.lower() == 'blue':
            print(
                "You open the BLUE one and suddenly one of the walls starts to open, letting you discover a hidden "
                "path. "
                "You follow this path and it takes you to a golden box. You open the box and all of your fears go "
                "away. "
                "You have the relic in your hands. You have the power over the temple now. You can leave. YOU WIN!")
        else:
            print("You open the RED one and all the room starts to shake intensely. The stairs break appart and the "
                  "bookcase falls down. You throw the book far but it's too late. A white fog fills the room. You "
                  "can't see "
                  "anything anymore. Suddenly, a big demon face appears in front of you and takes all your body and "
                  "soul. "
                  "You freeze immediately and fall like a brick. You were never found. Game Over.")
    else:
        print(
            "You open the door carefully. You start to feel a cold wind leaving the room as you open the door slowly. "
            "Suddenly you were pushed in and the door was shut and locked before you could react. You stand up and see "
            "immediately a pile of corpses at the wall. You try to understand where you are and how do you get out, "
            "but a voice whispers inside the corpse pile: 'You will never go back. We are the ones that failed to find "
            "the ancient relic, and now you are one of us'. Suddenly all the corpses stand up and take you to the pile "
            "without you even trying to fight. Game over.")

else:
    print(
        "You follow the right hallway and halfway you see a shadow following you, you start running but you are "
        "eventually blocked by a wall. The hallway took you to a dead end and the shadow managed to capture you. You "
        "were never able to leave the temple for the rest of your life. Game over.")
