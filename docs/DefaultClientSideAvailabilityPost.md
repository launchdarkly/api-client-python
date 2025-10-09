# DefaultClientSideAvailabilityPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**using_environment_id** | **bool** | Whether to enable availability for client-side SDKs. | 
**using_mobile_key** | **bool** | Whether to enable availability for mobile SDKs. | 

## Example

```python
from launchdarkly_api.models.default_client_side_availability_post import DefaultClientSideAvailabilityPost

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultClientSideAvailabilityPost from a JSON string
default_client_side_availability_post_instance = DefaultClientSideAvailabilityPost.from_json(json)
# print the JSON string representation of the object
print(DefaultClientSideAvailabilityPost.to_json())

# convert the object into a dict
default_client_side_availability_post_dict = default_client_side_availability_post_instance.to_dict()
# create an instance of DefaultClientSideAvailabilityPost from a dict
default_client_side_availability_post_from_dict = DefaultClientSideAvailabilityPost.from_dict(default_client_side_availability_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


