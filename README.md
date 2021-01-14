## ➡️ Jumbled_Words_Game 

**It is generally a - 💭A text-based word guessing game.** 

<h4>OUTLINE:</h4>
The game would be of two players, who would turn wise get random words which have jumbled letters. Initially we will start with player one’s turn so player two will have somewording in his/her mind, So what the person does is he would rearrange the letters of the words, basically he would shuffle the words and write those letters in some random order, and present it to player 1, so this person is presented with the shuffled word, he is supposed to guess what the actual word would be. If he is able to guess he would get a point and this person would pose a question to the other person and the game goes on. The players will be given points too, 1 point for correct, 0 for incorrect or no word filling. It will continue until the players selected to stop and in the end, it declares to scores in the score board. This is how the game will go. So, with this kind of strategy let’s play this game using python programming skills

**PREREQUISITE:**
* Knowledge of basic python language and use of libraries
* Have a minimum touch with classes concepts (OOPs)

**LOGIC:**

This will be done in 4 steps:

**1. Create a library of words for the game**

* create a list of words, with as many words you want
* choose a random word in the following way

  pick=random.choice(words)
* return this word

**2. Define a function to jumble words**

* jumble the word in following way:

  jumbled="".join(random.sample(word,len(word)))

* return the jumbled word

**3. Function to give ending lines of game**

* Your choice of presentation
* Scores on the game
* After that a thanking note

**4. Summary of the game**

* declare two variable and take name of players
* declare two variables for points , initially as zero
* declare a turn variable equal to zero
* now start a loop ( while (1) ) , 1 because we want to continue untill the players want
* declare computer’s task to choose a word from library created
* create a question word with the function calling
* print this
* now we use If-Else to create a question answer format similar to both players
* from If we check turn = even then player 1 Else player 2 chance, but the code is same except naming
* first print player name +“ your turn”
* next take input from player
* again use if else to check answer given and update the score
* same for both players code, update value of turn by 1
* now take input to continue = 1 or end = 0
* check if 0 then call thanking function and break the loop
