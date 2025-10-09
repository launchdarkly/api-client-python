# ClientSideAvailabilityPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**using_environment_id** | **bool** | Whether to enable availability for client-side SDKs. Defaults to &lt;code&gt;false&lt;/code&gt;. | 
**using_mobile_key** | **bool** | Whether to enable availability for mobile SDKs. Defaults to &lt;code&gt;true&lt;/code&gt;. | 

## Example

```python
from launchdarkly_api.models.client_side_availability_post import ClientSideAvailabilityPost

# TODO update the JSON string below
json = "{}"
# create an instance of ClientSideAvailabilityPost from a JSON string
client_side_availability_post_instance = ClientSideAvailabilityPost.from_json(json)
# print the JSON string representation of the object
print(ClientSideAvailabilityPost.to_json())

# convert the object into a dict
client_side_availability_post_dict = client_side_availability_post_instance.to_dict()
# create an instance of ClientSideAvailabilityPost from a dict
client_side_availability_post_from_dict = ClientSideAvailabilityPost.from_dict(client_side_availability_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


