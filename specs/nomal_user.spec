User Journey of Nomal User
==========================
Created by yzhou on 06/06/2017
This is a list of scenarios covering basic user journey.
Need to delete timecards on current week before running.
     
Normal user should submit timecard successfully
-----------------------------------------------

tags: regression, normal

* I go to previous week
* I should see "2" approved timecards
* I go to following week
* I should see "0" approved timecards
* I should see "1" entries
* I click "Copy from Previous Week"
* I should see a dialogue "Copy from previous week?"
* I click "Copy"
* I should see "0" approved timecards
* I should see "2" entries
* I delete the entry at index "1"
* I should see a dialogue "Delete timecard for this project?"
* I click "Delete"
* I should see "1" entries
* I click "SUBMIT"
* I should see a dialogue "Submit timecard from this week for approval？"
* I click "Submit"
* I should see a message "Timecard Approved"
* I click "OK"
* I should see "1" approved timecards
* I should see "1" entries


Normal user should see all kinds of error messages
--------------------------------------------------

tags: regression, normal

* I should see "1" approved timecards
* I should see "1" entries
* I enter project selection list
* I should see "TW TechOps - Finance Invoicing-Beijing-2017-04-05"
* I should see "TW Time Off - Non-sick leave"
* I search "AA"
* I should see "Please type at least 4 letters to search"
* I search "AAAA"
* I should see "AAAAAAAA" in "MY ASSIGNMENTS"
* I should see "No matching results found" in "GLOBAL PROJECTS"
* I click the clean button
* I should see "AAAAAAAA" in "MY ASSIGNMENTS"
* I should see "TW Time Off - Non-sick leave" in "RECENT PROJECTS"
* I choose project "TW Time Off - Non-sick leave"
* I should see "Public holiday" in "SUB PROJECT"
* I click the left arrow to go back
* I should see "AAAAAAAA" in "MY ASSIGNMENTS"
* I should see "TW Time Off - Non-sick leave" in "RECENT PROJECTS"
* I click the left arrow to go back
* I should see "TW Time Off - Non-sick leave" as project in the entry
* I should see "Sub-Project" as sub-project in the entry
* I click "Billable"
* I should see the billable value is true
* I click the hours on "Saturday"
* I should see the keyboard
* I should see my input area at "Saturday"
* I input "-2"
* I click "Next"
* I should see the keyboard
* I should see my input area at "Sunday"
* I input "26"
* I click "Next"
* I should see the keyboard
* I should see my input area at "Notes"
* I close the keyboard
* I click "Copy from Previous Week"
* I should see a dialogue "Copy from previous week?"
* I click "Copy"
* I should see "1" approved timecards
* I should see "3" entries
* I click "SUBMIT"
* I should see a dialogue "Submit timecard from this week for approval?"
* I click "Submit"
* I should see a message "Timecard was not submitted"
* I should see error messages as below
|Error Number|Text|
|1|"Sunday can not be more than 24 Hrs."|
|2|"A Timecard may only be marked as Billable if its Project is Billable and its Assignment, if any, is Billable."|
|3|"You must indicate your Work Location for each row when saving a timecard."|
|4|"Timecard with negative hour is not allowed."|
|5|"You must indicate the Sub Project Code for each row when saving a timecard."|
|1|"Sorry, you have already submitted a timecard with the exact same date, hours and project information. Please try avoid submitting duplicated timecards. Thanks."|
* I click "GO BACK"
* I should see "2" approved timecards
* I should see "2" entries
* I logout