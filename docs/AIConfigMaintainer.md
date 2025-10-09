# AIConfigMaintainer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**id** | **str** |  | 
**email** | **str** |  | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**role** | **str** |  | 
**key** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from launchdarkly_api.models.ai_config_maintainer import AIConfigMaintainer

# TODO update the JSON string below
json = "{}"
# create an instance of AIConfigMaintainer from a JSON string
ai_config_maintainer_instance = AIConfigMaintainer.from_json(json)
# print the JSON string representation of the object
print(AIConfigMaintainer.to_json())

# convert the object into a dict
ai_config_maintainer_dict = ai_config_maintainer_instance.to_dict()
# create an instance of AIConfigMaintainer from a dict
ai_config_maintainer_from_dict = AIConfigMaintainer.from_dict(ai_config_maintainer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


