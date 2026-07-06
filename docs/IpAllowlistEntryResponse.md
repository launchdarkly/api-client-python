# IpAllowlistEntryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier for the allowlist entry | 
**ip_address** | **str** | IP address or CIDR block | 
**description** | **str** |  | [optional] 
**created_by_member_id** | **str** |  | [optional] 
**created_at** | **int** |  | 
**updated_at** | **int** |  | 

## Example

```python
from launchdarkly_api.models.ip_allowlist_entry_response import IpAllowlistEntryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IpAllowlistEntryResponse from a JSON string
ip_allowlist_entry_response_instance = IpAllowlistEntryResponse.from_json(json)
# print the JSON string representation of the object
print(IpAllowlistEntryResponse.to_json())

# convert the object into a dict
ip_allowlist_entry_response_dict = ip_allowlist_entry_response_instance.to_dict()
# create an instance of IpAllowlistEntryResponse from a dict
ip_allowlist_entry_response_from_dict = IpAllowlistEntryResponse.from_dict(ip_allowlist_entry_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


