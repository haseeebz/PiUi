
# Poller
Allows you to poll a function or a shell script and assign it to the property after the indicated interval.

## Methods

### Poll
This is the only thing you need to create a poll.
###### Arguments
+ interval: The polling interval in seconds, 
+ func: function which you want to call.
+ shell: The shell script you want to run
+ typeCastForShell: Since shell output is always a string, you can type cast it into some simple type like bool, int etc

> NOTE: Either func or shell can be assigned. The poll runs once on startup and then runs periodically after the interval