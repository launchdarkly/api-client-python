# DependentFlagEnvironment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The environment name | [optional] 
**key** | **str** | The environment key | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**site** | [**Link**](Link.md) |  | 

## Example

```python
from launchdarkly_api.models.dependent_flag_environment import DependentFlagEnvironment

# TODO update the JSON string below
json = "{}"
# create an instance of DependentFlagEnvironment from a JSON string
dependent_flag_environment_instance = DependentFlagEnvironment.from_json(json)
# print the JSON string representation of the object
print(DependentFlagEnvironment.to_json())

# convert the object into a dict
dependent_flag_environment_dict = dependent_flag_environment_instance.to_dict()
# create an instance of DependentFlagEnvironment from a dict
dependent_flag_environment_from_dict = DependentFlagEnvironment.from_dict(dependent_flag_environment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


