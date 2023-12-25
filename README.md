# xrps-minting-bot
A python bot to mint xrps using xrpl library

## Get Your Private Key

Xaman/Xumm wallet does not provide the secret key. We need to obtain the key from https://secret-numbers-to-family-seed.xumm.dev/ . Enter the numbers that your wallet gave to you when creating the wallet.

I am not affiliated with the website. Use at your own risk. 

## Installation



  ### For Windows Users
  If you don't have Python installed on your machine, follow these steps:
  
  1. Watch this [video tutorial](https://www.youtube.com/watch?v=ERcsRnUQ64s) for a visual guide on installing Python on Windows.
  
  2. Alternatively, you can follow the written instructions below:
  
     - Open your web browser and go to the [official Python website](https://www.python.org/).
     - Navigate to the "Downloads" section.
     - Click on the "Latest Python 3 Release" link.
     - Scroll down to the "Files" section, and depending on your system (32-bit or 64-bit), choose the installer that says "Windows x86-64" for 64-bit or "Windows x86" for 32-bit.
     - Run the installer, and during the installation, make sure to check the box that says "Add Python to PATH" for easier command-line access.
     - ![image](https://github.com/EminnM/XRPS-minting-bot/assets/63583116/48e43f9a-218d-4995-9bf6-db221df52a32)
     - Click "Install Now" and follow the on-screen instructions.
     - After installing Python, open your terminal and verify the installation by typing:
       ```bash
       python --version
       ```

       You should see the installed Python version. And then type

         ```bash
         pip install xrpl-py
         ```
         and then
         ```bash
         pip install pwinput
         ```
        #### If you have git installed
        ```bash
        git clone https://github.com/EminnM/xrps-minting-bot
        cd xrps-minting-bot
        minting-bot.py
        ```
        #### If you don't
       Navigate to the GitHub repository.
       Click on the green "Code" button.
       Select "Download ZIP."
       Extract the ZIP file to your desired location.
       Open the terminal and navigate to the extracted folder:
       ```bash
       cd path/to/xrps-minting-bot
       minting-bot.py
       ```

       




  

  ### For MacOs Users
  If you don't have Python installed on your machine, follow these steps:
  
  1. Watch this [video tutorial](https://www.youtube.com/watch?v=5zX1MkAHdKU) for a visual guide on installing Python on Mac.
  
  2. Or open your web browser and go to the [official Python website](https://www.python.org/).

     -Navigate to the "Downloads" section.

     -Click on the "Latest Python 3 Release" link.

     -Scroll down to the "Files" section, and you'll see macOS installers. Choose the installer that matches your system.

     -Run the installer, and during the installation, make sure to check the box that says "Add Python to PATH" for easier command-line access.

     -Click "Install Now" and follow the on-screen instructions.

   - After installing Python, open your terminal and verify the installation by typing:

     ```bash
     python --version
     ```

     You should see the installed Python version. And then type

     ```bash
     pip install xrpl-py
     ```
     and then
      ```bash
     pip install pwinput

     ```
      #### If you have git installed

        ```bash
        git clone https://github.com/EminnM/xrps-minting-bot
        cd xrps-minting-bot
        python3 minting-bot.py
        ```
     #### If you don't
      Navigate to the GitHub repository.
      Click on the green "Code" button.
      Select "Download ZIP."
      Extract the ZIP file to your desired location.
      Open the terminal and navigate to the extracted folder:
       ```bash
       cd path/to/xrps-minting-bot
       ```
       To run the bot
       ```bash
       python3 minting-bot.py
        ```



  
  ### For Linux Folks
  Install python if you dont have already. 
  Install ```xrpl-py``` and  ```pwinput``` libraries then run the  ```minting-bot.py```
  


That's it

## Donate

If you find this project helpful and would like to support its development, you can make a donation using one of the following cryptocurrencies:

### Solana (SOL)

Solana Address: `2RPXEvbxwMtJf9pk72riDS4JTfNUKPG3HhTNhwos9Eiz`

### XRP (XRP)

XRP Address: `rLSLSfsaQpfsdxGuiLso8tE9HtyBqQQfJN`

### Ethereum (ETH)

Ethereum Address: `0xfca401bA530777809841d56508083522c24C2BEe`

Your contributions are greatly appreciated!




