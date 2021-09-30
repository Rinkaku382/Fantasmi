
define slowfade = Fade(1.0, 0, 3.0)
define midfade = Fade(1.0, 0, 2.0)
define quickfade = Fade(1.0, 0, 1.0)
define slowerfade = Fade (3.0, 0, 3.0)
define slowdissolve = Dissolve(2.0)
define middissolve = Dissolve(1.0)
define fadehold = Fade(3.0, 1.0, 3.0)

define config.menu_include_disabled = True
define config.hard_rollback_limit = 0

define a = Character("Miss A", color="#d4ccd7")
define k = Character("Kenny", color="#c9aad7")
define kg = Character("Kenny's ghost", color="#b888cf")
define c = Character("The Conglomerate", color="#b888cf")

label start:
    $ who = False
    $ where = False
    $ why = False
    $ kghost_res = 0
    scene 1
    with slowdissolve
    $ renpy.pause (3)
    a "Dear someone..." with dissolve
    stop sound fadeout (1)
    play music "prologue2.ogg" fadein(2)
    a """
    I don't actually know\nwho I'm writing to.

    Or why I'm doing it.

    Maybe it's just a way to liberate\na feeling I've been having.

    To let out the thoughts\nthat come from specific events.

    Or maybe it's to pass\nthese stories on to someone...

    So that they'll be remembered.

    You can call me Miss A,\nanyway.

    My full name\nis not important at all.

    It wouldn't add anything to this story.

    Because what I'm going to tell you\nis more about others than about me.

    So...

    I'll start from the beginning.

    I was taking a walk the other day.

    While finding myself in the vastness\nof nature around my house...

    I lost track of time.

    And when I got back,\na letter was waiting for me.
    """
    scene 3
    with slowdissolve
    a """
    The only thing on the envelope was my address.

    The sender's name\nwas missing...

    But I immediately\nrecognized the writing.

    And when I opened it,\na rush of memories hit me.
    """
    scene letter1a
    with slowfade
    $ renpy.pause (2)
    scene letter1b
    with middissolve
    $ renpy.pause (2)
    scene letter1c
    with middissolve
    $ renpy.pause (2)
    scene letter1d
    with middissolve
    $ renpy.pause (2)
    scene letter1e
    with middissolve
    $ renpy.pause (2)
    scene letter1f
    with middissolve
    $ renpy.pause (2)
    scene letter1g
    with middissolve
    $ renpy.pause (2)
    scene letter1h
    with middissolve
    $ renpy.pause (2)
    scene letter1i
    with middissolve
    $ renpy.pause (5)
    scene 3
    with slowdissolve
    a """
    Shinya...

    I hadn't heard from him for so long,\nand yet I never forgot him.

    As I read those words,\nold feelings peeled through my mind.

    Silently.

    Our ghosts...

    Months had passed\nsince the last time I saw one.

    But I still remember it\nvery clearly.

    An Autumn afternoon,\nafter a rainy morning.

    Right when it stopped pouring down,\nsomeone entered in the bar.

    I was alone,\nexpecting for clients.

    Or visitors,\njust like him.
    """
    stop music fadeout(4)
    scene black
    with midfade
    play sound "chapter.ogg" fadein(0.5)
    show text "Ghost #1\n\nKenny - Introduction" with quickfade
    $ renpy.pause (5)
    scene 2
    with midfade
    play music "kenny.ogg"
    """
    I've been keeping this coffee bar for some years, now.

    And it has always been\nquiet and calm.

    Tender light peeking in\nthrough the windows.

    Soft wind caressing\nthe curtains.

    Atmospheric music flowing\nfrom hidden speakers.

    Then, right in the middle\nof that afternoon, he came in.
    """
    scene 4
    with midfade
    $ renpy.pause (2)
    scene 5
    with middissolve
    $ renpy.pause (2)
    scene 6
    with middissolve
    $ renpy.pause (2)
    scene 7
    with slowdissolve
    """
    Like many others,\nhe came for me.

    For my ability.

    And I, in a way,\nwas waiting for him...

    Or for someone like him.

    He rapidly looked around...

    And then he took a seat next to me,\ngazing at the floor with nostalgic eyes.

    I think he wanted to say something,\nbut somehow he couldn't.
    """
    a "Hi, welcome to my coffee bar!"
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
                """
                a """
                It's a nice one!

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

                Had to took an airplane\nto come here...
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

            I think you know...
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

            I bet you wanna talk\nabout your ghost,right?
            """
            k """
            Yes...

            I'm having...

            Very big troubles with it.

            I think.
            """
            a "You think?"
            k """
            I'm not entirely sure.

            I feel like something is off.

            With me, in general.

            My mood hasn't been the same since...\nlong time.

            It's like something\nisn't working properly, in me.

            I tried asking for advices,\nand for help, but...

            I got nothing.

            And then, a dear friend\ntold me about you.

            He said that personal ghosts\ncan influence one's life.

            That this is the issue I'm having.

            The source of my feelings.

            So I decided to...try.

            And I came here.
            """
            a """
            Yes, that's true.

            Lots of people\ncome here seeking for help...

            And bring their ghosts with them,\nhoping that I will be able to erase them.

            That I'll make them disappear.

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
            scene 9
            with slowdissolve
            a """
            No.

            Just turn towards me.

            Look into my eye.

            And tell me about\nyourself.
            """
            jump kghost

