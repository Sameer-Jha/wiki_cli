# WIKI CLI

**A Command line <u>*wikipedia search tool*</u>**

**Because *nobody likes to leave the terminal***

**Installation**

This tool is made for linux operating system as of now, Python 3.7+ and Pip required. There are a couple of ways for installation.

1. Installing using the installation script. (You will need to have administrative privilege)

   > - Give the **installer.sh** executable permission
   >
   >   ​	`chmod +x installer.sh`
   >
   > - Make sure you are connected to internet, and run the installer
   >
   >   ​	`sudo ./installer.sh`

2.  Manual Installation.

   > - Installing the dependency packages
   >
   >   `pip install -r requirements.txt`
   >
   > - Installing these packages
   >
   >   - less : `sudo apt-get install less `
   >   - ping (iputils) : `sudo apt install iputils`
   >
   > - Now rename main.py to wiki and copy it to a PATH directory
   >
   >   ​								OR
   >
   >   Set an alias in the rc file for your shell (.bashrc, .zshrc etc)

### Usage

`wiki [-h] [-s SEARCH] [-F] [-i]`

> **optional arguments**:
> **-h, --help**            show this help message and exit
>
> **-s SEARCH, --search SEARCH**
>                      pass term for searching wikipedia
>
> **-F, --full**            output all the pagedata from wikipedia
>
> **-i, --interactive**     Run the tool interactively(CTRL+C to quit)