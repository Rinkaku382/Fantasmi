
define slowfade = Fade(1.0, 0, 3.0)
define midfade = Fade(1.0, 0, 2.0)
define quickfade = Fade(1.0, 0, 1.0)
define slowerfade = Fade (3.0, 0, 3.0)
define slowdissolve = Dissolve(2.0)
define fadehold = Fade(3.0, 1.0, 3.0)

define config.menu_include_disabled = True
#define config.hard_rollback_limit = 0

define a = Character("Miss A")
define s = Character("Shin'ya")

label start:
    scene black
    with midfade
    a """
    Dear someone...

    I don't actually know\nwhy I'm writing this.

    Or why I'm doing it.

    Maybe it's just a way to liberate\na feeling I've been having.

    To let out the thoughts\nthat come from specific events.

    Or maybe it's to pass on\nthese stories to someone...

    So that they'll be remembered.
    """
    scene 1
    with slowfade
    a """
    You can call me Miss A.

    My full name\nis not important at all.

    It wouldn't add anything to this story.

    Because what I'm going to tell you\nis more about others than about me.

    So...

    I'll start from the beginning.

    I was taking a walk the other day.

    Losing myself in the vastness\nof nature around my house...

    I lost track of time.

    And when I got back,\na letter was waiting for me.
    """
    scene 2
    with slowdissolve
    a """
    The only thing on the envelop was my address.

    I didn't know who the sender was...

    But there was no way\nI could not recognize the writing.

    And when I opened it,\na rush of memories hit me.
    """
    scene black
    with midfade
    show text "Dear A.,\n\nA year has already passed since the last time we saw each other,\nand I sure owe you some excuse for not writing you\nuntil now.\nI've spent all this time thinking about your 'ability',\nand about my ghosts.\nOr should I say ours?" with quickfade
    $ renpy.pause (25)
    scene 2
    with midfade
    a """
    Shin'ya...

    I haven't heard from him for so long,\nand yet I never forgot him.

    As I read those words,\nold feelings peeled through my mind.

    Silently.

    Our ghosts...

    Some months have passed\nsince the last time I saw one.

    But I remember it very clearly.

    An Autumn afternoon,\nafter a rainy morning.

    Right when it stopped pouring down,\nsomeone entered in the bar.

    Like all the time I was alone,\nexpecting for clients.

    Or visitors,\njust like him.
    """
    scene black
    with midfade
    show text "Ghost #1\n\nKenny"
    $ renpy.pause (5)
    scene 6
    with midfade
    """
    I've been keeping this bar for some years, now.

    And the mornings have always been\nquiet and calm.

    Tender light peeking in\nthrough the windows.

    Soft wind caressing\nthe curtains.

    Few customers,\nall solitary and silent.
    """

    scene black
    with slowfade
    show text "Thank you for playing this demo!\nI will release more about Fantasmi/ghosts during the coming months\nso follow me on Twitter at\n@TSoletude\nor\n@Rinkaku382" with quickfade
    $ renpy.pause (7)
    scene black
    with fadehold
    $ renpy.pause(3)
    $ renpy.quit()
