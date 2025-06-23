
# Binder
This object allows you to bind the property of a widget to a string. You can then update the propert using the binder.
NOTE: Keep in mind that the binder should only update the property with a valid value type.

## Methods

### bind
Binds the property to a string.
+ key : string to which the property is binded.

### update
Update a given property
+ key : string to which the property is binded.
+ value : value to which the property is updated. Must be a valid value the property can accept.

### combine
Combines a binder with another binder.
+ other :  Binder which you want to combine

## Example

The of text of label can now be updated from anywhere using binder.

```python
label = PiLabel(
	text = Pi.binder.bind("text")
)

Pi.binder.update("text", "Hello World!")
```