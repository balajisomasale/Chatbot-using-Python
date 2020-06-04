'''
play_word() — a function that would take in a player and a word, and add that word to the list of words they’ve played
update_point_totals() — turn your nested loops into a function that you can call any time a word is played
make your letter_to_points dictionary able to handle lowercase inputs as well'''


letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#List/Dictionary Comprehension=> Getting all the key-value pairs in zip of two lists
#List Comprehenshion is eqivalent to Lambda Expression in Java
letter_to_pointers={key:value for key,value in zip(letters,points)}

letter_to_pointers[" "]=0
print(letter_to_pointers)

#Calculating each letter score count for the given 'word'
def score_word(word):
    point_total=0
    for i in word:
        point_total+=letter_to_pointers.get(i,0)
    return point_total

#Testing Brownie count here
brownie_points=score_word("BROWNIE")
print(brownie_points)

#Taking a Example
player_to_words={"player1":["BLUE","TENNIS","EXIT"],"wordNerd":["EARTH","EYES","MACHINE"],"LExi Con":["ERASER","BELLY","HUSKY"],"Prof Reader":["ZAP","COMA","PERIOD"]}


player_to_points={}

#Iterating through the Items in a dictionary
for player,words in player_to_words.items():
    
    player_points=0
    #Get each element in words
    for word in words:
        player_points +=score_word(word)  #Calling the function written and passing the word to count the letters 
    player_to_points[player]=player_points #Setting the player points to each Player 
print(player_to_points)





