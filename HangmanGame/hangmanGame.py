
import random
import hangman_art
import hangman_words

answer = random.choice(hangman_words.word_list)
ans = list(answer)
print(len(answer))
toTest = ""
for i in range(0, len(answer)):

  toTest += "-"
print(toTest)


guesses = input("Guess a lette: ").lower()
End_Game = False
count = 6
lives = hangman_art.stages

while not End_Game:
  
  if guesses in ans:
    guess_idx = ans.index(guesses)
    toTest=list(toTest)
    toTest[guess_idx] = guesses
    toTest = "".join(toTest)
    ans[guess_idx] = "-"
 
    print(f"You got it\n {toTest.upper()}")
    
    if "-" not in toTest:
    
      print("You win!")
      End_Game = True
    else:
    
      guesses = input("keep guessing: ").lower()
  else:
    count -= 1

    print("Your guess is not right. You lose one life.")
    print(lives[count])
    
    if count == 0:
      print(f"You lose all lives! \nThe word is {answer.upper()}. ")
      
      End_Game = True
    else:
      guesses = input("keep guessing: ").lower()
    
    