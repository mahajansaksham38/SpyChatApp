from spy_details import spy,Spy,friends,ChatMessage
from steganography.steganography import Steganography
from datetime import datetime
from termcolor import colored
import os.path

STATUS_MESSAGE=['My name is Bond, James Bond', 'Shaken, not stirred.', 'Keeping the British end up, Sir']         #list to store available statuses
SALUTAIONS=['MR.','MRS.','DR.','ADV.','MISS.','ER.']                                                               #list  to store salutations

print "Hello! Let\'s get started"

#Funtion that takes name(string) arguement and return true if name is valid otherwise false
def valid_name(name):
        name=name.strip()                                   #strip() removes the whitespaces from start and end of the string
        name1=name.split(" ")                               #split() splits the string by spaces storing words in a list
        a=0
        b=0
        for i in name1:                                     #for loop iterates over each word in the name1 list
            if(i.isalpha()):                                #isalpha() returns true if srting has only alphabets, false otherwise
                a +=1                                       #increment a by 1 in i is isalpha()
            else:                                           #otherwise b is incremented by 1
                b+=1
        if (b>0):                                           #return false if b is greater than 0
            return False
        elif(b==0):                                         #return true if b==0
            return True

#this function  validates rating to be entered and returns rating if its valid
def valid_rating():
    #loop runs until valid rating is enterd
    while True:

        #if user enters some character other than float number then ValueError is generated which is handled by try-except block
        try:
            rate = raw_input("Your Spy ratings :\t")                     #ask for user input for spy rating
            if len(rate) == 0:
                while True:                                              #if length of entered rating is 0, loop runs until user enters valid input
                    print colored("WARNING: Please enter spy's rating.It cannot be left empty", 'red')
                    rate = raw_input("Your Spy ratings :\t")             #again asking for user input
                    if len(rate) != 0 and rate.isspace() == False:       #makes sure length of input is not 0 and not have just whitespaces
                        rate = float(rate)
                        break
                    else:
                        pass
            else:
                rate = float(rate)
            break                                                      #loop stops and rate is returned at end if its valid

        #if length of input is not 0 but error occurs then except block is executed and outer loop continues
        except ValueError:
            print colored("Please enter valid rating of spy", 'red')
            pass

        #return valid rate vlalue
    return rate
#valid_age() returns valid age, its logic is almost same as valid_rating() method
def valid_age():
    while True:
        try:
            age = raw_input("Your Spy age :\t")
            if len(age) == 0:
                while True:
                    print colored("WARNING: Please enter valid spy's age", 'red')
                    age = raw_input("Your Spy age :\t")
                    if len(age) != 0 and age.isspace() == False and age.isdigit()==True:
                        age = int(age)
                        break
                    else:
                        pass
            else:
                age = int(age)
            break
        except ValueError:
            print colored("Please enter valid rating of spy", 'red')
            pass

    return age

#making a function add_status(takes one arguement status_message) that add new status or select status from old statuses acc to user response
def add_status(status_message):

    updated_message=None                                                                  #assigning None to updated_message variable which will later store status updated
    if status_message != None:                                                            #if status_message is not none
        print "Your current status is: " +status_message                                  #print current status
    else:
        print "You don't have any status at the moment"                                   #print user doesnt have any status

    default=raw_input("Do you want to select from older status(Y/N): ")                   #asking user if he/she wants to select from older status or not

    if default.upper()== "N":                                                             #if user select enter n
        while True:                                                                       #loop keep executing if message is empty or has all whitespaces
            new_status_message=raw_input("Enter your new status: ")                       #ask user to enter new status
            if len(new_status_message)>0 :                                                #update_message stores new status and appends to STATUS_MESSAGE list
                if new_status_message.isspace()==False:
                    updated_message=new_status_message
                    STATUS_MESSAGE.append(new_status_message)                             #appends new_status_message in STATUS_MESSAGE list
                    break                                                                 #loop ends if new status is updated
                else:
                    print "Message cannot be empty"
                    pass

    elif default.upper()== "Y":                                                           #if user enters y list of old messages will be appeated

        item_number=1
        for message in STATUS_MESSAGE:                                                    #for loop for printing out old statuses
            print str(item_number)+' '+str(message)
            item_number+=1
        status_selection=raw_input("Choose from above statuses: ")                        #asking user for status selection

        if status_selection.isspace()==False and len(status_selection)>0:
            if len(STATUS_MESSAGE)>= int(status_selection):
                updated_message=STATUS_MESSAGE[int(status_selection)-1]
            else:
                print "You didn't select valid option"

    else:
        print "The option you chose is not valid ! Press y or n. "

    if updated_message:                                                                   #This block prints updated status if updated_messae has new status
        print 'Your updated status message is: %s' % (updated_message)
    else:
        print 'You did not update your status message'

    return updated_message

