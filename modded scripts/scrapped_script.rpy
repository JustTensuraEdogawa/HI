    #     # This call statement calls the poem sharing minigame to be played.
    #     call poemresponse_start
    #     call ch1_end

    #     call poem

    #     ## Day 2
    #     $ chapter = 2
    #     call ch2_main
    #     call poemresponse_start
    #     call ch2_end

    #     call poem

    #     ## Day 3
    #     $ chapter = 3
    #     call ch3_main
    #     call poemresponse_start
    #     call ch3_end

    #     ## Day 4
    #     $ chapter = 4
    #     call ch4_main

    #     # This python statement writes a file from within the game to the game folder
    #     # or to the Android/data/[modname]/files/game folder.
    #     python:
    #         if renpy.android and renpy.version_tuple == (6, 99, 12, 4, 2187):
    #             try: file(os.environ['ANDROID_PUBLIC'] + "/hxppy thxughts.png")
    #             except IOError: open(os.environ['ANDROID_PUBLIC'] + "/hxppy thxughts.png", "wb").write(renpy.file("hxppy thxughts.png").read())
    #         elif renpy.android:
    #             try: renpy.file(os.environ['ANDROID_PUBLIC'] + "/hxppy thxughts.png")
    #             except IOError: open(os.environ['ANDROID_PUBLIC'] + "/hxppy thxughts.png", "wb").write(renpy.file("hxppy thxughts.png").read())
    #         else:
    #             try: renpy.file(config.basedir + "/hxppy thxughts.png")
    #             except IOError: open(config.basedir + "/hxppy thxughts.png", "wb").write(renpy.file("hxppy thxughts.png").read())

    #     ## Day 5
    #     $ chapter = 5
    #     call ch5_main

    #     # This call statement ends the game but doesn't play the credits.
    #     call endgame
    #     return

    # elif persistent.playthrough == 1:
    #     $ chapter = 0
    #     call ch10_main
        
    #     # This jump statement jumps over to Act 2 from Act 1.
    #     jump playthrough2


    # elif persistent.playthrough == 2:
    #     ## Day 1 - Act 2
    #     $ chapter = 0
    #     call ch20_main
    #     label playthrough2:
    #         call poem

    #         python:
    #             if renpy.android and renpy.version_tuple == (6, 99, 12, 4, 2187):
    #                 try: file(os.environ['ANDROID_PUBLIC'] + "/CAN YOU HEAR ME.txt")
    #                 except IOError: open(os.environ['ANDROID_PUBLIC'] + "/CAN YOU HEAR ME.txt", "wb").write(renpy.file("CAN YOU HEAR ME.txt").read())
    #             elif renpy.android:
    #                 try: renpy.file(os.environ['ANDROID_PUBLIC'] + "/CAN YOU HEAR ME.txt")
    #                 except IOError: open(os.environ['ANDROID_PUBLIC'] + "/CAN YOU HEAR ME.txt", "wb").write(renpy.file("CAN YOU HEAR ME.txt").read())
    #             else:
    #                 try: renpy.file(config.basedir + "/CAN YOU HEAR ME.txt")
    #                 except IOError: open(config.basedir + "/CAN YOU HEAR ME.txt", "wb").write(renpy.file("CAN YOU HEAR ME.txt").read())

    #         ## Day 2 - Act 2
    #         $ chapter = 1
    #         call ch21_main
    #         call poemresponse_start
    #         call ch21_end

    #         # This call statement calls the poem mini-game with no transition.
    #         call poem(False)

    #         python:
    #             if renpy.android and renpy.version_tuple == (6, 99, 12, 4, 2187):
    #                 try: file(os.environ['ANDROID_PUBLIC'] + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
    #                 except IOError: open(os.environ['ANDROID_PUBLIC'] + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt", "wb").write(renpy.file("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt").read())
    #             elif renpy.android:
    #                 try: renpy.file(os.environ['ANDROID_PUBLIC'] + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
    #                 except IOError: open(os.environ['ANDROID_PUBLIC'] + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt", "wb").write(renpy.file("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt").read())
    #             else:
    #                 try: renpy.file(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
    #                 except IOError: open(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt", "wb").write(renpy.file("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt").read())

    #         ## Day 3 - Act 2
    #         $ chapter = 2
    #         call ch22_main
    #         call poemresponse_start
    #         call ch22_end

    #         call poem(False)

    #         ## Day 4 - Act 2
    #         $ chapter = 3
    #         call ch23_main

    #         # This if statement calls either a special poem response game or play
    #         # as normal.
    #         if y_appeal >= 3:
    #             call poemresponse_start2
    #         else:
    #             call poemresponse_start

    #         # This if statement is leftover code from DDLC where if your game is
    #         # a demo that it ends the game fully.
    #         if persistent.demo:
    #             stop music fadeout 2.0
    #             scene black with dissolve_cg
    #             "End of demo"
    #             return

    #         call ch23_end
    #         return

    # elif persistent.playthrough == 3:
    #     jump ch30_main

    # elif persistent.playthrough == 4:
    #     ## Day 1 - Act 4
    #     $ chapter = 0
    #     call ch40_main
    #     jump credits