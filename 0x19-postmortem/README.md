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

At 5;14 PM WAT, a configuration change was unwittingly released to our webserver without first being released to the testing environment. The change specified an invalid configuration command and an incorrect spelling of the file path to a library that is widely used by our webserver. This affected the successful reboot of our webservers, and hence two of our servers became down at 5:25 PM WAT. As soon as the outage began, our recovery system quickly activated a stand-by webserver, which was reserved for cases like this, and the load balancer began directing all traffic to the active webserver. Unfortunately, the active webserver didn't last long before it also crashed because the requests which were being directed to it by the load balancer were enormous for it to handle. The third server began to repeatedly execute a restart as it attemped to recover, and in 5:35 PM WAT, the service outage began fully.

**Resolution and Recovery**

At 5:35 WAT, the monitoring systems alerted our engineers who investegated and quickly announced the issue. By 5:40 PM, the response team identified that the monitoring system was magnifying the problem caused by this bug

At 5:50 PM, we attempted to rollback the erroneous configuration change. The rollback failed due to some missing files and inadequate file permisisons on the log file which was supposed to be used for the fix. These issues were addressed and successfully rolled back at 6:20 PM

Some services started to slowly recover, and we ascertained that the overall recovery would be faster by a restart of all of the webservers and API infrastructure servers. To aid the recovery, we turned off some of our monitoring systems whcih were triggering the bug. Thus, we decided to engage in a wide scale restart since our server systems are not large enough to trigger cascading failures. By 6:40 PM, 75% of the traffic was restored and 100% of traffic was routed to the API infrastructure at 6:42 PM.

**Corrective and Preventive Measures**

Yesterday, we conducted an internal review and analysis of the outage. The following are actions we are taking to address the underlying causes of the issue to help prevent recurrence and improve response times:
- Disable the current configuration release mechanism until safer measures are implemented. (Completed)
- Change rollback process to be quick and robust.
- Fix libraries and monitoring to crrectly timeout/interrupt on errors.
- Progammatically enforce staged rollouts of all configuration changes.
- Improve auditing processes of high-risk configuration options.
- Simulate rollouts of all configuration changes to get a sense of the changes' impacts.
- Include a time efficient rollback mechanism and improve the traffic ramp-up process, so that any future problems of this type can be corrected quickly.
- Develop better mechanism for quickly delivering status notifications during incidents.