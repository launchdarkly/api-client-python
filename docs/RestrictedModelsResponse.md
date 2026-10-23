# RestrictedModelsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successes** | **List[str]** | Model config keys that were added to the restricted list | 
**errors** | [**List[RestrictedModelError]**](RestrictedModelError.md) | Model config keys that were not added, with the reason for each key | 

## Example

```python
from launchdarkly_api.models.restricted_models_response import RestrictedModelsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RestrictedModelsResponse from a JSON string
restricted_models_response_instance = RestrictedModelsResponse.from_json(json)
# print the JSON string representation of the object
print(RestrictedModelsResponse.to_json())

# convert the object into a dict
restricted_models_response_dict = restricted_models_response_instance.to_dict()
# create an instance of RestrictedModelsResponse from a dict
restricted_models_response_from_dict = RestrictedModelsResponse.from_dict(restricted_models_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


