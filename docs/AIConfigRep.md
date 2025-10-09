# AIConfigRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the AI Config | 
**name** | **str** | The name of the AI Config | 

## Example

```python
from launchdarkly_api.models.ai_config_rep import AIConfigRep

# TODO update the JSON string below
json = "{}"
# create an instance of AIConfigRep from a JSON string
ai_config_rep_instance = AIConfigRep.from_json(json)
# print the JSON string representation of the object
print(AIConfigRep.to_json())

# convert the object into a dict
ai_config_rep_dict = ai_config_rep_instance.to_dict()
# create an instance of AIConfigRep from a dict
ai_config_rep_from_dict = AIConfigRep.from_dict(ai_config_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


