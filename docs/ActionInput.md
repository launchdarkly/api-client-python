# ActionInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instructions** | **object** | An array of instructions for the stage. Each object in the array uses the semantic patch format for updating a feature flag. | [optional] 

## Example

```python
from launchdarkly_api.models.action_input import ActionInput

# TODO update the JSON string below
json = "{}"
# create an instance of ActionInput from a JSON string
action_input_instance = ActionInput.from_json(json)
# print the JSON string representation of the object
print(ActionInput.to_json())

# convert the object into a dict
action_input_dict = action_input_instance.to_dict()
# create an instance of ActionInput from a dict
action_input_from_dict = ActionInput.from_dict(action_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


