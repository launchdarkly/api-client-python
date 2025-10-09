# ExpandedAIConfig

AI Config representation for Views API - contains only fields actually used by the Views service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A unique key used to reference the AI config | [optional] 
**name** | **str** | A human-friendly name for the AI config | [optional] 
**tags** | **List[str]** | Tags for the AI config | [optional] 
**description** | **str** | Description of the AI config | [optional] 
**version** | **int** | Version of the AI config | [optional] 
**created_at** | **int** | Creation date in milliseconds | [optional] 
**updated_at** | **int** | Last modification date in milliseconds | [optional] 
**flag_key** | **str** | Key of the flag that this AI config is attached to | [optional] 
**links** | [**ParentAndSelfLinks**](ParentAndSelfLinks.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.expanded_ai_config import ExpandedAIConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ExpandedAIConfig from a JSON string
expanded_ai_config_instance = ExpandedAIConfig.from_json(json)
# print the JSON string representation of the object
print(ExpandedAIConfig.to_json())

# convert the object into a dict
expanded_ai_config_dict = expanded_ai_config_instance.to_dict()
# create an instance of ExpandedAIConfig from a dict
expanded_ai_config_from_dict = ExpandedAIConfig.from_dict(expanded_ai_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


