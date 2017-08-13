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
        
    * Copy source code to Instance which you made above. you can put that source code on *C://workspace* path.
    

    
# Note

After you have already set new instance,then you can snapshot this instance to create custom AMI.

We can use this custom AMI directly to create multi-instance at once.