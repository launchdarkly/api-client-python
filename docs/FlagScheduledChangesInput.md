# FlagScheduledChangesInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional comment describing the update to the scheduled changes | [optional] 
**instructions** | **List[Dict[str, object]]** |  | 

## Example

```python
from launchdarkly_api.models.flag_scheduled_changes_input import FlagScheduledChangesInput

# TODO update the JSON string below
json = "{}"
# create an instance of FlagScheduledChangesInput from a JSON string
flag_scheduled_changes_input_instance = FlagScheduledChangesInput.from_json(json)
# print the JSON string representation of the object
print(FlagScheduledChangesInput.to_json())

# convert the object into a dict
flag_scheduled_changes_input_dict = flag_scheduled_changes_input_instance.to_dict()
# create an instance of FlagScheduledChangesInput from a dict
flag_scheduled_changes_input_from_dict = FlagScheduledChangesInput.from_dict(flag_scheduled_changes_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


