# I imported time
import time



def main():

    
 
    first_choice = 'none'
    second_choice = 'none'
    third_choice = 'none'
    forth_choice = 'none'
    
    print()
    print('Welcome to the eternal night')
    print()
    
    print('You wake up, its dark you can'+"'"+'t see a thing you reach around you feel something round. What do you find?')
    first_choice = input('(FLASHLIGHT/PIPE) ')

    print()

    #Should work
    if  first_choice.lower() == 'flashlight':
        print('You click on the flashlight, with the flashlight on you can see a door straight infront of you,')
        print('as you stand up to go to the door you hear a noise to your right. Do you go through the door ')
        print('Do you go through the door or go shine your flashlight at the noise.') 
        

        #should work
        while second_choice.lower() != 'door' or second_choice.lower() != 'shine':
            second_choice = input('(DOOR/SHINE) ')
            print()

            #Should work
            if second_choice.lower() == 'door':
                print('You walk across the wood floor You seem to have scared the noise away; you grab the handle')
                print('it doesn’t turn, the door appears you be rotting away you wonder if you can kick it down,')
                print('or if you should just find another way out.')
                
                third_choice = input('Do you kick the door or keep looking? (KICK/KEEP LOOKING) ')
                
                print()

                # Should work
                if third_choice.lower() == 'kick':
                    print('You kick the door it offers little resistant, You walk out the door and realize you are')
                    print('alone in a dark forest there appears to be a single star out, you recognize it as a north')
                    print('star you decide that its best to run away from the house.') 
                    forth_choice = input('Do you run North towards the star or run East or West? (NORTH/EAST/WEST) ')
                    
                    #should work
                    while forth_choice.lower() != 'north' or forth_choice != 'east' or forth_choice != 'west':
                        print()
                        
                        #done
                        if forth_choice.lower() == 'north':
                            print('You decide to go North. You start running to towards the star, trees threaten to hide it')
                            print('from you but you seem to be able you follow it as your running it vanishes behind the trees.')
                            print('You keep running looking for it hoping to see it again. Just them a howl piercing through the')
                            print('trees. You run faster you feel its right behind you, up ahead you see a cabin you hope to reach')
                            print('it in time. You run in the cabin locking the door not know how much help it will do with how rotten')
                            print('the door looks you turn back and see a sight all to familiar. You lay down with a laugh, knowing')
                            print('your fate, hoping next time you can escape this terrible cabin once in for all.')

                            #restart
                            time.sleep(2)
                            main()

                        #should work
                        elif forth_choice.lower() == 'east':
                            print('You decide to run East hoping you can get a clean get away. After some time, you end up')
                            print('in a clearing and decide to catch your breath for a minute. All the sudden you hear a howl')
                            print('piercing through the chilly air, you hold your breath as you turn around and there it is,')
                            print('the monster standing on the edge of the forest, red eyes glowing, glaring at you but not')
                            print('stepping closer. Just them you see the sun peaking over the trees and the monster retreats')
                            print('into the forest.')
                            print()
                            print('You stay in the clearing for a while then, and decide to find your way to out of the woods')
                            print('before night fall.')
                            print()
                            print('You escaped. Ending 3 of 3')

                            restart = input('Do you want to play again? (YES/NO) ')
                            if restart.lower() == 'yes':
                                main()
                            else:
                                exit()
                        
                        #should work with claw ending
                        elif forth_choice.lower() == 'west':
                            print('You decide to run west, the forest grows thick as you run through it, you hear a howl coming')
                            print('from behind you. You quicken your pace hoping it won’t catch you. Ahh, you scream as something')
                            print('stabs you in the chest as your cloths start to darken for your crimson blood, you wonder if')
                            print('you’ll ever escape as you pass out.')
                            time.sleep(2)
                            print()
                            print('You wake up somehow alive your hand reaches for your chest and its still there but its not')
                            print('bleeding. You decide its best to leave it there for now, as you pass out.')

                            time.sleep(1)
                            main()



                        else:
                            print('Only a moment of hesitation, you feel ready to pick.')
                            forth_choice = input('(NORTH/EAST/WEST) ')

                #done
                elif third_choice.lower() == 'keep looking':
                    print('You turn around and notice a open window as well as a staircase leading down.')
                    forth_choice = input('Where do you go? (DOWN/WINDOW) ')

                    #done
                    while forth_choice.lower() != 'down' or forth_choice.lower() != 'window':

                        print()

                        if forth_choice.lower() == 'window':
                            print('You run to the window hoping it will break you threw the flashlight, it hits the window,')
                            print('breaks making the cabin pitch black. You know there’s no escape and let the monster over')
                            print('take you as everything fades from your mind.')

                            #restart
                            time.sleep(2)
                            main()

                        elif forth_choice.lower() == 'down':
                            print('Down the stairs you see a door. You run hoping you lock yourself down there hoping the')
                            print('monster will leave if you wait long enough. You shut the door, hands freezing from the')
                            print('steel door, you can find the lock, just then something clicks, sealing you down there.')
                            print('You wonder way you even try, you have to kill it you doubt you can escape with it alive')
                            print('but you don’t have anything sharp enough. You wonder how many times you been here thinking')
                            print('the exact same thing, knowing your fate that you will never leave. With that you draft to')
                            print('sleep.')

                            #restart
                            time.sleep(2)
                            main()

                        else:
                            print('Time seems to pause as you make up your mind.')
                            forth_choice = input('(DOWN/WINDOW) ')
                
                #Should work and leads to claw ending
                else:
                    print('You seem hesitant, right as you decide to kick the door open, you see something out of the')
                    print('corner of your eye, the noise you realize, just as you turn something stabs you in the chest,')
                    print('you look down only to see a lone claw in your chest, you feel it was always there but you')
                    print('must be mistaken, you stumble out the door and pass out.')

                    print()
                    time.sleep(3)

                    print('You wake up the claw still in your chest, maybe that could kill it you think to yourself')
                    print('as you draft back to sleep, hoping this nightmare ends.')

                    #restart
                    time.sleep(1)
                    main()
                    
            #done
            elif second_choice.lower() == 'shine':
                print('You shine your light at the noise right as you see it, it runs back into the darkness, but')
                print('you were able to notice its claw markings on the hard wood wall, you bet it could shear')
                print('your fingers off in one swipe. You decide you would rather not find out if it could.')
                print('Do you try the door and turn your back to it or do you look for another way out?') 
                third_choice = input('(DOOR/LOOK AROUND) ')

                print()
                
                #done
                if third_choice.lower() == 'door':
                    print('You decide to run for the door it looks rotten, and decide to just ram your shoulder into')
                    print('the door hoping that it will be the fast enough to leave the noise behind, you burst')
                    print('through the door, wood splintering but you seem to be unhurt, you keep running hoping')
                    print('to get as far away as you can, you don’t look back. You rest for the night in a nearby')
                    print('tree planning on looking for help tomorrow.')

                    #restart
                    time.sleep(2)
                    main()
                
                #Done
                elif third_choice.lower() == 'look around':
                    print('You look around seeing a closed window near the door. You could swear it wasn’t there')
                    print('before you decide it’s the best way out quickly, you throw the flashlight hoping that')
                    print('the window will break, it flies true smashing into the window glass shatters. You jump')
                    print('out the window, too quickly to pick up your flashlight. As you run off into the night')
                    print('you look back to see a figure in the window, the light turns off leaving the after')
                    print('image of the figure in your eyes haunting you. You decide its best to keep running')
                    print('until you find someone.')
                    print()
                    print('You escaped. Ending 2 of 3')

                    restart = input('Do you want to play again? (YES/NO) ')
                    if restart.lower() == 'yes':
                        main()
                    else:
                        exit()
                
                #done
                else:
                    print('You stand there, frighten with fear as something pounces you hit the floor hard wishing')
                    print('you had done something as your consciousness leaves you.')

                    #restart
                    time.sleep(2)
                    main()
                    
            #done
            else:
                print('You sit still dumbfounded trying to figure out how you got in the cabin and hoping to')
                print('yourself that the noise is just a rat. You feel you should try the door or at least')
                print('face your fear and shine the light at the noise.')
                

    #Just need claw ending and test everything
    elif first_choice.lower() == 'pipe':

        print('You feel a pipe in your hands ready to strike at any noise you hear')
        print('Just then you hear something clawing at a wall near by. Do you go')
        print('towards it or backaway from it? ')
        second_choice = input ('(FIGHT/FLIGHT) ')

        print()

        while second_choice.lower() != 'flight' or second_choice.lower() != 'fight':

            #should work
            if second_choice.lower() == 'fight':
                print('you walk closer its hard to tell how far away it is, you wish you had a flashlight you')
                print('continue forward ready to swing at the first noise it makes. You take a step pain shoots')
                print('up your foot, just then you hear it screech, you most of stepped on its tail what do you do?')
                third_choice = input('(SWING/RUN) ')
                
                #should work
                while third_choice != 'swing' or third_choice != 'run':
                    print()

                    #should work
                    if third_choice.lower() == 'swing':
                        print('You swing, it feels like you hit a brick wall, you hear the pipe bend. You')
                        print('can’t save yourself that was your only chance you drop the pipe and fall back')
                        print('on to a claw. To shots up into your chest as you hit the ground, you pass out')
                        print('from the pain.')
                        print()
                        print('You wake you and reach toward your chest the claw is still there, you lay in')
                        print('the dark a little more then fall asleep.')

                        time.sleep(2)
                        main()
                    
                    #ADDed A RESTART Question
                    elif third_choice.lower() == 'run':
                        print('You run pain keeps shooting up the foot that stepped on it, you fall unable to keep')
                        print('running with the pain in your foot, you turn over and try to swing the pipe at the')
                        print('noise you feel like you just hit a brick wall and drop the pipe. It cuts off your')
                        print('arm and leaves you there to die.')
                        print()
                        print('you lose. Ending 1 of 3')

                        restart = input('Do you want to play again? (YES/NO) ')
                        if restart.lower() == 'yes':
                            main()
                        else:
                            exit()

                    
                    #should work
                    else:
                        print('Your mind starts screaming at you begging you to decide')
                        third_choice = input('(SWING/RUN) ')

            #Works 
            elif second_choice.lower() == 'flight':
                print('You scramble to your feet and start quietly walking away from the noise as your walking')
                print('away you find a wall.')
                third_choice = input('(LEFT/RIGHT) ')

                while third_choice.lower() != 'left' or third_choice != 'right':
                    print()

                    #Should work and asks to restart
                    if third_choice.lower() == 'left':
                        print('You turn to the left as your walking you stumble upon a staircase leading down, you')
                        print('start going down hoping there’s  a door at the bottom so you can keep out the monster')
                        print('as you walking something pushes you down the stairs when you reach the bottom you hear')
                        print('a click of a look and a voice saying please feed my pet for me, I haven’t have visitors')
                        print('in ages. You hear the noise you heard above you can feel the hunger in its eyes.')
                        print()

                        print('the end')

                        restart = input('Do you want to play again? (YES/NO) ')
                        if restart.lower() == 'yes':
                            main()
                        else:
                            exit()

                    #sjould work now!!!
                    elif third_choice.lower() == 'right':
                        print('You turn to the Right as your walking you start to feel a window thinking to yourself')
                        print('your free you use your pipe and break the window; you jump out it and run you hear the')
                        print('howl of the monster from the cabin you run hoping that it won’t find you. You hide in')
                        print('a tree and wait you slowly draft to sleep.')

                        #restart
                        time.sleep(2)
                        main()

                    #SHOULD WORK NOW!!!
                    else:
                        print('You feel stupid for not choosing sooner and just pick ')
                        third_choice = input('(LEFT/RIGHT) ')

    
        

            #this is done now!!!
            else:
                print('You sit there, your pipe ready to hit anything that comes your way, the noise stops, you')
                print('wait for what seems like hours. What every it is seems content waiting for you to make a')
                print('move. You start to feel tired, but can’t sleep, sleep would mean death. You’re ready to')
                print('make your move.')
                
                second_choice = input('(FIGHT/FLIGHT) ')

                print()

    #done
    elif first_choice == 'claw':  
        print('Memories flood your mind of past attempts. You rip the claw out of your chest surprised')
        print('on how clean the claw came out of you try and feel for blood but can’t feel any. With the')
        print('claw in hand, you feel energized, you stand up and look for the monster. The full moon')
        print('breaks through the clouds, light spills through the window, lighting up the cabin. You')
        print('see the monster standing before you on the opposite side of the room, looking ready to')
        print('attack. What do you do?')
        second_choice = input('(ATTACK/DODGE) ')

        print()

        if second_choice == 'dodge':
            print('It rushes at you. Your body moves almost as if you’ve been here before. The monster misses')
            print('and leaves itself wide open. What do you stab?')
            third_choice = input('(EYE/HEART) ')

            while third_choice.lower() != 'eye' or third_choice.lower() != 'heart':

                if third_choice.lower() == 'eye':
                    print('You go for the eye. It screams out and runs half blind done the stairs. You run out of the')
                    print('cabin dawn has come. You look back and don’t catch sight of it. You make it to the road, a')
                    print('car stops for you. The driver asks where you want to go, “ho…” you say, just then a howl')
                    print('cuts you off, that howl you know all to well, even as you drive away you know your never')
                    print('escape.')
                    print()
                    print('You got the secret bad ending')

                    restart = input('Do you want to play again? (YES/NO) ')
                    if restart.lower() == 'yes':
                        main()
                    else:
                        exit()
                
                elif third_choice.lower() == 'heart':
                    print('You stab the monster, the claw cuts easily through its body. The monster goes limp as the')
                    print('claw reaches its heart. It falls to the floor, you did it, the monster has finally been')
                    print('killed your free you think to yourself after all this time your finally see the sun rise')
                    print('on this terrible nightmare. And with that you walk out of the cabin as the first lights')
                    print('of dawn come a lick your face with their warmth rays of sun. You walk through the forest')
                    print('and reach a road, a car finally comes and stops for you, the driver asked where your headed,')
                    print('home you reply,')
                    print('home.')
                    print()
                    time.sleep(2)
                    print('You got the secret good ending')

                    restart = input('Do you want to play again? (YES/NO) ')
                    if restart.lower() == 'yes':
                        main()
                    else:
                        exit()

                else:
                    print('All your choices have led you here, it’s to late to show mercy, where do you stab it?')
                    third_choice = input('(EYE/HEART) ')
            
        elif second_choice == 'attact':
            print('You rush forward, it was hoping for this, it seems eager. You attack and clash against it')
            print('claws, they both break, you stand there stunned as it stabs you with its other claw.')
            print('You failed and pass out.')
            time.sleep(2)
            main()

        else:
            print('You stand there stunned unable to move as to stabs you, interesting enough, it still has both its')
            print('claws. You pass out')
            main()

    #Done
    else: 
        print('The item seems to have vanished, you start to wonder if it was ever there to begin with.')
        print('You start to shuffle backwards as you, just then your hand doesn’t hit the floor you start')
        print('falling down steps, you must be in a basement, your scream in pain from the fall, the')
        print('noise you heard goes quiet, you pass out from the pain.')

        #restart
        time.sleep(2)
        main()
   

    
main()


    