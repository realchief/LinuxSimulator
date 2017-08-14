# Simulate-user-Activity-ubuntu
This simulation script is working on Ubuntu.

# Directory Structure.

- automate_lib : Includes base functions to process with windows handler and browser.
    * baseFunctions.py : 
    * Browser.py :
    * const.py :
    * keyboard.py :
    * Taskbar.py :
    * ubuntu_wmctrl.py :
    * web.py :
    * winlaunch.py :

- simulate_ubuntu.py : This file is main file to start simulate.

- urls.csv : includes 500 popular urls to browse randomly.


# Setup on new Instance.

- Step 1: 
    
    * First run the script with these parameters.
        
    ```
        python create_instance.py -f -l
    ```

- Step 2: 
    
    * At first, use puttygen to generate ppk file to connect via ssh.
    * use putty to connect Ubuntu Instance (username: ubuntu, private key file: ppk file generated above.).
    
- Step 3:
    
    Assuming you are in putty ssh window now.
    
    * In order to run Ubuntu GUI (hosted on AWS EC2) on your Windows host, 
      follow these instructions to install Ubuntu desktop & TightVNC server on Ubuntu:
    
    ```
        [ubuntu] sudo apt-get update
        [ubuntu] sudo apt-get install ubuntu-desktop
        [ubuntu] sudo apt-get install tightvncserver
        [ubuntu] sudo apt-get install gnome-panel gnome-settings-daemon
     ```
        
    * Launch VNC server to create an initial configuration file:
    
    ```
        [ubuntu] vncserver :1
    ```
    
    * Open the configuration file in nano:
    ```
       [ubuntu] nano ~/.vnc/xstartup
    ```
    
    * Edit the configuration file to look like this. After you’re done, enter Ctrl + X and ‘Y’ to save it.
    
    ```
        #!/bin/sh
        export XKL_XMODMAP_DISABLE=1
        unset SESSION_MANAGER
        unset DBUS_SESSION_BUS_ADDRESS
        
        [ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup
        [ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources
        xsetroot -solid grey
        
        vncconfig -iconic &
        gnome-panel &
        gnome-settings-daemon &
        metacity &
        nautilus &
        gnome-terminal &
    ```
    
    * Kill and restart the VNC server to apply the settings. This needs to happen each time the VNC / X-Windows configuration is updated.
    
    ```
        [ubuntu] vncserver -kill :1
        [ubuntu] vncserver :1
    
    ```
    
- Step 4

    If you’re on Windows, download Tight-VNC to install VNC. Connect to <Ip Address>::5901 and use the password you gave above. 
    You should now see your new shiny Ubuntu desktop.
    
    
- Step 5

    Copy source code folder *workspace_ubuntu* to /home/ubunut/workspace_ubuntu on instance.
    
    
# Note

After you have already set new instance,then you can snapshot this instance to create custom AMI.

We can use this custom AMI directly to create multi-instance at once.


## In development (TODO)

- Add feature to support Multi-language while writing to libreOffice Document.
- Improve feature to browse random site.
    * Issues
        This is taking long time to browse a site and this is happening on one tab.
    
    * Switch tab while browsing.
    * Speed up to browse a site as possible as similarity to human action.
- Add features to switch between office and browser.
