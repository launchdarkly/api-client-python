# AIConfigDependency

A resource that depends on this AI Config

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the dependent resource | 
**key** | **str** | The key of the dependent resource | 

## Example

```python
from launchdarkly_api.models.ai_config_dependency import AIConfigDependency

# TODO update the JSON string below
json = "{}"
# create an instance of AIConfigDependency from a JSON string
ai_config_dependency_instance = AIConfigDependency.from_json(json)
# print the JSON string representation of the object
print(AIConfigDependency.to_json())

# convert the object into a dict
ai_config_dependency_dict = ai_config_dependency_instance.to_dict()
# create an instance of AIConfigDependency from a dict
ai_config_dependency_from_dict = AIConfigDependency.from_dict(ai_config_dependency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


