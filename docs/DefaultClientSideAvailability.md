# DefaultClientSideAvailability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**using_mobile_key** | **bool** | Whether to enable availability for mobile SDKs | 
**using_environment_id** | **bool** | Whether to enable availability for client-side SDKs | 

## Example

```python
from launchdarkly_api.models.default_client_side_availability import DefaultClientSideAvailability

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultClientSideAvailability from a JSON string
default_client_side_availability_instance = DefaultClientSideAvailability.from_json(json)
# print the JSON string representation of the object
print(DefaultClientSideAvailability.to_json())

# convert the object into a dict
default_client_side_availability_dict = default_client_side_availability_instance.to_dict()
# create an instance of DefaultClientSideAvailability from a dict
default_client_side_availability_from_dict = DefaultClientSideAvailability.from_dict(default_client_side_availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


