File list
------------
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

