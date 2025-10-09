# MultiEnvironmentDependentFlags


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[MultiEnvironmentDependentFlag]**](MultiEnvironmentDependentFlag.md) | An array of dependent flags with their environment information | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**site** | [**Link**](Link.md) |  | 

## Example

```python
from launchdarkly_api.models.multi_environment_dependent_flags import MultiEnvironmentDependentFlags

# TODO update the JSON string below
json = "{}"
# create an instance of MultiEnvironmentDependentFlags from a JSON string
multi_environment_dependent_flags_instance = MultiEnvironmentDependentFlags.from_json(json)
# print the JSON string representation of the object
print(MultiEnvironmentDependentFlags.to_json())

# convert the object into a dict
multi_environment_dependent_flags_dict = multi_environment_dependent_flags_instance.to_dict()
# create an instance of MultiEnvironmentDependentFlags from a dict
multi_environment_dependent_flags_from_dict = MultiEnvironmentDependentFlags.from_dict(multi_environment_dependent_flags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


