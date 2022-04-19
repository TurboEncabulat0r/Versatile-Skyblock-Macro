# Versatile Skyblock Macro Documentation 
Incomplete documentation of Versatile Skyblock Macro, to be updated in the future.
## Discord Bot
The discord bot works based on command and subcommand scripts, the commands interact with the macro by calling spesific names to thier designated macro such as .farmpotato or .farmwart. This is soon to be completely redesigned

The discord bot also has a built in whitelisting system, where you can allow only spesific people to controll the bot, this system is under heavy development untill a good config file manager is setup

### General Commands
These comamnds are used more than most in the bot, they are often used to stop and start the macro or to send the player to a spesific destination.

* **.dc:**  
*Attempts to disconnect the active player from the server, if send reports on it will send a screenshot when finished*

* **.tohub:**  
*Attempts to send the player to the skyblock hub, if send reports on it will send a screenshot when finished*

* **.tois:**  
*Attempts to send the player to /is, if send reports is on it will send a screenshot when finished*

* **.say:**  
*Takes a string as an input and says it in chat, ex `.say hello`
used to force send commands in chat such as when stuck in limbo*

* **.stop**   
*Used to stop the macro*

* **.farmcycle:**  
*Only for the potato farm, it completely resets position of the player by sending them to the hub and back to the is, it will then walk to farm and begin macroing*

* **.startFarming:**  
*acts as a resume farming command, to be used when you stop the macro in the middle of the farm but wish to continue farming, all these systems will be redesigned and consolidated*

* **.netherwart:**
*used to start the netherwart farm, will start from the beginning and reset position*

* **.sugarcane:**
*used to start the sugarcane macro, will reset postion and begin the macro process*

### Direction commands
These are soon to be updated and consolidated into one command, such as `.walk x`, x can be any direction possible within the codebase

Current implementation of this freezes the bot untill its done walking, in the future this needs to run based off of threads.

* **.walkleft:**   
*Used to force the player to walk left, used as `.walkleft x` x can be any number float or int*

* **.walkright:**   
*Used to force the player to walk right, used as `.walkright x` x can be any number float or int*

* **.walkforward:**   
*Used to force the player to walk forward, used as `.walkforward x` x can be any number float or int*

* **.walkback:**   
*Used to force the player to walk back, used as `.walkback x` x can be any number float or int*

## Misc Commands
* **.runtime:**  
*Returns the bots runtime and sends it in chat*

* **.ping**  
*Returns the latency of the bot*

* **.sendreports**  
*Toggels on and off the sending of reports, sending reports meaning sending screenshot after a comamnd completes so the user dosent have to type `.sc`*