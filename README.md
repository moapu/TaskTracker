File list
=========
speechrecognition.py <br/>
setup.py <br/>
saveToMongo.py <br/>
main.py <br/>

General Usage Notes <br/>
------------------------
Upon Starting this application the input allows the user to prompt for an voice command after its been activated to ***Listening*** <br/>
the user is then allowed to say a command. <br/>
Example of a command would be ***Start Timer for Laundry***, the command will process that voice and then record that data <br/>
into the Mongo Database we have created. <br/>
The result of this will track every set of voice data, the command won't end here. User have to say ***Stop Timer*** once <br/>
this happen the user will be able to save their according time into the database. If the user wants to backtrack what they did <br/>
in that specific time they can say something like ***What's my time for Laundry*** and then the database for laundry will <br/> 
be displayed. However, you'll need to manually using voice command to shut the system down. This is done by saying ***close***

Speechrecognition.py
--------------------
Purpose of this is to create a API speech functionality for the rest of the program; the general goal we focus on is how to get the
end user to identify the command and respond with the appropriate one.

Speechrecognition.py<br/>
 class SpeechApp:

    def __init__(self):
        """ RECOGNIZER """
        self.r = sr.Recognizer()

    def mic_input(self):
        """ return the microphone input """

        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source)
            print("\t*** {} ***".format("LISTENING"))
            return self.r.listen(source)
           
User input will be taken into accountability throughout the listening function of these methods. 

Setup.py<br/>
------------
Install all the nessecary requirement for the process.

def install(package):

    subprocess.call([sys.executable, "-m", "pip", "install", package])

saveToMongo.py
--------------
The function of saveToMongo include the following: <br/>
1. Save task with a allocated time<br/>
2. Return all entry from the mongo database <br/>
3. return one entry from the mongo database <br/>
4. delete an whole entry <br/>

main.py
------

The last file will allow the entire program to run. <br/>

        # === TITLE ===
         +------------+
         | SPEECH APP |
         +------------+
        
        *** LISTENING ***
         
        ================
        DURATION: 15 sec
        ================
  
  



