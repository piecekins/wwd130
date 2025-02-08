

print()

first_item = input('You wake up, its dark you can'+"'"+'t see a thing you reach around you feel something round. What do you find? (FLASHLIGHT/PIPE) ')

print()

if  first_item.lower() == 'flashlight':
    print('You click on the flashlight, with the flashlight on you can see a door straight infront of you, as you stand up to go to the door you hear a noise to your right')


elif first_item.lower() == 'pipe':
    print('You feel a pipe in your hands ready to strike at any noise you hear')
    fight_or_flight = input('Just then you hear something clawing at a wall near by. Do you go towards it or backaway from it? (FIGHT/FLIGHT) ')
    if fight_or_flight.lower() == 'fight':
        print('you walk closer its hard to tell how far away it is, you wish you had a flashlight')

else: print('The item seems to have vanished, you start to wonder if it was ever there to begin with')




