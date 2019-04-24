#README
This will complete your timesheets in the RAPID environment automatically

#GETTING STARTED
   0. Needs Python 3 to run
   1. Write an 'timesheetsbatch.json' file where every employee is an entry with the following fields:
      * username, password, commands, timesheet
      * Commands is the series of terminal commands needed to get to the timesheet screen
      * Timesheet is a comma separated array for every day of the week (Mon - Sun) in two digit form, with the job code as the first entry

#VALID TIMESHEET
      {
        "username": "",
        "password": "",
        "commands": ["dd","XXXX","dd"],
        "timesheet": "CODE,dd,dd,dd,dd,dd,,,"
      }

#TODO
* Use [SimpleCrypt](https://blog.ruanbekker.com/blog/2018/04/29/encryption-and-decryption-with-simple-crypt-using-python/) to encode passwords
* Use Anthony's frontend to schedule users' jobs
* Get Windows VM to run this as a service
* Find possible fail points to check for
* Email or return a screenshot of timesheet
* Allow option for a series of terminal commands which are not the same as mine
* Check if the timesheet code is a correct one, get a list of all of them

