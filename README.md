# Log_Roller_Beta_v1
The log roller game is starting to take form

GENERAL:
The game is input based right now so pres enter after your input for the action to work.

HOMESCREEN:
In homescreen use "a" and "d" to navigate between selected level.
selected level will have a different box around it not just "#".
avalible levels are have their number visible inside their square, unavalible levels are just 3x3 boxes of "#".
select a level and press "s" to play it.
to save your progress when closing the game press "q", if you just close it your progress will be lost.
press "r" to delete your progress and start from scratch.

IN A LEVEL:
To move use wasd.
to restart the level and move the log back to the starting position press "r".
to quit the level press "q", if you have finished the level before the next level will still be avalible.
"#" are walls.
"-" is the start position.
"+" is the end position.
"@"(1) or "@@"(2) or "@"(3) is the log.

                      @
                      
As shown above the log can have three different states.
(1) is when it is standing up, it will fall down no matter which way you move it.
(2) is when it's laying down horisontal, if yo move it up or down it will roll and stay in the same state, if you move it sideways it will flipp up to state(1).
(3) is when it's laying down vertical, if yo move it sideways it will roll and stay in the same state, if you move it up or down it will flipp up to state(1).
you can not land on top of walls when you move the log, example: "@ #" here you can not move to the right because the log needs two avalible tiles to fall.

HOW TO WIN:
To win a level you have to get the log from the start position to the end position by getting through the puzzel.
The log has to end standing up(state (1)) on the end position to win the level.
You will not win if the log is in state (2) or (3) and one of the parts cover the end position.
When you win a level the next one unlocks.
