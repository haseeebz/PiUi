
# Binder
This object allows you to bind the property of a widget to a string. You can then update the propert using the binder.
NOTE: Keep in mind that the binder should only update the property with a valid value type.

# Methods

## Bind
Binds the property to a string.
# Arguments
key -> string to which the property is binded.

## update
Update a given property
# Arguments
key -> string to which the property is binded.
value -> value to which the property is updated. Must be a valid value the property can accept.

## combine
Combines a binder with another binder.
# Arguements
other -> Binder which you want to combine

# Examples

```python
label = PiLabel(
	text = Pi.binder.Bind("text")
)

Pi.binder.update("text", "Hello World!")
```