label kghost:
    scene black
    with midfade
    play sound "chapter.ogg"
    show text "Ghost #1\n\nKenny - Analysis" with quickfade
    $ renpy.pause (5)
    scene 8
    with midfade
    k """
    Throughout the years I got accostumed\nto more and more fear...

    At each step I took...

    At each eye I met...

    I always felt an uncomfortable feeling.

    As if I was cursed.

    Fully aware of my obligations...

    Of my duties as an artist\ntowards my fans.

    I did everything I could\nfor everyone.

    And yet nobody\ndid anything for me.

    That's when fear appeared.

    When I started\nfeeling unwell.

    In that moment,\nI looked around myself...
    """
    scene 10
    with slowdissolve
    kg """
    Stop talking!

    Don't tell her anything!
    """
    a """
    It took you long enough\nto show up.

    There's so many\nof you in one!

    Are you...\na conglomerate...?
    """
    c """
    It's none\nof your business.

    Leave us alone.

    We don't need you.
    """
    menu:
        "I just want to help him.":
            c """
            We don't care.

            He's in good company\nwith us.

            He does not need\nanyone's help.

            We are the only ones\nwho can help him.
            """
            menu:
                "Let me try, at least!":
                    c """
                    We won't.

                    Now let us leave\nthis place.
                    """
    """
    They are so stubborn...

    Maybe I should be firmer.
    """
    menu:
        "Why is he here, if you are enough?":
            c """
            Once again, that's none\nof your business.

            He's weak.

            He commits mistakes.

            We are here to solve them.
            """
            menu:
                "You're not doing a good job, then.":
                    c """
                    What do you know\nabout us?

                    We are strangers.

                    We don't know you.

                    You don't know us.

                    So your opinion does not matter.
                    """
                    "They sound harsher then before..."
                "Are you so much helpful?":
                    c """
                    Yes.

                    We are.

                    Now let us leave,\nplease.
                    """
                    "Are they wavering?"
            menu:
                "Ghosts like you are just a front.":
                    $ kghost_res = -1
                    a """
                    You are all talk\nand no act.

                    You stand there,\nwith your mighty words.

                    While he keeps on suffering.

                    And you don't even\nlet him talk.

                    Are you helping him\nfor real?

                    It does not seem so.
                    """
                    c "..."
                    jump kghost2
                "What if I don't?":
                    $ kghost_res = 1
                    c """
                    We won't talk anymore,\nthen.
                    """
                    jump kghost2
        "Won't you just give me one opportunity?":
            c """
            Absolutely not.

            You only are\na useless brat.

            We are more\nthan enough for him.

            No one ever helped him.

            And you're not an ecception.
            """
            menu:
                "Oh, and are you? Really?":
                    c """
                    ...

                    What are you insinuating?
                    """
                    a """
                    Oh absolutely nothing...

                    Just that you are\nsuch a good ghost...
                    """
                    menu:
                        "So good that he's suffering so much.":
                            $ kghost_res = -1
                            a """
                            And I bet\nit's also your fault...

                            Right?
                            """
                            c "..."
                            jump kghost2
                        "Aren't you?":
                            $ kghost_res = 1
                            c """
                            ...

                            We are tired\nof your pathetic nonsense.

                            You think\nyou can scare us?

                            Make us angry?

                            You can't.
                            """
                            jump kghost2
                "Maybe I am.":
                    c """
                    Exceptions don't exist.

                    Humans are all the same.

                    They demand,\nbut don't give.

                    They lie,\nand are never sincere.

                    Not even\nwith themselves.

                    Such is\nthe human condition.
                    """
                    menu:
                        "I'm not the unsincere one, here.":
                            $ kghost_res = 1
                            c """
                            Your words\ndon't touch us.

                            We don't care about what\nyou have to say.

                            And we will never do.
                            """
                            jump kghost2
                        "Yet you demand attention, but don't give any.":
                            $ kghost_res = -1
                            a """
                            Aren't you just as selfish,\nby doing that?

                            Ghosts should be\nbetter than humans, right?
                            """
                            c "..."
                            jump kghost2

