# AiConfigsAccessDenied


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**reason** | [**AiConfigsAccessDeniedReason**](AiConfigsAccessDeniedReason.md) |  | 

## Example

```python
from launchdarkly_api.models.ai_configs_access_denied import AiConfigsAccessDenied

# TODO update the JSON string below
json = "{}"
# create an instance of AiConfigsAccessDenied from a JSON string
ai_configs_access_denied_instance = AiConfigsAccessDenied.from_json(json)
# print the JSON string representation of the object
print(AiConfigsAccessDenied.to_json())

# convert the object into a dict
ai_configs_access_denied_dict = ai_configs_access_denied_instance.to_dict()
# create an instance of AiConfigsAccessDenied from a dict
ai_configs_access_denied_from_dict = AiConfigsAccessDenied.from_dict(ai_configs_access_denied_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


