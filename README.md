# Ghost-Ping
Selfbot for ghost pinging.
### Python Usage
If you wish to run python source, 
- Download python 3.6 + 
- Run `pip install -r requirements.txt`
- Put token into to token.json
- Run `main.py`
### Running Exe 
If you wish to avoid installing python and its dependencies, you can run the EXE. 
- On the right there is a "releases" tab.
- Download latest version.
- Extract to a folder. 
- Change `token` in token.json to your user token. 
- Run the `ghost(version).exe` file. 
### Android
It is possible to use this on android. 
- On the app store search and download "Termux"
- Open the app and paste this command `git clone https://github.com/Greenpilot4/ghost-ping.git`
- Note that if this command does not work install git with `sudo apt-get install git`
- Then type `cd ghost-ping`
- After that type `pip install -r requirements.txt`
- Once done you can then run the program with `python main.py`
- If python or pip do not work run `sudo apt-get install python pip
## Getting User Token 
1. Press Ctrl+Shift+I on Discord to show developer tools.
2. Navigate to the **Application** tab.
3. Select Local Storage > https://discordapp.com on the left.
4. Filter by **Token**.
5. Press Ctrl+R to reload.
6. Find token at the bottom and copy the value
![image](https://camo.githubusercontent.com/cadf3467f8b9da2c41c370a4e12860b06ca61925f3b9f673ef4573e8c7509ac0/68747470733a2f2f692e696d6775722e636f6d2f6a68674f554c702e676966) 
## Bot Usage
First enable developer mode. 
1. Click Appearance under App Settings on the left hand side.
2. In the Appearance settings on the right, scroll all the way to the bottom to the Advanced section and click the switch to the right of Developer Mode .
- When asked for "who you would like to ping" right click on the desired user and hit "Copy ID" then put a @ in front of ID. 
- When asked for "where you would like to ping" right click the channel, for example general and "Copy ID".
![image](https://i.imgur.com/KYKLO9v.png)
# Disclaimer
Selfbots officially violate Discord ToS. I take no responsibility for consequent actions taken against user accounts.
