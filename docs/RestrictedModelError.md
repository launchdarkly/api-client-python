# RestrictedModelError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The model config key that was not added | 
**message** | **str** | Why the key was not added. A key that a config variation uses cannot be restricted. Move those variations to a different model first. | 
**code** | **int** | HTTP status code for this key. &#x60;400&#x60; means a config variation uses the key. &#x60;404&#x60; means the key does not exist in the project. | 

## Example

```python
from launchdarkly_api.models.restricted_model_error import RestrictedModelError

# TODO update the JSON string below
json = "{}"
# create an instance of RestrictedModelError from a JSON string
restricted_model_error_instance = RestrictedModelError.from_json(json)
# print the JSON string representation of the object
print(RestrictedModelError.to_json())

# convert the object into a dict
restricted_model_error_dict = restricted_model_error_instance.to_dict()
# create an instance of RestrictedModelError from a dict
restricted_model_error_from_dict = RestrictedModelError.from_dict(restricted_model_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


