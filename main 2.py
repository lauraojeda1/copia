#WAR 2.v.3
import time
import random
print('LOADING')
time.sleep(2)
###INTRO####

while True:
    intro = True
    dead = False
    while intro:
        enemies = ['Japan', 'Britain', 'Germany', 'France', 'Russia', 'America', 'Pakistan']
        techs = ['Club Weapons', 'Masonry', 'Stone', 'Stone Weapons', 'Mining', 'Philosophy', 'Religion',  'Bronze', 'Monarchy',  'Bronze Swords', 'Shields', 'Steel',
                  'Steel Swords', 'Trade', 'Cartography', 'Cavalry', 'Naval Forces', 'Mathematics', 'Bow and Arrows', 'Catapults', 'Trebuchets', 'Democracy',
                 'Firearms', 'Mechanics', 'Vehicles', 'Steam Engines', 'Advanced Firearms', 'Computing', 'Misiles', 'Nuclear Weaponry',
                 'Space Industries', 'Advanced Computing', 'Interplanetary Colonization', 'DNA Reorginization', 'Near Light-Speed Travel',
                 'Interstellar Colonization', 'Intergalactic Colonization']
        inv = []
        resource_message = True
        en = 0
        seh = 100
        shp = 50
        saggro = 0
        smoney = 0
        sen = 0
        stl = 0
        setl = 0
        sehr = 0
        smt = 0
        smm = 0
        sdefense = 0
        soffense = 0
        smhp = 75
        snc = 0
        scount = 0
        senemy = enemies[en]
        hc = 25
        aggro = 0
        tl = 0
        eh = 100
        ehr = 0
        etl = 0
        hp = 50
        offense = .01
        defense = .02
        money = 0
        mt = 0
        mhp = 75
        mm = 0
        defense_messages = ['You built forts around your border.', 'You built a wall around your border.',
                          'You recruited a small group of troops.', 'You reinforced your capital\'s walls.',
                            'You built watchtowers around your border.', 'You sent troops around your border.',
                            'You improved your military\'s armor.']
        rb = 0
        allies = []
        emhp = 100
        nc = 0
        score = 0 
        won = False
        count = 0
        enemy = enemies[en]
        playing = False
        sallies = []
        
        print('WELCOME TO WAR TWO')
        print()
        time.sleep(.75)
        print('1. Start Game')
        print('2. Guide')
        print('3. What\'s new?')
        print()
        opening = input('> ')

        if opening == '1':
            print()
            print('Enable savepoints? (y/n)')
            print()
            sc = input('> ')
            playing = True
            intro = False
            print()
            print('... Staring new game ...')
            print()
            time.sleep(3)
        if opening == '2':
            print('RULES')
            print()
            print('There are seven enemy countries in WAR 2--')
            print('every enemy you beat, you advance to the next.')
            print('While fighting, you have 6 options--')
            print()
            print('1. Upgrade')
            print('Choosing to upgrade allows you to upgrade maximum HP, defense, offense, or')
            print('the strength of your current technology.')
            print()
            print('2. Learn Technology')
            print('This allows you to learn the next technology.')
            print()
            print('3. Attack Enemy')
            print('This allows you to attack your current enemy.')
            print('The damage you deal depends on money, your technology level, your')
            print('enemy\'s technology level, and some chance.' )
            print('You are able to choose from three attack types of varying strength')
            print('and cost.')
            print()
            print('4. Gather resources')
            print('Gather resources to gain money, and if you enemy does not attack you')
            print('as you are gaining resources, HP.')
            print()
            print('5. Full Heal')
            print('Restores your HP to maximum')
            print('The cost of a full heal increases each time you use it.')
            print('n. Launch Nuclear Weapons')
            print('Once you have unlocked the \"Nuclear Weapon\" technology, you will be able to')
            print('launch nuclear weapons at your enemy.')
            print('You earn nukes every turn.')
        if opening == '3':
            print('--New--')
            print('  -Added Resources')#
            print('  -Added shop and items')#
            print('  -Added Trade')#

        while playing:
            if nc > 50:
                nc = 50
            if tl >= 4:
                if resource_message == True:
                    rc = random.randint(1,4)
                    if rc == 4:
                        print('After closer inspection, you notice that there is plenty of gold within your territory.')
                        resource_message = False
                        mt += 10
                        rb = 9
                        print()
                        time.sleep(5)
                    elif rc == 3:
                        print('After closer inspection, you notice that there is plenty of silver within your territory.')
                        resource_message = False
                        mt += 5
                        rb = 7
                        print()
                        time.sleep(5)
                    elif rc == 2:
                        print('After closer inspection, you notice that there is plenty of iron within your territory.')
                        resource_message = False
                        mt += 3
                        rb = 5
                        print()
                        time.sleep(5)
                    else:
                        print('After closer inspection, you notice that there is a lack of resources within your territory.')
                        mt -= (3/4)*mt
                        resource_message = False
                        rb = -3
                        print()
                        time.sleep(5)
            eh += ehr
            if tl >= 28:
                nc += random.randint(1,3)
            if enemy != 'PAKISTAN':
                enemy = enemies[en]
            count += 1
            if enemy == 'Pakistan':
                print()
                print('SITUATION SUDDENLY INTENSIFIES')
                print()
                enemy = 'PAKISTAN'
                eh = 10000
            money += mt
            mt = tl * 3 + money/100
            euc = random.randint(1,2)
            if etl < len(techs) - 1:
                if euc == 2:
                    etl += 1
            elif euc == 1:
                ehr += 1
            if money > mm:
                mm = money
            if mm > 200:    
                if money <= (1/2)*mm:
                    print('You have economically crippled yourself!')
                    mm = money
                    defense -= (1/3)*defense
                    offense -= (1/3)*offense
                    time.sleep(.5)
                    print()
            if hp > mhp:
                hp = mhp
            print('--Your stats--')
            time.sleep(.5)
            print(' -HP: ' + str(round(hp, 2)))
            time.sleep(.25)
            print(' -Technology:', techs[tl])
            time.sleep(.25)
            print(' -Money: ' + str(round(money,2)))
            time.sleep(.25)
            print(' -Money Per Turn: ' + str(round(mt,2)))
            time.sleep(.25)
            print(' -Defense: ' + str(round(defense,2)))
            time.sleep(.25)
            print(' -Enemy: ' + enemy + ' Enemy +' + str(aggro))
            time.sleep(.25)
            if tl >= 27:
                print(' -Nukes: ' + str(nc))
            print()
            if hp > 0:
                print('What will you do?--')
                print()
                time.sleep(.75)
                print(' 1. Upgrade')
                print(' 2. Learn a new tech')
                print(' 3. Attack Enemy')
                print(' 4. Gather Resources')
                print(' 5. Full Heal -' + str(hc) + ' money')
                if tl >= 28:
                    print(' n. Launch Nuclear Weapons')
                if sc == 'y':
                    print(' s. Save')
                if tl >= 12:
                    if len(allies) > 0:
                        print(' t. Trade')
                print(' b. Buy')
                print(' i. Check Inventory')
                print()
                time.sleep(.5)
                choice = input('> ')
                print()
                time.sleep(.5)

                if choice == '1':
                    print('--Upgrade Menu--')
                    print()
                    time.sleep(.25)
                    print(' -1. Upgrade maximum HP')
                    time.sleep(.25)
                    print(' -2. Upgrade defense')
                    time.sleep(.25)
                    print(' -3. Upgrade offense')
                    time.sleep(.25)
                    print(' -4. Upgrade technology')
                    time.sleep(.25) 
                    print()
                    time.sleep(.5)
                    upgrade_choice = input(' > ')
                    if upgrade_choice == '1':
                        mhp += tl/2
                        print(' Increased maximum HP by ' + str(tl/2))
                        print()
                        time.sleep(.5)
                    elif upgrade_choice == '2':
                        print(random.choice(defense_messages))
                        print()
                        time.sleep(.5)
                        defense += tl/10
                        print(' Increased defense by ' + str(tl/10))
                        print()
                        time.sleep(.5)
                    elif upgrade_choice == '3':
                        print(' You slightly strengthened your military.')
                        offense += tl/500
                    elif upgrade_choice == '4':
                        print(' You\'re perfecting the use of ' + techs[tl] + '.')
                        offense += tl/50
                        print()
                        time.sleep(.5)
                    if aggro < 6:
                        attack_chance = random.randint(1,3)
                        if attack_chance == 1:
                            print(' You were attacked by ' + enemies[en] + ' using ' + techs[etl])
                            print()
                            time.sleep(.75)
                            hp -= (random.randint(1,3) * etl + 1) - (defense)
                    elif aggro > 6:
                        attack_chance = random.randint(1,2)
                        if attack_chance == 1:
                            print(' You were attacked by ' + enemies[en] + ' using ' + techs[etl])
                            print()
                            time.sleep(.75)
                            hp -= (random.randint(1,4) * (etl + 2)) - ((3/4)*(defense))
                    elif aggro > 9:
                        print(' You were attacked by ' + enemies[en] + ' using ' + techs[etl])
                        print()
                        time.sleep(.75)
                        hp -= (random.randint(1,5) * etl + 3) - ((defense/2))
                        
                    
                        

                if choice == '2':
                    if tl < len(techs) - 1:
                        tl += 1
                        print()
                        time.sleep(.75)
                        print('--Learning new technology--')
                        time.sleep(.75)
                        print()
                        print( ' -You learned ' + techs[tl])
                        print()
                        time.sleep(.75)
                        attack_chance = random.randint(1,3)
                        if attack_chance == 1:
                            print(' You were attacked by ' + enemies[en] + ' using ' + techs[etl])
                            print()
                            time.sleep(.75)
                            hp -= (random.randint(1,3) * etl + 1) - (defense)
                        else:
                            print(' You safely learned a new technology')
                        print()
                        time.sleep(.5)
                    if tl == len(techs):
                        print('You cannot learn any new technologies!')
                        attack_chance = random.randint(1,3)
                        if attack_chance == 1:
                            print(' You were attacked by ' + enemies[en] + ' using ' + techs[etl])
                            print()
                            time.sleep(.75)
                            hp -= (random.randint(1,3) * etl/random.randint(2,3) + aggro * random.randint(2,3)) - ((defense)/random.randint(1,3)) 
                        else:
                            print()

                if choice == '3':
                    if money >= 10:
                        print('--Choose an attack--')
                        print()
                        print(' -1. Minor attack -10 money')
                        time.sleep(.25)
                        print(' -2. Large attack -50 money')
                        time.sleep(.25)
                        print(' -3. Major attack -100 money')
                        time.sleep(.25)
                        print()
                        attack_choice = input(' > ')
                        if attack_choice == '1':
                            print('You attacked ' + enemies[en]+'.')
                            eh -= (((offense * 1000)/random.randint(1,3))-(etl/2) + tl/5 + money/100)/random.randint(5,15)
                            money -= 10
                            print('Enemy HP: ' + str(round(eh,2)))
                            print()
                            time.sleep(.5)
                        elif attack_choice == '2':
                            print('You attacked ' + enemies[en] + '.')
                            eh -= (((offense * 1500)/random.randint(1,2))-(etl/2) + tl/2 + money/100)/random.randint(5,15)
                            money -= 50
                            print('Enemy HP: ' + str(round(eh,2)))
                            print()
                            time.sleep(.5)
                        elif attack_choice == '3':
                            money -= 100
                            print('You attacked ' + enemies[en] + '.')
                            eh -= (((offense * 3000)/random.randint(1,2))-(etl/3) + tl/3 + money/100)/random.randint(5,15)
                            print('Enemy HP: ' + str(round(eh,2)))
                            print()
                            time.sleep(.5)
                        hp -= (((offense * 500)/random.randint(1,2))-(etl/2))/random.randint(1,4)

                    else:
                        print('Insufficient Money!')
                        print()
                        time.sleep(1)
                    aggro_chance = random.randint(1,3)
                    if aggro_chance >= 0:
                        print(enemy + ' has become slightly more aggressive!')
                        aggro += 1

                if choice == '4':
                    attack_chance = random.randint(1,3)
                    if attack_chance == 1:
                        print(' You were attacked by ' + enemies[en] + ' using ' + techs[etl])
                        print()
                        time.sleep(.75)
                        hp -= (random.randint(1,3) * etl + 1) - (defense)
                    else:
                        print('You safely gathered resources!')
                        print('+' + str(tl) + 'HP')
                        hp += tl
                        money += tl + rb
                if choice == '5':
                    if money >= hc:
                        print('You fully healed!')
                        hp = mhp
                        money -= hc
                        hc *= 2
                    else:
                        print('Insufficient money!')
                if choice == 'n':
                    print('How many nukes will you launch?')
                    launch_ammount = input('> ')
                    if launch_ammount.isdigit():
                        if int(launch_ammount) <= nc:
                            print()
                            print('You launched ' + launch_ammount + ' nuclear weapons at ' + enemy + '.')
                            eh -= random.randint(3,5)*(int(launch_ammount)) - (etl/random.randint(1,4))
                            nc -= int(launch_ammount)
                            print('Enemy HP: ' + str(round(eh)))
                        elif int(launch_ammount) > nc:
                            print('You cannot launch that many nuclear weapons!')
                    else:
                        print('You accidentally launched nukes at yourself -- HP -' + str((1/10)*hp))
                        hp -= (1/10)*hp
                if choice == 't':
                    if int(len(allies)) > 0:
                        print('What will you trade?--')
                        x = 0
                        while x <= len(inv) - 1:
                            print(' -' + str(x + 1) + '. ' + inv[x])
                            x += 1
                        trade_choice = input(' > ')
                        if trade_choice.isdigit(): 
                            if int(trade_choice) <= len(inv):
                                trade_choice = int(trade_choice)
                                if inv[(trade_choice - 1)] == 'Trebuchets':
                                    print('You traded your Trebuchets to ' + random.choice(allies))
                                    money += 75
                                    offense -= 2
                                    inv.pop((trade_choice - 1))
                                elif inv[(trade_choice - 1)] == 'Catapults':
                                    print('You traded your Catapults to ' + random.choice(allies))
                                    money += 70
                                    offense -= (1/5)*offense
                                    inv.pop((trade_choice - 1))
                                elif inv[(trade_choice - 1)] == 'Ships':
                                    print('You traded your Ships to ' + random.choice(allies))
                                    money += 130
                                    offense -= (1/5)*offense
                                    inv.pop((trade_choice - 1))
                                elif inv[(trade_choice - 1)] == 'Steel Swords':
                                    print('You traded your steel swords to ' + random.choice(allies))
                                    money += 25
                                    offense -= .015
                                    inv.pop((trade_choice - 1))
                                elif inv[(trade_choice - 1)] == 'Pickaxes':
                                    print('You traded your Pickaxes to ' + random.choice(allies))
                                    money += 5
                                    mt -= 2
                                    inv.pop((trade_choice - 1))
                                elif inv[(trade_choice - 1)] == 'Stone Swords':
                                    print('You traded your Stone Swords to ' + random.choice(allies))
                                    money += 10
                                    offense += .02
                                    inv.pop((trade_choice - 1))
                                elif inv[trade_choice] == 'Muskets':
                                    print('You traded Muskets to ' + random.choice(allies))
                                    offense += .01
                                    inv.pop(trade_choice - 1)
                                    money += 25
                                    mt -= .25
                                    defense += .5
                                elif inv[trade_choice - 1] == 'Advanced Firearms':
                                    print('You traded Advanced Firearms to ' + random.choice(allies))
                                    inv.pop(trade_choice - 1)
                                    offense += .03
                                    defense += 2.1
                                    money += 130
                                    mt += 1
                                elif inv[trade_choice - 1] == 'Misiles':
                                    print('You have traded Misiles to ' + random.choice(allies) + '.')
                                    inv.pop(trade_choice - 1)
                                    offense += .03 
                                    defense += 2
                                    money += 145
                                    mt -= 2
                                elif inv[trade_choice - 1] == 'Rockets':
                                    print('You have traded Rockets to ' + random.choice(allies) + '.')
                                    inv.pop(trade_choice - 1)
                            else:
                                print('Invalid decision')
                                print()
                                time.sleep(.75)
                        else:
                            print('???')
                            print()
                            time.sleep(.75)
                    else:
                        print('You have no allies to trade to!!')
                        
                        
                            
                if choice == 'b':#############################################
                    print('--Market--')
                    print()
                    time.sleep(1)
                    if tl >= 3:
                        print('1.  Stone Swords      - 20 money')
                    if tl >= 4:
                        print('2.  Pickaxes          - 25 money')
                    if tl >= 12: 
                        print('3.  Steel Swords      - 30 money')
                    if tl >= 16:
                        print('4.  Ships             - 200 money')
                    if tl >= 19:
                        print('5.  Catapults         - 100 money')
                    if tl >= 20:
                        print('6.  Trebuchets        - 120 money')
                    if tl >= 22:
                        print('7.  Muskets           - 75 money')
                    if tl >= 26:
                        print('8.  Advanced Firearms - 100 money')
                    if tl >= 28:
                        print('9.  Misiles           - 200 money')
                    if tl >= 30:
                        print('10. Rockets           - 750 money')
                    print()
                    buy_choice = input('> ')
                    if buy_choice == '1':
                        if tl >= 3:
                            print('You purchased Stone Swords')
                            money -= 20
                            offense += 0.00025
                            inv.insert(-1,'Stone Swords')
                    elif buy_choice == '2':
                        if tl >= 4:
                            print('You purchased Pickaxes')
                            money -= 25
                            mt += 1.5
                            inv.insert(-1,'Pickaxes')
                    elif buy_choice == '3':
                        if tl >= 12:
                            print('You purchased Steel Swords')
                            money -= 30
                            offense += 0.001
                            inv.insert(-1,'Steel Swords')
                    elif buy_choice == '4':
                        if tl >= 16:
                            print('You purchased Ships')
                            money -= 200
                            offense += 0.05
                            inv.insert(-1,'Ships')
                    elif buy_choice == '5':
                        if tl >= 19:
                            print('You purchased Catapults')
                            money -= 100
                            offense += 0.02
                            inv.insert(-1,'Catapults')
                    elif buy_choice == '6':
                        if tl >= 20:
                            print('You purchased Trebuchets')
                            money -= 120
                            offense += 0.017
                            inv.insert(-1,'Trebuchets')
                    elif buy_choice == '7':
                        if tl >= 22:
                            print('You purchased Muskets')
                            money -= 75
                            defense += 1
                            offense += .05
                            inv.insert(-1,'Muskets')
                    elif buy_choice == '8':
                        if tl >= 26:
                            print('You purchased Advanced Firearms')
                            money -= 100
                            offense += .06
                            defense += 2
                            inv.insert(-1,'Advanced Firearms')
                    elif buy_choice == '9':
                        if tl >= 28:
                            print('You purchased Misiles')
                            offense += .08
                            defense += 3
                            money -= 200
                            inv.insert(-1,'Misiles')
                    elif buy_choice == '10':
                        if tl >= 30:
                            print('You purchased Rockets')
                            offense += .01
                            money -= 750
                            defense += 7
                            inv.insert(-1,'Rockets')
                            
                    else:
                        print('Invalid decision!!')
                if choice == 'i':
                    print('Inventory: ')
                    print(inv)
                    print()

                if choice == 's':
                    if sc == 'y':
                          print('. . . SAVING . . .')
                          print()
                          time.sleep(5)
                          sallies = allies
                          sinv = inv  
                          seh = eh
                          shp = hp
                          saggro = aggro
                          smoney = money
                          sen = en
                          stl = tl
                          setl = etl
                          sehr = ehr
                          smt = mt
                          smm = mm
                          sdefense = defense
                          soffense = offense
                          smhp = mhp
                          snc = nc
                          scount = count
                          senemy = enemy
                          srb = rb
                            
                            
                        
                        
                    
            else:
                if sc == 'y':
                    print(' . . . Going back to savepoint . . .')
                    print()
                    allies = sallies
                    inv = sinv
                    time.sleep(5)
                    h = seh
                    hp = shp
                    aggro = saggro
                    money = smoney
                    en = sen
                    tl = stl
                    etl = setl
                    ehr = sehr
                    mt = smt
                    mm = smm
                    defense = sdefense
                    offense = soffense
                    mhp = smhp
                    nc = snc
                    count = scount
                    enemy = senemy
                else:
                    time.sleep(1)
                    print()
                    dead = True
                    playing = False

              
            if eh <= 0:
                if enemy == 'PAKISTAN':
                    print('')
                    print(' . . . ')
                    time.sleep(5)
                    print()
                    print('Pakistan was defeated.')
                    won = True
                    playing = False
                else:
                    ally_chance = random.randint(1,4)
                    if ally_chance == 4 or ally_chance == 2:
                        print(enemy + ' surrenders!')
                        print()
                        time.sleep(2)
                        print('They wish to become your ally.')
                        time.sleep(1)
                        print('Do you accept their request? (y/n)')
                        ally_choice = input('> ')
                        if ally_choice == 'y':
                            allies.insert(-1,enemy)
                            print()
                    print()
                    time.sleep(3)
                    print('You defeated ' + enemies[en])
                    print()
                    en += 1
                    emhp *= 1.5
                    etl -= 1
                    time.sleep(1)
                    ehr /= 1.25
                    print('Your new enemy is. . .  ')
                    time.sleep(2)
                    print(enemies[en])
                    print()
                    time.sleep(2)
                    aggro = 0
                    eh = emhp
              

    while dead:
        print('G A M E  O V E R')
        intro = True
        dead = False

    while won:
        print('You have won!')
        time.sleep(2)
        print()
        print('--Score--')
        print(' -Money Bonus: ' + str(money))
        score += money
        time.sleep(1)
        print(' -Turns Bonus: ' + str((200 - count) * 5))
        score += (200 - count) * 5
        time.sleep(1)
        print(' -HP Bonus: ' + str(hp))
        score += hp
        time.sleep(1)
        print(' -Total Score: ' + str(score))
        time.sleep(5)
        print()
        intro = True
        won = False
        
