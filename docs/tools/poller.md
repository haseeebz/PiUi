
# Poller
Allows you to poll a function or a shell script and assign it to the property after the indicated interval.

## Methods

### Poll
This is the only thing you need to create a poll.
+ interval: The polling interval in seconds, 
+ func: function which you want to call.
+ shell: The shell script you want to run
+ typeCastForShell: Since shell output is always a string, you can type cast it into some simple type like bool, int etc

> Either func or shell can be assigned. The poll runs once on startup and then runs periodically after the interval

## Example
In this example, the function gets called every 10 seconds.

```python
label = PiLabel(
	text = Pi.poller.poll(10, func = foo)
)
```
