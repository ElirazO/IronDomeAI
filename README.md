# AI Iron Dome


![](/image/IronDomeAI.png)

Specification:
1.	This is a realization of genetic algorithm that simulates evolution (NEAT).
2.	80 games are running simultaneously in the background in each generation.
3.	As long as a green rocket doesn’t hit the ground the game continues.
4.	A game gets one point when a blue rocket hits a green rocket.
5.	The screen will display the most successful game for 10 seconds. If there is more successful game the screen will jump to it in 10 seconds, otherwise the game will remain until the game is over.
6.	‘GEN’ shows the number of generations that have passed.
7.	Each launcher (game) has a brain that controls the blue rocket in order to intercept a green rocket.


![](/image/nn.png)


8.	Each population inherits the weights of the most successful pair in the previous-generation with added noise that simulate mutation. (As evolution works)
9.	Sometimes the convergence comes in later generations, but in most cases, you can see a game that reaches a high score (200-300) in the early generations (5-10). 
10.	You will see various interesting behaviors of green rocket prediction and self-developing strategies.
