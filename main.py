from battle import Person
from magic import Spell
from inventory import item

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
potion=Item

#instantiate People
player=Person( 460 , 65 , 60 , 34 , [fire,thunder,blizzard,meteor,quake,cure,cura] )
enemy=Person( 1200 , 65 , 45 , 25 , [] )
running = True
i=0

print ( "AN ENEMY ATTACKS" )

while running:
    print("========================================")
    player.choose_action()
    choice=input( "Choose Action:" )
    index=int(choice) - 1

    if index == 0:
        dmg=player.generate_damage()
        enemy.take_damage(dmg)
        print( "You attacked for" , dmg , "Points of damage." )

    elif index ==1:
        player.choose_magic()
        magic_choice=int(input( "choose magic:" ))-1

        spell=player.magic[magic_choice]
        magic_dmg=spell.generate_damage()
        currrent_mp=player.get_mp()

        if spell.cost>currrent_mp:
            print( "\nNOt enough MP\n" )
            continue
        player.reduce_mp(spell.cost)


        if spell.type == "white":
            player.heal(magic_dmg)
            print("\n"+spell.name + " heals for",str(magic_dmg)," HP:")
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print("\n"+spell.name+" deals",str(magic_dmg)," points of damage" )



    enemy_choice =1
    enemy_dmg=enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print( "Enemy attacks for" ,enemy_dmg)
    print("====================================")
    print( "ENEMY HP: " + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()))
    print( "Your HP:" + str(player.get_hp()) + "/" + str(player.get_max_hp()))
    print( "Your MP:" + str(player.get_mp()) + "/" + str(player.get_max_mp()))
    if enemy.get_hp()==0:
        print(" You win! ")
        running = False

    elif player.get_hp()==0:
        print( "You lose ,enemy defeated you!" )
        running = False
