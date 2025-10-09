# DependentFlagsByEnvironment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DependentFlag]**](DependentFlag.md) | A list of dependent flags, which are flags that use the requested flag as a prerequisite | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**site** | [**Link**](Link.md) |  | 

## Example

```python
from launchdarkly_api.models.dependent_flags_by_environment import DependentFlagsByEnvironment

# TODO update the JSON string below
json = "{}"
# create an instance of DependentFlagsByEnvironment from a JSON string
dependent_flags_by_environment_instance = DependentFlagsByEnvironment.from_json(json)
# print the JSON string representation of the object
print(DependentFlagsByEnvironment.to_json())

# convert the object into a dict
dependent_flags_by_environment_dict = dependent_flags_by_environment_instance.to_dict()
# create an instance of DependentFlagsByEnvironment from a dict
dependent_flags_by_environment_from_dict = DependentFlagsByEnvironment.from_dict(dependent_flags_by_environment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


