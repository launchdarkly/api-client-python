# FlagCopyConfigEnvironment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The environment key | 
**current_version** | **int** | Optional flag version. If you include this, the operation only succeeds if the current flag version in the environment matches this version. | [optional] 

## Example

```python
from launchdarkly_api.models.flag_copy_config_environment import FlagCopyConfigEnvironment

# TODO update the JSON string below
json = "{}"
# create an instance of FlagCopyConfigEnvironment from a JSON string
flag_copy_config_environment_instance = FlagCopyConfigEnvironment.from_json(json)
# print the JSON string representation of the object
print(FlagCopyConfigEnvironment.to_json())

# convert the object into a dict
flag_copy_config_environment_dict = flag_copy_config_environment_instance.to_dict()
# create an instance of FlagCopyConfigEnvironment from a dict
flag_copy_config_environment_from_dict = FlagCopyConfigEnvironment.from_dict(flag_copy_config_environment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