#making a function to add friend
def add_friend():

    new_friend = Spy("","",0,0)                                                           #initializing object to empty values

    #asking input from user
    name = raw_input("Welcome, Please enter your spy name: ")                             #ask user for name
    name_check = valid_name(name)                                                         #call valid_name function
    if name_check == True:                                                                #if valid_name returns true then ask for salutation
        salutation= raw_input("Are they 'MR.' or 'MRS.' or 'DR.' or 'ADV.' or 'MISS.' or 'ER.'?: ")
        if salutation.upper() in SALUTAIONS:                                              #if entered salutation exist in SALUTATIONS list then code runs further
            new_friend.salutation=salutation
            new_friend.name = new_friend.salutation + " " + name
            new_friend.age=valid_age()                                                    #calling valid_age() funtion
            new_friend.rating = valid_rating()                                            # calling valid_rating() funtion

            #validating inputs from user and appending to friend list
            if new_friend.age> 12 and new_friend.rating >= spy.rating:                  #age should be greater than 12 and rating should be greater than current spy rating
                friends.append(new_friend)
                print 'Friend Added!'
            else:
                print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'
        else:                                                                             #if entered salutation is not in SALUTATION list then print message and exit to menu
            print colored("Invalid salutation!!",'red')
            print colored("Choose from: 'MR.','MRS.','DR.','ADV.','MISS.','ER.' ",'blue')

    else:
        print colored("Entered name is not valid. Try again!",'red')
    return len(friends)

