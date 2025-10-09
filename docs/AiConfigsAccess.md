# AiConfigsAccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**denied** | [**List[AiConfigsAccessDenied]**](AiConfigsAccessDenied.md) |  | 
**allowed** | [**List[AiConfigsAccessAllowedRep]**](AiConfigsAccessAllowedRep.md) |  | 

## Example

```python
from launchdarkly_api.models.ai_configs_access import AiConfigsAccess

# TODO update the JSON string below
json = "{}"
# create an instance of AiConfigsAccess from a JSON string
ai_configs_access_instance = AiConfigsAccess.from_json(json)
# print the JSON string representation of the object
print(AiConfigsAccess.to_json())

# convert the object into a dict
ai_configs_access_dict = ai_configs_access_instance.to_dict()
# create an instance of AiConfigsAccess from a dict
ai_configs_access_from_dict = AiConfigsAccess.from_dict(ai_configs_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


