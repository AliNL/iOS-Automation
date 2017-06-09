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
