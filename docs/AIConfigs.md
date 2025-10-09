# AIConfigs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedLinks**](PaginatedLinks.md) |  | [optional] 
**items** | [**List[AIConfig]**](AIConfig.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from launchdarkly_api.models.ai_configs import AIConfigs

# TODO update the JSON string below
json = "{}"
# create an instance of AIConfigs from a JSON string
ai_configs_instance = AIConfigs.from_json(json)
# print the JSON string representation of the object
print(AIConfigs.to_json())

# convert the object into a dict
ai_configs_dict = ai_configs_instance.to_dict()
# create an instance of AIConfigs from a dict
ai_configs_from_dict = AIConfigs.from_dict(ai_configs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


