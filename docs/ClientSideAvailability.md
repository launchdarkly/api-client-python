# ClientSideAvailability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**using_mobile_key** | **bool** |  | [optional] 
**using_environment_id** | **bool** |  | [optional] 

## Example

```python
from launchdarkly_api.models.client_side_availability import ClientSideAvailability

# TODO update the JSON string below
json = "{}"
# create an instance of ClientSideAvailability from a JSON string
client_side_availability_instance = ClientSideAvailability.from_json(json)
# print the JSON string representation of the object
print(ClientSideAvailability.to_json())

# convert the object into a dict
client_side_availability_dict = client_side_availability_instance.to_dict()
# create an instance of ClientSideAvailability from a dict
client_side_availability_from_dict = ClientSideAvailability.from_dict(client_side_availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


