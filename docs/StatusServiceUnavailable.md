# StatusServiceUnavailable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specific error code encountered | 
**message** | **str** | Description of the error | 

## Example

```python
from launchdarkly_api.models.status_service_unavailable import StatusServiceUnavailable

# TODO update the JSON string below
json = "{}"
# create an instance of StatusServiceUnavailable from a JSON string
status_service_unavailable_instance = StatusServiceUnavailable.from_json(json)
# print the JSON string representation of the object
print(StatusServiceUnavailable.to_json())

# convert the object into a dict
status_service_unavailable_dict = status_service_unavailable_instance.to_dict()
# create an instance of StatusServiceUnavailable from a dict
status_service_unavailable_from_dict = StatusServiceUnavailable.from_dict(status_service_unavailable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


