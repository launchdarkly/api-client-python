# StoreIntegrationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**timestamp** | **int** |  | [optional] 

## Example

```python
from launchdarkly_api.models.store_integration_error import StoreIntegrationError

# TODO update the JSON string below
json = "{}"
# create an instance of StoreIntegrationError from a JSON string
store_integration_error_instance = StoreIntegrationError.from_json(json)
# print the JSON string representation of the object
print(StoreIntegrationError.to_json())

# convert the object into a dict
store_integration_error_dict = store_integration_error_instance.to_dict()
# create an instance of StoreIntegrationError from a dict
store_integration_error_from_dict = StoreIntegrationError.from_dict(store_integration_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


