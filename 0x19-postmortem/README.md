# TripiiTech API Infrastructure outage incident report

Feb 21, 2023

#

*By the TripiiTech API Infrastructure Team*

**Issue Summary**

From 5:35 PM to 6:42 PM WAT, requests to most TripiiTech APIs resulted in 404 & 500 error response messages. TripiiTech applications, and GUIs that rely on these APIs returned errors or had limited functionality. The issues affected 100% of traffic to this API infrastructure. Users could not access our website, but were able to access certain APIs that run on a different infrasctructure. The root cause of this outage was an invalid configuration change on our webserver that made two of our webservers inaccessible. As a result, our backup webserver was activated, but shortly went down because of the enormous traffic to it.

**Timeline (all times West African Time)**
- 5:14 PM: Configuration push begins
- 5:35 PM: Outage begins
- 5:35 PM: Pagers alerted teams
- 5:50 PM: Attempted configuration change rollback
- 6:00 PM: Failed configuration change rollback
- 6:20 PM: Successful configuration change rollback
- 6:24 PM: Server restarts begin
- 6:42 PM: 100% of traffic back online

**Root Cause**

