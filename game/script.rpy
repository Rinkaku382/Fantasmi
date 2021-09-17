
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
    $ who = False
    $ where = False
    $ why = False
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
    show text "Dear A.,\n\nHow are you doing?\nIs everything alright there at the bar?\n\nA year has already passed since the last time we saw each other,\nand I sure owe you some excuse for not writing you\nuntil now.\nI've spent all this time thinking about your 'ability',\nand about my ghosts.\nOr should I say ours?" with quickfade
    $ renpy.pause (25)
    scene 2
    with midfade
    a """
    Shin'ya...

    I haven't heard from him for so long,\nand yet I never forgot him.

    As I read those words,\nold feelings peeled through my mind.

    Silently.

    Our ghosts...

    Months have passed\nsince the last time I saw one.

    But I remember it very clearly.

    An Autumn afternoon,\nafter a rainy morning.

    Right when it stopped pouring down,\nsomeone entered in the bar.

    I was alone,\nexpecting for clients.

    Or visitors,\njust like him.
    """
    scene black
    with midfade
    show text "Ghost #1\n\nKenny - Introduction"
    $ renpy.pause (5)
    scene 6
    with midfade
    """
    I've been keeping this bar for some years, now.

    And it has always been\nquiet and calm.

    Tender light peeking in\nthrough the windows.

    Soft wind caressing\nthe curtains.

    Gentle music flowing\nfrom hidden speakers.

    Then, right in the middle\nof that afternoon, he came in.
    """
    scene 7
    with slowdissolve
    """
    Like many others,\nhe came for me.

    For my ability.

    And I, in a way,\nwas waiting for him...

    Or for someone like him.

    He rapidly looked around...

    And then he took a seat next to me,\ngazing at the floor with nostalgic eyes.

    I think he wanted to say womething,\nbut somehow he couldn't.
    """
    a "Hi, welcome to my bar!"
    k """
    ...

    Hey.
    """
    jump kquestions

label kquestions:
    if who == True and where == True:
        jump kconversation
    else:
        menu:
            "What's your name?" if not who:
                $ who = True
                k """
                Kenny.

                That's my name.
                """
                a """
                Sounds like a funny name!

                You can call me Miss A.

                Nice to meet you, Kenny.
                """
                k "Oh...\nn-nice to meet you too."
                jump kquestions
            "I've never seen you around these parts..." if not where:
                $ where = True
                k """
                Yeah, I'm...

                I'm not from around here.

                Actually, I live very far.

                Had to took an airplan...
                """
                a """
                Oh really...?

                Well, that seems like\na big effort for real....
                """
                k "You can bet on that."
                jump kquestions

label kconversation:
    menu:
        "What brings you here?":
            k """
            I...

            I think you know.
            """
            a "And what is it\nI should know?"
            k """
            The reason...

            My reason to be here.

            I mean...

            You're that Miss A., right?
            """
            a """
            Yes.

            Miss A. in the flesh.

            Nice to meet you.

            So...

            You wanna talk about your ghost,\nI bet.
            """
            k """
            Yes...

            I'm having\nvery big troubles with it.

            I think.
            """
            a "You think?"
            k """
            I'm not entirely sure.

            I feel like something is off.

            With me, in general.

            My mood hasn't been the same since...\nlong time.

            A dear friend told me about you.

            And that personal ghosts can influence one's life\npositively or negatively.
            """
            a """
            Yes, that's true.

            And people come here seeking help...

            But please,\ndon't expect solutions.

            I can't solve your problems.

            I can only identify them.
            """
            k """
            That's ok.

            All I want is\nto know what's wrong.
            """
            a """
            Ok, let's see, then...
            """
            k """
            Do I...

            Do I have to do\nsomething particular?
            """
            a """
            No.

            Just turn towards me.

            And look into my eyes.
            """
            jump kghost

label kghost:
    scene black
    with midfade
    show text "Ghost #1\n\nKenny - Interrogation"
    $ renpy.pause (5)
    scene 8
    with midfade
    """
    """


    scene black
    with slowfade
    show text "Thank you for playing this demo!\nI will release more about Fantasmi/ghosts during the coming months\nso follow me on Twitter at\n@TSoletude\nor\n@Rinkaku382" with quickfade
    $ renpy.pause (7)
    scene black
    with fadehold
    $ renpy.pause(3)
    $ renpy.quit()
