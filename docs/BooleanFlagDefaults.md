# BooleanFlagDefaults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**true_display_name** | **str** | The display name for the true variation, displayed in the LaunchDarkly user interface | 
**false_display_name** | **str** | The display name for the false variation, displayed in the LaunchDarkly user interface | 
**true_description** | **str** | The description for the true variation | 
**false_description** | **str** | The description for the false variation | 
**on_variation** | **int** | The variation index of the flag variation to use for the default targeting behavior when a flag&#39;s targeting is on and the target did not match any rules | 
**off_variation** | **int** | The variation index of the flag variation to use for the default targeting behavior when a flag&#39;s targeting is off | 

## Example

```python
from launchdarkly_api.models.boolean_flag_defaults import BooleanFlagDefaults

# TODO update the JSON string below
json = "{}"
# create an instance of BooleanFlagDefaults from a JSON string
boolean_flag_defaults_instance = BooleanFlagDefaults.from_json(json)
# print the JSON string representation of the object
print(BooleanFlagDefaults.to_json())

# convert the object into a dict
boolean_flag_defaults_dict = boolean_flag_defaults_instance.to_dict()
# create an instance of BooleanFlagDefaults from a dict
boolean_flag_defaults_from_dict = BooleanFlagDefaults.from_dict(boolean_flag_defaults_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


