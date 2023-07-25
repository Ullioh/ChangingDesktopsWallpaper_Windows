# ChangingDesktopsWallpaper_Windows
A little program to change the wallpaper in Windows automatically, every time you reboot or startup the PC

The objective of this programs is can change the desktop wallpaper in windows every time tha starup the pc, this .py archive was created with Python and   Unsplash API (obviously) 
This program was built using [Python]([https://pages.github.com/](https://www.python.org/))
to run the .py need installed python and Requests module.

###  Install Requests with 
```
pip install requests
```
With all that, you might running this program with any IDE or console python.

### How to run every time that you startup the pc:
To make a .py file execute on Windows startup, you must follow these steps:
+ Open File Explorer and navigate to the location where the .py file you want to run on Windows startup is located.
+ Right-click on the .py file and select "Create shortcut".
+ Once the shortcut is created, right-click on it and select "Copy".
+ Press the Windows key + R to open the "Run" dialog box.
+ Type "shell:startup" in the dialog box and press Enter. This will open the Windows startup folder.
+ Right-click in an empty space inside the startup folder and select "Paste". This will copy the shortcut of the .py file into the startup folder.
+ Restart your computer, and the .py file will automatically execute on Windows startup.

this method only works if you have administrator permissions on your PC. 

### NOTE:
In the code there is a variable called topic in this you choose the topic or type of image that you want to be placed, you just have to change the topic and then save the file.

### Example 
```
topic = "gundam" # gundam images
topic = "animals" # igames animals
topic = "black" #images black 
```

Enjoyed!
