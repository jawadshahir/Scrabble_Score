
player_to_words= { }
player_to_points={}   
#functions
  #add word that a player got
def play_word(player,word):
    if player in player_to_words:
      player_to_words[player].append(word)
      update_point()
    else: 
       w=[word]
       player_to_words.update({player:(w)})
       update_point()
    
       
  #score word
def score_word(word):
    point_total = 0
    for letter in word:
      point_total += letter_to_points.get(letter, 0)
    return point_total
  #update score
def update_point():
    for player, words in player_to_words.items():
      player_point=0
      for word in words:
        player_point+=score_word(word)
        player_to_points[player]=player_point
 
 


letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]
player=" "

letter_to_points={
    key: value 
    for key, value 
    in zip(letters, points)
    }

while (player!= "exit"):
  
 
  player=input('Please input the player name that got the word or type exit to see the score: ').title()
  

  
  if player=="Exit":
    winner_name= max(player_to_points, key=player_to_points.get)
    winner_pt= max(player_to_points.values())
    print(winner_name)
    print(winner_pt)
    
    print(player_to_points)
    
    print(player_to_words)
    
    print ("Winner is "+ winner_name + " with "+ str(winner_pt)+ " points! ")

  
    
    break
  else:  
    word=input('Please enter the word that the player got: ').upper()
   
    play_word(player,word)
    print(player_to_points)
    print(player_to_words)




  
  