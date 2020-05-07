from random import shuffle, randint

# ---- Mhxanismoi Fyllwn ----

def card(typos, rank, points):
    return (typos, rank, points)


def cardType(card):
    return card[0]


def cardRank(card):
    return card[1]


def cardStrength(card):
    return card[2]


def printCard(card):
    # card('A', '♠', 11) --> (A,♠)
    return "({},{})".format(cardType(card), cardRank(card))


stack = [card('A', '♠', 11), card('2', '♠', 2), card('3', '♠', 3), card('4', '♠', 4), card('5', '♠', 5),
         card('6', '♠', 6), card('7', '♠', 7), card('8', '♠', 8), card('9', '♠', 9), card('10', '♠', 10),
         card('J', '♠', 10), card('Q', '♠', 10), card('K', '♠', 10), card('A', '♥', 11), card('2', '♥', 2),
         card('3', '♥', 3), card('4', '♥', 4), card('5', '♥', 5), card('6', '♥', 6), card('7', '♥', 7),
         card('8', '♥', 8), card('9', '♥', 9), card('10', '♥', 10), card('J', '♥', 10), card('Q', '♥', 10),
         card('K', '♥', 10), card('A', '♣', 11), card('2', '♣', 2), card('3', '♣', 3), card('4', '♣', 4),
         card('5', '♣', 5), card('6', '♣', 6), card('7', '♣', 7), card('8', '♣', 8), card('9', '♣', 9),
         card('10', '♣', 10), card('J', '♣', 10), card('Q', '♣', 10), card('K', '♣', 10), card('A', '♦', 11),
         card('2', '♦', 2), card('3', '♦', 3), card('4', '♦', 4), card('5', '♦', 5), card('6', '♦', 6),
         card('7', '♦', 7), card('8', '♦', 8), card('9', '♦', 9), card('10', '♦', 10), card('J', '♦', 10),
         card('Q', '♦', 10), card('K', '♦', 10)]
openstack = [] # trapezi
ranks = ['♠', '♥', '♣', '♦']


# --- Script for deck making ---

def makeMeADeck():
    str = '['
    with open('cards.txt', "w", encoding="utf-8") as f:
        for rank in ranks:
            for i in range(1, 14):
                if i == 1:
                    str = str + "card('A', '{}', 11), ".format(rank)
                elif i == 11:
                    str = str + "card('J', '{}', 10), ".format(rank)
                elif i == 12:
                    str = str + "card('Q', '{}', 10), ".format(rank)
                elif i == 13:
                    str = str + "card('K', '{}', 10), ".format(rank)
                else:
                    str = str + "card('{}', '{}', {}), ".format(i, rank, i)
        str = str.strip(', ')
        str = str + ']'
        f.write(str)


# --- Mhxanismos Paixtwn ---

def player(name):
    return [name, 0, []]


def nameOf(p):
    return p[0]


def pointsOf(p):
    return p[1]


def deckOf(p):
    return p[2]


# --- Mhxanismoi Trapoulas ---

def initializeStack(closedstack):
    shuffle(closedstack)


def createDecks(player_list, stack):
    for i in range(0, 7):
        for p in player_list:
            deckOf(p).append(stack.pop())


def refillStack(closedstack, openstack):
    for i in range(0, len(openstack) - 1):
        closedstack.append(openstack.pop(0))


def top_card(ls):
    return ls[-1]


def playCard(player, card, openstack):
    deckOf(player).remove(card)
    openstack.append(card)


def isPlayable(karta1, karta2):
    if cardType(karta1) == cardType(karta2) or cardRank(karta1) == cardRank(karta2):
        return True
    else:
        return False


def drawCard(stack, player, times=1):
    for i in range(0, times):
        deckOf(player).append(stack.pop())


def showPlayerOptions(player, topcard):
    """
(A,karw)
j--> 1 - ()
()
3 - ()
(2,koupa)
()
6 - ()

opt = 3
"""
    opt = 0

    options = ''
    j = 0

    for karta in deckOf(player):
        if isPlayable(topcard, karta):
            if nameOf(player)!='CPU':
                options = options + "{} - {}\n".format(j, printCard(karta))
            opt += 1
        else:
            if nameOf(player)!='CPU':
                options = options + "{}\n".format(printCard(karta))
        j += 1
    print(options)
    return opt


