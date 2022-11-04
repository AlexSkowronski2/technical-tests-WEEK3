import random

LETTER_DISTRIBUTION = {
    # keys of this represent frequency of respective letters in property
    "12": ["E"],
    "9": ["A", "I"],
    "8": ["O"],
    "6": ["N", "R", "T"],
    "4": ["L", "S", "U", "D"],
    "3": ["G"],
    "2": ["B", "C", "M", "P", "F", "H", "V", "W", "Y"],
    "1": ["K", "J", "X", "Q", "Z"]
}

class Tile:
    def __init__(self, letter):
        self.letter = letter
        #want to make points property and call getPoints on it but not letting me
    
    def getPoints(self):
        # given time constraints this seemed quickest method, would do a dictionary with the key as the points and list of letters
        if self.letter == 'A' or self.letter == 'E' or self.letter == 'I' or self.letter == 'O' or self.letter == 'N' or self.letter == 'R' or self.letter == 'T' or self.letter == 'L' or self.letter == 'S' or self.letter == 'U':
            return 1
        elif self.letter == 'D' or self.letter == 'G':
            return 2
        elif self.letter == 'B' or self.letter == 'C' or self.letter == 'M' or self.letter == 'P':
            return 3
        elif self.letter == 'F' or self.letter == 'H' or self.letter == 'V' or self.letter == 'W' or self.letter == 'Y':
            return 4
        elif self.letter == 'K':
            return 5
        elif self.letter == 'J' or self.letter == 'X':
            return 8
        elif self.letter == 'Q' or self.letter == 'Z':
            return 10
        else:
            #would do an error message here
            return "You do not have a valid tile"
    
class Word:
    def __init__(self, list_of_Tiles):
        self.letters = list_of_Tiles
    
    def calculate_score(self):
        total = 0
        for each_letter in len(self.letters) - 1:
            total += each_letter.getPoints()
        return total

class Bag_of_Tiles:
    def __init__(self):
        self.all_tiles = []

    def loop_over_dict(self, frequency_key):
        #accessing list of letters that turn up frequency times
        list_of_letters = LETTER_DISTRIBUTION["{}".format(frequency_key)]

        for letters in list_of_letters:
            self.all_tiles.append(Tile(letters))

    def multiple_loops(self, function, frequency):
        #performs above method for frequency number of times
        i = 1
        while i <= frequency:
            function
            i += 1

    def shuffle_bag(self):
        random.shuffle(self.all_tiles)

    def take_out_tile(self, player_tiles):
        removed_tile = self.all_tiles.pop()
        player_tiles.append(removed_tile)

class Player:
    def __init__(self, player_name, list_of_player_tiles, points_accumulated):
        self.player_name = player_name
        self.player_tiles = list_of_player_tiles
        self.player_points = points_accumulated

    def print_tiles(self):
        presentable_list = []
        for each_tile in self.player_tiles:
            presentable_list.append(each_tile["letter"])
        print(presentable_list)

def start_game():
    game_start = input("Hi Stranger, would you like to play Scrabble? 'yes'/'no' ").upper()
    if game_start == 'YES' or game_start == 'Y':
        return True
    elif game_start == 'NO' or game_start == 'N':
        return False
    else:
        #want to work a way into looping back to asking same question
        return False

def get_name():
    return input("Hi Stranger, what is your name???")

def main():
    game_condition = start_game()
    if game_condition == True:

        player_name = get_name()
        current_Player = Player(player_name, [], 0)

        deck = Bag_of_Tiles()
        frequency_list = ["12", "9", "8", "6", "4", "3", "2", "1"]
        #could have probably used the dictionary created for above list

        #for j in frequency_list:
        #deck.multiple_loops(deck.loop_over_dict(j), int(j))
        #deck.loop_over_dict(j)

        #ABOVE, wanted to make a function to do the looping for me in deck_multiple_loops but did not work how I planned
        #BELOW, should do this in a separate method in Bag_of_Tiles
        for j in frequency_list:
            i = 1
            while i <= int(j):
                deck.loop_over_dict(j)
                i += 1
        deck.shuffle_bag()
        
        for iterator in range(7):
            deck.take_out_tile(current_Player.player_tiles)
        print(current_Player.print_tiles())

    else:
        print("Well it's your loss!")


main()