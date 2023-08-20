import random
class Character:
    def __init__(self):
        self.negate_hit = 'x0@'
        self.critical_hit = 'x2@'
        self.modifier_deck = [self.negate_hit, '-2', '-1', '-1', '-1', '-1', '-1', '+0', '+0', '+0', '+0', '+0', '+0', '+1', '+1', '+1', '+1', '+1', '+2', self.critical_hit]
        self.top_card = ""
        self.dis_advantage = False
        self.End_Turn = False

    def scenario_effect(self, b, n):
        apply_effect = b
        if apply_effect == True:
            while n > 0:
                self.modifier_deck.append('-1')
                n-=1

    def shuffle(self, d):
        random.shuffle(d)
        return d

    def fill_deck(self, d):
        deck_file = open("deck_file2.txt", "w+", encoding="utf8")
        x=len(d)
        for card in d:
            deck_file.writelines(card)
            x-=1
            if x > 0:
                deck_file.writelines("\n")
        deck_file.close()
        return d

    def empty_discard(self):
        open("discard_pile2.txt", "w", encoding="utf8").close

    def deck_prep(self,d):
        self.shuffle(d)
        self.fill_deck(d)
        self.empty_discard()

    def add_bless(self, n):
        bless_append = open("deck_file2.txt", "a+", encoding="utf8")
        for x in range(n):
            bless_append.writelines("\n")
            bless_append.writelines("x2 Bless")
        bless_append.close()
        print("Bless you!")
        
    def add_curse(self, n):
        curse_append = open("deck_file2.txt", "a+", encoding="utf8")
        for x in range(n):
            curse_append.writelines("\n")
            curse_append.writelines("x0 Curse")
        bless_append.close()
        print("Curses!")
    
    def small_deck_shuffle(self):
        small_deck = self.reading_file()
        random.shuffle(small_deck)
        self.fill_deck(small_deck)
        
    def bless(self, n):
        self.add_bless(n)
        self.small_deck_shuffle()
        exit(0)
    
    def curse(self, n):
        self.add_curse(n)
        self.small_deck_shuffle()
        exit(0)
    
    def display_card(self):
        read_deck = open("deck_file2.txt", "r", encoding="utf8")
        self.top_card = read_deck.readline(20)
        read_deck.close()
        print("Card drawn:") #****?
        print(self.top_card)
        return self.top_card

    def discard(self):
        open_discard = open("discard_pile2.txt", "a+", encoding="utf8")
        if "x2 Bless" in self.top_card or "x0 Curse" in self.top_card:
            print("back to bless deck with you")
            pass
        else:
            open_discard.writelines(self.top_card)
        open_discard.seek(0)
        print("Discard pile:") #****?
        print(open_discard.read()) #****?
        open_discard.close()

    def reading_file(self):
        deck_file = open("deck_file2.txt", "r", encoding="utf8")
        deck_read = deck_file.read()
        reading_deck = deck_read.split("\n")
        deck_file.close()
        return reading_deck

    def remove_card_list(self):
        smaller_deck = self.reading_file()
        smaller_deck.pop(0)
        deck_rewrite = open("deck_file2.txt", "w+", encoding="utf8")
        y=len(smaller_deck)
        for card in smaller_deck:
            deck_rewrite.writelines(card)
            y -= 1;
            if y > 0:
                deck_rewrite.writelines("\n")
        deck_rewrite.close()
        return smaller_deck

    def normal_process(self):
        self.display_card()
        self.discard()
        self.reading_file()
        self.remove_card_list()
    
    def attack(self):
        pile = open("discard_pile2.txt", "r", encoding="utf8")
        p = pile.read()
        if self.End_Turn == True and (self.critical_hit in p or self.negate_hit in p):
            undrawn = self.reading_file()
            if "x2 Bless" in undrawn or "x0 Curse" in undrawn:
                drawn = p.split("\n")
                drawn.pop()
                undrawn.extend(drawn)
                self.deck_prep(undrawn)
                print("Deck reset with bless/curses")
            else:
                try:
                    self.apply_perks()
                except:
                    pass
                self.deck_prep(self.modifier_deck)
                print("Deck reset")
        elif self.dis_advantage == True:
            self.normal_process()
            self.flip_effect()
            self.normal_process()
        else:
            self.normal_process()
            self.flip_effect()
        pile.close()
        
class Geminate(Character):
    def __init__(self):
        self.Perk_1 = False
        self.Perk_2 = 0
        self.Perk_3 = 0
        self.Perk_4 = 0
        self.Perk_5 = False
        self.Perk_6 = False
        self.Perk_7 = False
        self.Perk_8 = 0
        super().__init__()
        
    def apply_perks(self):
        if self.Perk_1 == True:
            self.modifier_deck.remove('-2')
            self.modifier_deck.append('+0')
            print("Perk 1 Added")
        if self.Perk_2 > 0:
            z = self.Perk_2
            while z > 0:
                self.modifier_deck.remove('-1')
                self.modifier_deck.append('+0 E for E')
                z -= 1
                print("Perk 2 Added!")
        if self.Perk_3 > 0:
            w = self.Perk_3
            while w > 0:
                self.modifier_deck.remove('+0')
                self.modifier_deck.append('+1 Poison')
                w -= 1
        if self.Perk_4 > 0:
            v = self.Perk_4
            while v > 0:
                self.modifier_deck.remove('+0')
                self.modifier_deck.append('+1 Wound')
                v -= 1
        if self.Perk_5 == True:
            self.modifier_deck.remove('+0')
            self.modifier_deck.remove('+0')
            self.modifier_deck.append('Flip Pierce 3')
            self.modifier_deck.append('Flip Pierce 3')
        if self.Perk_6 == True:
            self.modifier_deck.append('+1 Push 3')
            self.modifier_deck.append('+1 Push 3')
        if self.Perk_7 == True:
            self.modifier_deck.append('x2 Brittle, Self')
        if self.Perk_8 > 0:
            u = self.Perk_8
            while u > 0:
                self.modifier_deck.append('Flip +1 Regen, Self')
                u -= 1
        
    def flip_effect(self):
        try:
            while 'Flip' in self.top_card:
                self.normal_process()
        except:
            pass
  
  

gem = Geminate()

# gem.Perk_1 = True
# gem.Perk_2 = 0    #Max 3
# gem.Perk_3 = 0    #Max 2
# gem.Perk_4 = 0    #Max 2
# gem.Perk_5 = True
# gem.Perk_6 = True
# gem.Perk_7 = True
# gem.Perk_8 = 2    #Max 2
# gem.scenario_effect(True, 2)

# gem.bless(1)
# gem.curse(1)
# gem.dis_advantage = True

gem.End_Turn = True
gem.attack()