#making select_friend() function to select friend returns index of friend in friends list
#if valid friend is not selected it returns None
def select_friend():

    item_number = 0

    #for loop iterate through friends list and print the list of friends
    for friend in friends:
        print '%d. %s aged %d with rating %.2f is online' % (item_number + 1, friend.name,
                                                             friend.age,
                                                             friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")                           #ask user for user input to choose from friends
    if len(friend_choice)>0 and friend_choice.isdigit():                            #isdigit() checks if input has only numbers then return true otherwise false
            friend_choice=int(friend_choice)
            if friend_choice<item_number+1:                                         #friend_choice should be valid number of friend otherwise print message
                friend_choice_position = friend_choice - 1
                return friend_choice_position
            else:
                print 'Choose number between (1--%s)' %(item_number)
                return None
    elif len(friend_choice)==0 or friend_choice.isspace()==True:                    #if length of friend_choice is 0 or contains only whitespaces then return None
            print 'Choose number between (1--%s)' % (item_number)
            return None
    else:
            print 'Choose number between (1--%s)' %(item_number)




#function to send message using encode() METHOD  of Steganography
def send_message():
    friend_choice = select_friend()                                             #calling select_friend() and stores the index in friend_choice
    if friend_choice==None:                                                     #if friend_choice is not valid then prints message and exit to menu
        print colored("Try again",'blue')
    else:
        original_image = raw_input("What is the name of the image?")            #asking for image path which is to be encoded

        if os.path.isfile(original_image):                                      #checks for valid image path
            output_path = "output.jpg"
            text = raw_input("What do you want to say? ")                       #asking input message to be sent
            if len(text)>0 and text.isspace()==False:
                Steganography.encode(original_image, output_path, text)         #encode() encodes the text in image provided
                new_chat = ChatMessage(text, True)                              #object new_chat of class ChatMessage
                friends[friend_choice].chats.append(new_chat)                   #append object in spy's chat list
                print "Your secret message image is ready"
            else:                                                               #if message is empty or contains only whitespaces message is printed
                print colored("Oops! Seems like your message has no text. Try again!",'red')
        else:
            print colored("Path you provided for image was not valid.",'red')

#function to read message using decode() method of Steganography
def read_message():

    sender = select_friend()                                                    #call to select_friend()
    if sender==None:                                                            #if selected friend is not valid print message otherwise continue
        print colored("Try again", 'blue')
    else:
        output_path = raw_input("What is the name of the file?")                #asking for image path to be decoded
        if os.path.isfile(output_path):                                         #checks if given image path is valid(returns true if valid), if no it prints a message & exit to menu
            secret_text = Steganography.decode(output_path)                     #decode() takes path of encoded image and return the decoded message
            if len(secret_text)>0 or secret_text.isspace()==False:

                #print message if message contains sos or save me or need help
                special_words=['SOS','SAVE ME','NEED HELP']
                if secret_text.upper() in special_words:
                    print colored('Alert! This is emergency message: '+ secret_text,'red')

                #counts and print average word count of messages in chat
                words=secret_text.split()
                friends[sender].average=(float(friends[sender].average*len(friends[sender].chats)+len(words)))/(len(friends[sender].chats)+1)
                print "Average word count is: %.2f" %(friends[sender].average)


                new_chat = ChatMessage(secret_text, False)
                friends[sender].chats.append(new_chat)              #appends the new_chat object details to chats list of friend
                print "Your secret message has been saved!"

                if len(secret_text.split())>100:                    #if length of message is more than 100 words friend is deleted
                    print colored("You are speaking to much.We are deleting you.",'red')
                    friends.pop(sender)
            else:                                                   #if decode message is empty then print message
                print colored("Looks like your message is empty.Try again",'red')
        else:                                                       #if image path is not valid then prints messsage and exit to menu
            print colored("Path you provided for image was not valid.", 'red')

#function to read chat history
def read_chat_history():

    read_for = select_friend()                                              #select friend to read chat of
    print '\n'

    for chat in friends[read_for].chats:                                    #loop runs through chat list of selected friend and prints messages with time
            if chat.sent_by_me:
                print colored([chat.time.strftime("%d %B %Y")],'blue'),     #prints time in blue text
                print colored('You said: ','red'),                          #prints user in red text
                print chat.message
            else:
                print colored([chat.time.strftime("%d %B %Y")],'blue'),
                print colored(friends[read_for].name+' said: ','red'),
                print chat.message

#function to start chat takes current spy object as argument
def start_chat(spy):

#setting user status to None at starting
    current_status_message = None
    spy.name=spy.salutation+" "+spy.name

    if spy.age > 12 and spy.age< 50:

        print "Authentication complete. Welcome " + spy.name+ " age: " + str(spy.age) + " and rating of: " + str(
            spy.rating) + " Proud to have you onboard"

        #prints a particular message for specified rating
        if spy.rating > 4.5:
            print 'Great ace!'
        elif spy.rating > 3.5 and spy.rating <= 4.5:
            print 'You are one of the good ones.'
        elif spy.rating >= 2.5 and spy.rating <= 3.5:
            print 'You can always do better'
        else:
            print 'We can always use somebody to help in the office.'

        show_menu = True

        #loop run while show_menu is true
        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)                                  #asking user to select from menu

            if len(menu_choice) > 0 and menu_choice.isspace()==False:
                menu_choice = int(menu_choice)
                if menu_choice == 1:                                               #status update if choice is 1
                    print 'You chose to update the status'
                    current_status_message=add_status(current_status_message)      #call add_status function with current status as argument
                elif menu_choice == 2:
                    print "You selected option to add a friend"
                    number_of_friends=  add_friend()                               #call add_friend function

                    print 'You have %d friend(s)' %(number_of_friends)
                elif menu_choice == 3:
                    send_message()                                                 #call to send_message funtion if choice is 3
                elif menu_choice == 4:
                    read_message()                                                 #call to read_message funtion if choice is 4
                elif menu_choice == 5:
                    read_chat_history()                                            #call to read_chat_history() function if choice is 5
                elif menu_choice==6:                                               #exit application if choice is 6
                    exit()
                else:
                    print colored("Enter correct choice",'red')
            else:                                                                  #if user enter invalid menu option then prints message
                print colored('Please enter a valid option','red')
    else:                                                                          #print message if age of spy is not appropriate (in red)
        print 'Sorry you are not of the correct age to be a spy'

while True:
    question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "  # asking user if he wants to continue as current spy or not
    existing = raw_input(question)

    #if user wants to continue as current spy call start_chat function
    if existing.upper() == "Y":
        start_chat(spy)
        break
    #else user will enter new spy details to continue
    elif existing.upper()=="N":

            name=raw_input("Welcome, Please enter your spy name: ")
            name_check=valid_name(name)
            if name_check==True:
                salutation = raw_input("Should I call you 'MR.' or 'MRS.' or 'DR.' or 'ADV.' or 'MISS.' or 'ER.'? :\t")
                if salutation.upper() in SALUTAIONS:

                    spy.age = valid_age()
                    if spy.age<50 and spy.age>12:                                           #checks if age is between 12 and 50
                        spy.name = name
                        spy.salutation = salutation
                        spy.rating=valid_rating()
                        start_chat(spy)
                    else:                                                                    #if age is not correct prints message
                        print colored("Sorry you are not of correct age to be a spy!!",'red')
       
                else:                                                                        #if salutation is not in list then print message
                    print colored("Invalid salutation!!", 'red')
                    print colored("Choose from: 'MR.','MRS.','DR.','ADV.','MISS.' ,'ER.'", 'blue')

            else:                                                                            #if name entered is not valid print message
                print colored("Entered name is not valid. Try again!",'red')

    else:                                                                                   #if user enters other than y or n then prints message and loop continues
        print colored("Please choose from y or n",'red')
        pass





