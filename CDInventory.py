#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# JByrne, 2021-Aug-28, unsucessfully attempted to convert pseudocode to python script.
# JByrne, 2021-Sept-1, completed assignment
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD():
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
    """
       
#fields

#constructor method
    def __init__(self, cd_id, cd_title, cd_artist):
        
        if str(cd_id).isnumeric():
            self.__identity = int(cd_id)
        else:
            raise Exception("Not an integer")
        self.__title = cd_title
        self.__artist = cd_artist

###### ------ identity ------ ######
# DEFINE THE 'GETTER'
    @property
    def identity(self):
        return self.__identity     
        
# DEFINE THE 'SETTER'
    @identity.setter
    def identity(self, value):
        if str(value).isnumeric():
            self.__identity = int(value)
        else:
            raise Exception('Not an integer')

###### ------ title ------ ######
# DEFINE THE 'GETTER'
    @property
    def title(self):
        return self.__title    
        
# DEFINE THE 'SETTER'
    @title.setter
    def title(self, value):
        self.__title = value

###### ------ artist ------ ######
# DEFINE THE 'GETTER'
    @property
    def artist(self):
        return self.__artist
        
# DEFINE THE 'SETTER'
    @artist.setter
    def artist(self, value):
        self.__artist = value
    pass

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # DONE Add code to process data from a file
    def Load_inventory(file_name):
        
        try:
            objFile = open(file_name, 'r')

            for line in objFile:
                cd_data = line.strip().split(', ')
                lstOfCDObjects.append( CD(cd_data[0], cd_data[1], cd_data[2]))
   
            objFile.close()
        except:
            print("\n---No Existing CD Data ---\n")
        
    # DONE Add code to process data to a file
    def save_inventory(filename, list):
        objFile = open(filename, 'w')

        for object in list:
            cd_data = str(object.identity) + ", " + object.title + ", " + object.artist + "\n"
            objFile.write(cd_data)
   
        objFile.close()
        
        
        
        
        
    pass

# -- PRESENTATION (Input/Output) -- #
class IO:
    # DONE add docstring
    """Handling Input / Output"""
    
    # DONE add code to show menu to user
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[i] Display Current Inventory\n[a] Add CD\n[s] Save Inventory to file')
        print('[l] load Inventory from file\n[x] exit\n')

    # DONE add code to captures user's choice
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['i', 'a', 's', 'l', 'x']:
            choice = input('Which operation would you like to perform? [i, a, s, l or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    
    def show_CD_data(object):
        """Takes data from CD object and returns it as a string"""
        show_data = ''
        show_data = str(object.identity) + ', ' + object.title + ', ' + object.artist
        return show_data
    
    # DONE add code to display the current data on screen
    def show_list(list):
        """Shows current inventory list on screen"""
        print("\nCurrent Inventory is:\n----------------------------------")
        for object in list:
            print(IO.show_CD_data(object))
        print("----------------------------------")
   
    # DONE add code to get CD data from user and add to list
    def get_add_CD_data():
        """Asks user for new CD data and adds to object list
        
        Args:
            none
            
        Returns:
            none
            
        """
        cd_data = []
        
        while True:
            strID = input('Enter ID: ').strip()
            try:
                int(strID)
                break
            except:
                print("Please input an integer")
            continue
        strTitle = input('What is the CD\'s title? ').strip()
        stArtist = input('What is the Artist\'s name? ').strip()
        cd_data = [strID, strTitle, stArtist]
        
        lstOfCDObjects.append( CD(cd_data[0], cd_data[1], cd_data[2]))

        
        
########################### -  MAIN SCRIPT BODY - #############################
# DONE Add Code to the main body

# DONE - Load data from file into a list of CD objects on script start
FileIO.Load_inventory(strFileName)

# DONE - Display menu to user
IO.show_list(lstOfCDObjects)

while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # DONE - let user exit program
    if strChoice == 'x':
        break
    
    # DONE - let user load inventory from file
    elif strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled:  ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = []
            FileIO.Load_inventory(strFileName)
            IO.show_list(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_list(lstOfCDObjects)
        continue  # start loop back at top.
    
    # DONE - let user add data to the inventory
    elif strChoice == 'a':
        IO.get_add_CD_data()
        continue  # start loop back at top.
        
    # DONE - show user current inventory
    elif strChoice == 'i':
        IO.show_list(lstOfCDObjects)
        continue  # start loop back at top.
    
    # DONE - let user save inventory to file
    elif strChoice == 's':
        IO.show_list(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        
        if strYesNo == 'y':
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        
        continue  # start loop back at top.
        
    # catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')
###############################################################################


