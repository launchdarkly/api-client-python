# ModelConfigs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedLinks**](PaginatedLinks.md) |  | [optional] 
**items** | [**List[ModelConfig]**](ModelConfig.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from launchdarkly_api.models.model_configs import ModelConfigs

# TODO update the JSON string below
json = "{}"
# create an instance of ModelConfigs from a JSON string
model_configs_instance = ModelConfigs.from_json(json)
# print the JSON string representation of the object
print(ModelConfigs.to_json())

# convert the object into a dict
model_configs_dict = model_configs_instance.to_dict()
# create an instance of ModelConfigs from a dict
model_configs_from_dict = ModelConfigs.from_dict(model_configs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