def sort_list(li, cond=lambda x: x):
    """
    Ταξινόμηση φυσαλίδας κατά το κριτήριο cond
    """
    for j in range(0, len(li)):
        for i in range(1, len(li)):
            if cond(li[i - 1]) > cond(li[i]):
                li[i], li[i - 1] = li[i - 1], li[i]
    return li


def alphabetically(player):
    return ord(player[0][0])


def pointAccording(player):
    return pointsOf(player)


def countPoints(playerlist):
    for p in playerlist:
        p[1] = pointsOf(p) + sum(cardStrength(x) for x in deckOf(p))


def printScore(playerlist):
    print('Σκορ:')
    playerlist = sort_list(playerlist, pointAccording)
    for p in reversed(playerlist):
        print('Ο {} έχει {} πόντους.'.format(nameOf(p), pointsOf(p)))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def startGame(stack):
  list_of_players = []
  print(" ---- ΑΓΩΝΙΑ ---- ")
  settings = int(input('0-Κανονικό   1-VS CPU'))
  if settings==0:
    num_of_players = int(input("Αριθμός Παιχτών: "))
    for i in range(0, num_of_players):
        name = input("Όνομα Παίχτη {}: ".format(i + 1))
        list_of_players.append(player(name))
    list_of_players = sort_list(list_of_players, alphabetically)
  else:
      print('Παίζεις εναντίον της CPU')
      name = input("Όνομα Παίχτη: ")
      list_of_players.append(player(name))
      list_of_players.append(player('CPU'))
      num_of_players = 2
      list_of_players = sort_list(list_of_players, alphabetically)
  # ftiakse thn trapoula

  print('Ανακάτεμα τράπουλας...')
  initializeStack(stack)
  createDecks(list_of_players, stack)

  # trava arxikh karta
  openstack = []
  print('Επιλογή του πρώτου φύλλου...')
  openstack.append(stack.pop())
  i = 0
  bonus = 0
  conditionOf9 = True
  conditionOf8 = True
  conditionOf7 = True
  gameCondition = True
  conditionOfAce = True

  """ 
  i+=1
  0%num_of_players = 0
  π.χ στην περίπτωση τριών παιχτών 
  1%3 = 1
  2%3 = 2 
  3%3 = 0 // γίνεται ο κύκλος 
  4%3 = 1 
  5%3 = 2
  6%3 = 0 // ξαναγίνεται κύκλος
  ---γενικά:
  list_of_players[i%num_of_players]
  δείκτης: 
  i%num_of_players
  """

  while gameCondition:

      if i==0:
          conditionOf7 = False
          conditionOf8 = False
          conditionOf9 = False
          conditionOfAce = False

      # σε περίπτωση που το πάνω ανοιχτό φύλλο είναι Α
      if cardType(top_card(openstack)) == 'A':
          print('Ο τύπος άλλαξε σε {}!'.format(rankCond))
      conditionOfAce = True
      # σε περίπτωση που το πάνω ανοιχτό φύλλο είναι 9
      if cardType(top_card(openstack)) == '9' and conditionOf9 == True:
          print('Ο {} έχασε την σειρά του!'.format(nameOf(list_of_players[i % num_of_players])))

          i += 1
          conditionOf9 = False

      print('Παίζει ο {}...'.format(nameOf(list_of_players[i % num_of_players])))
      if cardType(top_card(openstack)) != 'A':
          print('Το χαρτί στο τραπέζι είναι {}'.format(printCard(top_card(openstack))))
      elif cardType(top_card(openstack)) == 'A' and conditionOfAce:
          print('Ο τύπος των φύλλων είναι {}!'.format(rankCond))
      if nameOf(list_of_players[i%num_of_players])!='CPU':
        print('Τα φύλλα σου είναι: ')
      else:
          print('Η CPU έχει {} φύλλα.'.format(len(deckOf(list_of_players[i%num_of_players]))))
      if cardType(top_card(openstack)) != 'A':
          playable_cards = showPlayerOptions(list_of_players[i % num_of_players], top_card(openstack))
      elif cardType(top_card(openstack)) == 'A' and conditionOfAce:
          playable_cards = showPlayerOptions(list_of_players[i % num_of_players], card('A', rankCond, 11))
      
      # σε περίπτωση που το πάνω ανοιχτό φύλλο είναι 7
      if conditionOf7 and cardType(top_card(openstack)) == '7' and not ('7' in [cardType(x) for x in deckOf(list_of_players[i % num_of_players])]) and bonus!=0:
          print("+{} Φύλλα! (επειδή δεν έχεις 7)".format(bonus))
          if len(stack)>bonus:
            drawCard(stack, list_of_players[i % num_of_players], bonus)
          else:
            refillStack(stack, openstack)
            drawCard(stack, list_of_players[i % num_of_players], bonus)
          bonus = 0
          print('New Deck!')
          playable_cards = showPlayerOptions(list_of_players[i % num_of_players], top_card(openstack))
          conditionOf7 = False
      if playable_cards == 0:
          print('Κανένα φύλλο δεν παίζεται.')
          if conditionOf7 and cardType(top_card(openstack)) == '7' and bonus!=0:

            print("+{} Φύλλα! (επειδή δεν έχεις 7)".format(bonus))
            if len(stack) > bonus:
                drawCard(stack, list_of_players[i % num_of_players], bonus)
            else:
                refillStack(stack, openstack)
                drawCard(stack, list_of_players[i % num_of_players], bonus)
            bonus = 0
            conditionOf7 = False
          else:
            print('Τράβηξε φύλλο...')
            if len(stack) !=0:
                drawCard(stack, list_of_players[i % num_of_players], 1)
            else:
                refillStack(stack, openstack)
                drawCard(stack, list_of_players[i % num_of_players], 1)
            print('Τράβηξες {}!'.format(printCard(top_card(deckOf(list_of_players[i % num_of_players])))))
    
            if isPlayable(top_card(deckOf(list_of_players[i % num_of_players])), top_card(openstack)):
                print('Παίζω {}...'.format(printCard(top_card(deckOf(list_of_players[i % num_of_players])))))
                playCard(list_of_players[i % num_of_players], top_card(deckOf(list_of_players[i % num_of_players])), openstack)
                if cardType(top_card(openstack)) == '7':
                    bonus+=2
                if cardType(top_card(openstack)) == 'A' and conditionOfAce:
                    if nameOf(list_of_players[i % num_of_players]) == 'CPU':
                        rankCondIndex = randint(0,3)
                    else:
                        print('Δίαλεξε τον αριθμό που αντιστοιχεί στον τύπο του χαρτιού:')
                        rankCondIndex = int(input('0 - ♠, 1 - ♥, 2 - ♣, 3 - ♦'))
                        while rankCondIndex not in [0, 1, 2, 3]:
                            print('Άκυρη επιλογή!')
                            rankCondIndex = int(input('Ξαναδιάλεξε! '))
                    rankCond = ranks[rankCondIndex]
                    conditionOf8 = True
            else:
              print('Τίποτα δεν μπορεί να παιχτεί :(')
              print('Επόμενος παίχτης... ')
              #conditionOf8 = True
              #conditionOf9 = True
      else:
          if conditionOf7 and cardType(top_card(openstack)) == '7' and '7' not in [cardType(x) for x in deckOf(list_of_players[i % num_of_players])] and bonus!=0:
              print("+{} Φύλλα!".format(bonus))
              if len(stack) > bonus:
                  drawCard(stack, list_of_players[i % num_of_players], bonus)
              else:
                  refillStack(stack, openstack)
                  drawCard(stack, list_of_players[i % num_of_players], bonus)
              bonus = 0
              new_playable = showPlayerOptions(list_of_players[i % num_of_players],top_card(openstack))
              conditionOf7 = False

          if nameOf(list_of_players[i%num_of_players]) == 'CPU':
              index=0
              while not isPlayable(deckOf(list_of_players[i % num_of_players])[index], top_card(openstack)):
                index = randint(0,len(deckOf(list_of_players[i%num_of_players]))-1)
              print('Η CPU έπαιξε {}!'.format(printCard(deckOf(list_of_players[i % num_of_players])[index])))

          else:
            index = int(input('Διάλεξε ποιά κάρτα θα παίξεις! '))
    
          """
            index --> 1 - (A, koupa)
            (2, karw)
            2 - (Q, spa8i)
          """
          if cardType(top_card(openstack)) != 'A' and nameOf(list_of_players[i%num_of_players])!='CPU':
            while not isPlayable(deckOf(list_of_players[i % num_of_players])[index], top_card(openstack)):
                print('Άκυρη επιλογή!')
                index = int(input('Ξαναδιάλεξε ποιά κάρτα θα παίξεις! '))
          elif cardType(top_card(openstack)) == 'A' and conditionOfAce:
            if nameOf(list_of_players[i%num_of_players])=='CPU':
                index = 0
                while not isPlayable(deckOf(list_of_players[i % num_of_players])[index], card('A', rankCond, 11)):
                    while not isPlayable(deckOf(list_of_players[i % num_of_players])[index], card('A', rankCond, 11)):
                        index = randint(0, len(deckOf(list_of_players[i % num_of_players]))-1)
                print('Η CPU έπαιξε {}!'.format(printCard(deckOf(list_of_players[i % num_of_players])[index])))
            else:
                while not isPlayable(deckOf(list_of_players[i % num_of_players])[index], card('A', rankCond, 11)):
                    print('Άκυρη επιλογή!')
                    index = int(input('Ξαναδιάλεξε ποιά κάρτα θα παίξεις! '))
          playCard(list_of_players[i % num_of_players], deckOf(list_of_players[i % num_of_players])[index], openstack)
          if cardType(top_card(openstack)) == '7':
              bonus += 2
          """
          Έλεγχος αν ο παίχτης έριξε άσσο.
          """
          if cardType(top_card(openstack)) == 'A' and conditionOfAce:
              if nameOf(list_of_players[i%num_of_players])=='CPU':
                  rankCondIndex = randint(0,3)
              else:
                  print('Δίαλεξε τον αριθμό που αντιστοιχεί στον τύπο του χαρτιού:')
                  rankCondIndex = int(input('0 - ♠, 1 - ♥, 2 - ♣, 3 - ♦'))
                  while rankCondIndex not in [0, 1, 2, 3]:
                      print('Άκυρη επιλογή!')
                      rankCondIndex = int(input('Ξαναδιάλεξε! '))
              rankCond = ranks[rankCondIndex]

          conditionOf9 = True
          conditionOf8 = True
      #conditionOf9 = True
      conditionOf7 = True

      # σε περίπτωση που το ανοιχτό πάνω φύλλο είναι 8
      if cardType(top_card(openstack)) == '8' and conditionOf8 == True:
          print('Ξαναπαίζεις!')

          conditionOf8 = False
      else:
          i +=1
    
      for p in list_of_players:
        if len(deckOf(p)) == 0:
          countPoints(list_of_players)
          printScore(list_of_players)
          print('Τέλος Παρτίδας!')
          stack = [card('A', '♠', 11), card('2', '♠', 2), card('3', '♠', 3), card('4', '♠', 4), card('5', '♠', 5),
                   card('6', '♠', 6), card('7', '♠', 7), card('8', '♠', 8), card('9', '♠', 9), card('10', '♠', 10),
                   card('J', '♠', 10), card('Q', '♠', 10), card('K', '♠', 10), card('A', '♥', 11), card('2', '♥', 2),
                   card('3', '♥', 3), card('4', '♥', 4), card('5', '♥', 5), card('6', '♥', 6), card('7', '♥', 7),
                   card('8', '♥', 8), card('9', '♥', 9), card('10', '♥', 10), card('J', '♥', 10), card('Q', '♥', 10),
                   card('K', '♥', 10), card('A', '♣', 11), card('2', '♣', 2), card('3', '♣', 3), card('4', '♣', 4),
                   card('5', '♣', 5), card('6', '♣', 6), card('7', '♣', 7), card('8', '♣', 8), card('9', '♣', 9),
                   card('10', '♣', 10), card('J', '♣', 10), card('Q', '♣', 10), card('K', '♣', 10), card('A', '♦', 11),
                   card('2', '♦', 2), card('3', '♦', 3), card('4', '♦', 4), card('5', '♦', 5), card('6', '♦', 6),
                   card('7', '♦', 7), card('8', '♦', 8), card('9', '♦', 9), card('10', '♦', 10), card('J', '♦', 10),
                   card('Q', '♦', 10), card('K', '♦', 10)]
          initializeStack(stack)
          for p in list_of_players:
              p[2] = []
          list_of_players = sort_list(list_of_players, alphabetically)
    
          print('Ανακάτεμα τράπουλας...')
          initializeStack(stack)
          createDecks(list_of_players, stack)
    
    
          # trava arxikh karta
          print('Επιλογή του πρώτου φύλλου...')
          openstack = []
          openstack.append(stack.pop())
          i = 0
          bonus = 0
          conditionOf9 = True
          conditionOf8 = True
          conditionOf7 = True
          conditionOfAce = True
    
          break
    
      for p in list_of_players:
          if pointsOf(p) > 50:
              print('--- Τέλος Παιχνιδιού! --- ')
              gameCondition = False
              print('Τέλος Αγωνίας!')
              sort_list(list_of_players, pointAccording)
              printScore(list_of_players)
              break