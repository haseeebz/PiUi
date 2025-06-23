
# Shell

Executes a shell script and returns the output.

* cmd : The script you want to execute. You can use a string if the command is simple, otherwise use a list of strings as you would with subprocess.

> Output : Returns a tuple of (str, bool), If the script ran successfully, the bool is True. If it failed, its false and the stderr is returned as output instead.

## Example

```python
Pi.Shell("systemctl reboot")
```