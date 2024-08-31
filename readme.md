# Undertale Bingo Generator
Undertale Bingo Generator is a bingo board generator for undertale bingo speedrunning. This generator produces json data to be used by [bingosync](https://bingosync.com/) to create a multiplayer interactive bingo board. For the latest release, go to the [Releases](https://github.com/willyjwillyj/Undertale-Bingo/releases/) tab. 

## Usage
Place the goals.txt and either the executable from the releases, or the source files in the same folder, then run the bingo generator. This will open an application where you can press a button to generate a new bingo board. Copy and paste that board into bingosync, so you can start your bingo game.

This board generator is designed and optimized for traditional bingo versions, though alternate bingo versions will work fine.

## Specifications
Bingo goals are listed in goals.txt. A goal is formated as the number 1-3, which represents the goal difficulty tier, 1 being easy, 2 being moderate, and 3 being hard, a space, then the text for the bingo space. The generator will randomly select 5 spaces to be easy, 15 spaces to be moderate, and 5 spaces to be hard goals, such that each row, column, and diagonal contains exactly 1 easy, 3 moderate, and 1 hard goals, then randomly assign goals from each category to the designated spaces, with an equal probability for any goal from that tier being in any possible space. The generator will not assign the same goal to multiple spaces on the same board.

## Modification
This bingo generator, while designed and maintained for the Undertale Speedrunning Community, can be modified to be used by any community for any reason. To modify, replace the goals.txt file according to the specifications above with your own goals, while ensuring that each goal tier has sufficient amount of goals to fill a board.

## Credits
This bingo generator was created by [Svool_Gsviv_](https://github.com/SvoolGsviv) with guidance from the Undertale Speedrunning Community. The interface was created by [willyjwillyj](https://github.com/willyjwillyj). Ongoing development may be fielded from both developers and will be noted as appropriate.