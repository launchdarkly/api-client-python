# AIConfigMaintainer

The member or team that maintains this resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**id** | **str** | The member ID | 
**email** | **str** | The member email address | 
**first_name** | **str** | The member first name | [optional] 
**last_name** | **str** | The member last name | [optional] 
**role** | **str** | The member role | 
**key** | **str** | The team key | 
**name** | **str** | The team name | 

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


