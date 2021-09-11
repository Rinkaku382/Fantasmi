
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
    scene scene1
    with slowfade
    a """
    Dear someone...

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

    return
