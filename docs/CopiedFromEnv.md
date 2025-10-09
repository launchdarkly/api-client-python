# CopiedFromEnv


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key of feature flag copied | 
**version** | **int** | Version of feature flag copied | [optional] 

## Example

```python
from launchdarkly_api.models.copied_from_env import CopiedFromEnv

# TODO update the JSON string below
json = "{}"
# create an instance of CopiedFromEnv from a JSON string
copied_from_env_instance = CopiedFromEnv.from_json(json)
# print the JSON string representation of the object
print(CopiedFromEnv.to_json())

# convert the object into a dict
copied_from_env_dict = copied_from_env_instance.to_dict()
# create an instance of CopiedFromEnv from a dict
copied_from_env_from_dict = CopiedFromEnv.from_dict(copied_from_env_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


