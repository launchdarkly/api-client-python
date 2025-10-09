# AIConfigVariationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AIConfigVariation]**](AIConfigVariation.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from launchdarkly_api.models.ai_config_variations_response import AIConfigVariationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AIConfigVariationsResponse from a JSON string
ai_config_variations_response_instance = AIConfigVariationsResponse.from_json(json)
# print the JSON string representation of the object
print(AIConfigVariationsResponse.to_json())

# convert the object into a dict
ai_config_variations_response_dict = ai_config_variations_response_instance.to_dict()
# create an instance of AIConfigVariationsResponse from a dict
ai_config_variations_response_from_dict = AIConfigVariationsResponse.from_dict(ai_config_variations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