label kghost2:
    if kghost_res == 1:
        """
        Then,\nthe ghost stopped talking.
        """
        play sound "chapter.ogg"
        show text "Ghost #1\n\nKenny - Conclusion" with quickfade
        $ renpy.pause (5)
        scene 8
        with slowdissolve
        """
        And Kenny looked\nway more sad than before.

        He still stood there\nfor a while.

        In silence.

        And then, he got away.

        As if he was\ncontrolled by something.

        Something stronger...

        That forced him to go away\nand never come back.
        """
        scene 2
        with midfade
        """
        That wasn't\nmy first or only failure.

        It happens a lot...

        To fail\nat talking with a ghost.

        Personal ghosts can be stubborn.

        Or aggressive.

        Or introvert.

        Sometimes it's dangerous\nto even engage with them.
        """
        scene 1
        with middissolve
        """
        And yet, that day left me\na sense of defeat.

        But Shinya's letter\nstill continued...

        And the other two parts\nreminded me of two other encounters.
        """
        jump enddemo

    if kghost_res == -1:
        $ write = False
        $ travelling = False
        kg """
        ...

        Ok, then.

        We will let him talk.

        For this time.
        """
        a """
        Don't worry,\nthere won't be others.
        """
        scene 9
        with middissolve
        a """
        Kenny?

        Are you there?
        """
        k """
        Y-yes...

        What was I\nsaying...?
        """
        a "You were talking\nabout your fear."
        scene 8
        with middissolve
        k """
        Yeah,\nright...

        At that time...

        Even though I had people\nall around me...

        I felt lonely.

        No one was really\ninterested in me.

        They were much rather\ninto my fame.

        They feeded themselves\noff it.

        They feeded off me.

        And then I escaped.

        I erased\nmy phone number.

        Fled from\nmy country.

        And came here...\nto understand myself.

        But I still feel\nall those eyes on me.
        """
        jump kconversation2

label kconversation2:
    if write == True and travelling == True:
        jump kconversation3
    else:
        menu:
            "What is it that made you famous?" if not write:
                $ write = True
                k """
                My...

                My creations.

                All the things\nI wrote.

                All the things\nI thought...

                I thought that\nthrowing them outside of me would help.

                I wanted to...

                I don't know...

                Maybe to liberate myself.

                Or to send messages\nto other people.

                But sometimes people\njust want to take.

                And take...

                And take again.

                Then the pressure comes in.

                You can't create anymore.

                Expectations arise.

                Time runs shorter.

                And you can't help but\nfall victim of all this.

                I tried doing my best...

                But I don't know\nif I succeeded.
                """
                jump kconversation2
            "How can travelling help you?" if not travelling:
                $ travelling = True
                k """
                I want to find myself\nonce again.

                I feel like I've lost...me.

                And I have to find all my pieces.

                And I thought\nthat...

                Putting some distance between\npresent and past can help, sometimes.

                And new places\ncan give new ideas.

                New images\ncan inspire new feelings.

                Fame is an obstacle to that.

                An obstacle to the process...

                And also to the result.

                It poisons the creation\nfrom the moment it starts developing...

                Until the second it is born.
                """
                jump kconversation2

