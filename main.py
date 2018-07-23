

#from inventory import Item
from battle import Person,bcolors
from magic import Spell


#create Black magic
fire=Spell( "Fire " , 10 , 100 , "black" )
thunder=Spell( "Thunder ", 10 , 100 , "black" )
blizzard=Spell( "Blizzard " , 10 , 100 , "black" )
meteor=Spell( "Meteor " , 10 , 100 , "black" )
quake=Spell( "Quake " , 10 , 100 , "black" )

#create white magic_choice
cure=Spell( "Cure " , 12 , 120 ,"white" )
cura=Spell( "Cura " , 18 , 200 , "white" )

#create some items
#potion=Item

#instantiate People
player=Person( 460 , 65 , 60 , 34 , [fire,thunder,blizzard,meteor,quake,cure,cura] )
enemy=Person( 1200 , 65 , 45 , 25 , [] )
running = True
i=0

print ( bcolors.BOLD + "AN ENEMY ATTACKS" + bcolors.ENDC )

while running:
    print("========================================")
    player.choose_action()
    choice=input( bcolors.UNDERLINE + " Choose Action: " + bcolors.ENDC )
    index=int(choice) - 1

    if index == 0:
        dmg=player.generate_damage()
        enemy.take_damage(dmg)
        print( bcolors.FAIL + "You attacked for" , dmg , " Points of damage. " + bcolors.ENDC )

    elif index ==1:
        player.choose_magic()
        magic_choice=int(input( bcolors.UNDERLINE + " Choose Magic: " + bcolors.ENDC ))-1

        spell=player.magic[magic_choice]
        magic_dmg=spell.generate_damage()
        currrent_mp=player.get_mp()

        if spell.cost>currrent_mp:
            print( bcolors.HEADER + "\nNOt enough MP\n" + bcolors.ENDC )
            continue
        player.reduce_mp(spell.cost)


        if spell.type == "white":
            player.heal(magic_dmg)
            print("\n"+spell.name + " heals for",str(magic_dmg)," HP")
        elif spell.type == "black":

            enemy.take_damage(magic_dmg)
            print("\n" + spell.name + " deals",str(magic_dmg), " points of damage" )



    enemy_choice =1
    enemy_dmg=enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print(bcolors.OKBLUE + "Enemy attacks for" ,enemy_dmg , bcolors.ENDC)
    print("====================================")
    print( bcolors.OKBLUE + "ENEMY HP: " + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC)
    print( bcolors.UNDERLINE + "\n","Your HP:" + str(player.get_hp()) + "/" + str(player.get_max_hp())," " + bcolors.ENDC)
    print( bcolors.WARNING + "\n" , "Your MP:" + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)
    if enemy.get_hp()==0:
        print(" You win! ")
        running = False

    elif player.get_hp()==0:
        print( bcolors.BOLD + "You lose ,enemy defeated you!" + bcolors.ENDC )
        running = False
