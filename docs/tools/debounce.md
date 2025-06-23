
# Debounce

Calls a function atleast once in a given duration. This is useful if you want to prevent spam calls. It's simply a decorator that you can put on a function.

+ interval : The duration in which a function must be called. If a function call is made before the duration ends than the function is not called.

## Example
This function can only be called once every 2 seconds.
```python
Pi.Debounce(2)
def searchApps():
	pass
```