label kconversation3:
    scene black
    with midfade
    play sound "chapter.ogg"
    show text "Ghost #1\n\nKenny - Conclusion" with quickfade
    $ renpy.pause (5)
    scene 7
    with slowdissolve
    a """
    You know...

    Your ghost was very stubborn.

    And harsh.

    And it was more than one.

    I call that kind 'conglomerate'.

    Which means it is a multitude of ghosts\nthat form one entity.

    So, more personal ghosts into one.

    And they wanted to protect you\nfrom the outside world.

    Sometimes, ghosts think\nthey act in our defense, but...

    They act as a reflection\nof our self-defense mechanism.

    Taking distance from people...

    Abandoning our past...

    Embracing the future...

    All these actions may be guided\nby you or your ghost.

    So, let me ask you something...

    You don't have to answer,\nbut let's try anyway.
    """
    menu:
        "Will you continue travelling?":
            k """
            ...

            Maybe.

            I would like to.

            There is peace in travelling.

            And freedom.

            And when I'm writing, now,\nit's not for others...

            But for myself alone.

            Somehow, though...\nI'll have to think about it.
            """
        "Will you go back?":
            k """
            Sometimes I think I should...

            Going back,\nsolving everything I left behind...

            There are nights in which\nI dream about all that.

            The people\nI abandoned.

            The situations\nI escaped from.

            And I ask\nmyself...

            What's happening there, now?

            Is there someone\nwaiting for me?

            But I don't know if I could.

            Not even if I should.
            """
    a """
    Like I said\nat the beginning...

    I can't give you\nany answer.

    I can only ask questions.

    Talk with your ghost.

    Pass through its defenses...

    And open your mind.

    Then, encourage you to look at things\nfrom different perspectives.
    """
    k """
    I think that's enough.

    It really helped.

    And I can truly tell you that...

    Coming here all the way from home\nwas worth it.

    So...\nthank you.
    """
    a """
    Oh, you don't have to\nthank me!

    Don't worry about it.

    It's my hobby.
    """
    k "Your hobby?"
    a """
    Yes...

    My job is to keep this place.

    And talking with ghosts\nis just something I do to help others.

    I think it's the least\nI can do for other people.
    """
    scene 2
    with midfade
    """
    I still remember that day with melancholy.

    A slightly happier one\nthan Kenny's, though.

    Anyway...

    He took a coffee.

    We drank together for a bit.

    Talked about our lives.

    About his writings.

    About the travel\nand the sensations that come with it.
    """
    scene 1
    with middissolve
    """
    I remember feeling envious.

    I, too, wanted to go far away.

    To discover new things.

    But I'm still\ntied to this place.

    Before going away,\nhe said this...

    If he had my power,\nhe would have used it to know people better...

    To analyze the world around him.

    In order to write about it\nand let other people know.

    And I can't help\nbut wonder...

    Is this what you are doing now,\nShinya?

    Your letter\nstill continued...

    And the remaining two parts\nreminded me of two other encounters.
    """
    jump enddemo


label enddemo:
    stop music fadeout(10)
    scene black
    with slowfade
    show text "Writing, Promgramming and Art by\n\nRinkaku" with midfade
    $ renpy.pause (4)
    show text "Colour by\n\nLio" with midfade
    $ renpy.pause (4)
    show text "Music by by\n\nTatsuhisa Yamamoto" with midfade
    $ renpy.pause (4)
    show text "Additional sounds by\n\nRinkaku" with midfade
    $ renpy.pause (4)
    play sound "chapter.ogg"
    show text "Thank you for playing this demo!\nI will release more about Fantasmi/ghosts during the coming months\nso follow me on Twitter at\n@TSoletude\nor\n@Rinkaku382"
    $ renpy.pause (7)
    scene black
    with fadehold
    $ renpy.pause(3)
    $ renpy.quit()
