# AiConfigsAccessAllowedRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**reason** | [**AiConfigsAccessAllowedReason**](AiConfigsAccessAllowedReason.md) |  | 

## Example

```python
from launchdarkly_api.models.ai_configs_access_allowed_rep import AiConfigsAccessAllowedRep

# TODO update the JSON string below
json = "{}"
# create an instance of AiConfigsAccessAllowedRep from a JSON string
ai_configs_access_allowed_rep_instance = AiConfigsAccessAllowedRep.from_json(json)
# print the JSON string representation of the object
print(AiConfigsAccessAllowedRep.to_json())

# convert the object into a dict
ai_configs_access_allowed_rep_dict = ai_configs_access_allowed_rep_instance.to_dict()
# create an instance of AiConfigsAccessAllowedRep from a dict
ai_configs_access_allowed_rep_from_dict = AiConfigsAccessAllowedRep.from_dict(ai_configs_access_allowed_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


