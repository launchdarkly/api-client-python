# RestrictedModelsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | **List[str]** |  | 

## Example

```python
from launchdarkly_api.models.restricted_models_request import RestrictedModelsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestrictedModelsRequest from a JSON string
restricted_models_request_instance = RestrictedModelsRequest.from_json(json)
# print the JSON string representation of the object
print(RestrictedModelsRequest.to_json())

# convert the object into a dict
restricted_models_request_dict = restricted_models_request_instance.to_dict()
# create an instance of RestrictedModelsRequest from a dict
restricted_models_request_from_dict = RestrictedModelsRequest.from_dict(restricted_models_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


