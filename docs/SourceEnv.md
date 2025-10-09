# SourceEnv


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the source environment to clone from | [optional] 
**version** | **int** | (Optional) The version number of the source environment to clone from. Used for optimistic locking | [optional] 

## Example

```python
from launchdarkly_api.models.source_env import SourceEnv

# TODO update the JSON string below
json = "{}"
# create an instance of SourceEnv from a JSON string
source_env_instance = SourceEnv.from_json(json)
# print the JSON string representation of the object
print(SourceEnv.to_json())

# convert the object into a dict
source_env_dict = source_env_instance.to_dict()
# create an instance of SourceEnv from a dict
source_env_from_dict = SourceEnv.from_dict(source_env_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


