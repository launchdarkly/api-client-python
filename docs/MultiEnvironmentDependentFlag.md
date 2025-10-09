# MultiEnvironmentDependentFlag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The flag name | [optional] 
**key** | **str** | The flag key | 
**environments** | [**List[DependentFlagEnvironment]**](DependentFlagEnvironment.md) | A list of environments in which the dependent flag appears | 

## Example

```python
from launchdarkly_api.models.multi_environment_dependent_flag import MultiEnvironmentDependentFlag

# TODO update the JSON string below
json = "{}"
# create an instance of MultiEnvironmentDependentFlag from a JSON string
multi_environment_dependent_flag_instance = MultiEnvironmentDependentFlag.from_json(json)
# print the JSON string representation of the object
print(MultiEnvironmentDependentFlag.to_json())

# convert the object into a dict
multi_environment_dependent_flag_dict = multi_environment_dependent_flag_instance.to_dict()
# create an instance of MultiEnvironmentDependentFlag from a dict
multi_environment_dependent_flag_from_dict = MultiEnvironmentDependentFlag.from_dict(multi_environment_dependent_flag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


