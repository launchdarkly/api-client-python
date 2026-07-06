# CreateIpAllowlistEntryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.create_ip_allowlist_entry_request import CreateIpAllowlistEntryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIpAllowlistEntryRequest from a JSON string
create_ip_allowlist_entry_request_instance = CreateIpAllowlistEntryRequest.from_json(json)
# print the JSON string representation of the object
print(CreateIpAllowlistEntryRequest.to_json())

# convert the object into a dict
create_ip_allowlist_entry_request_dict = create_ip_allowlist_entry_request_instance.to_dict()
# create an instance of CreateIpAllowlistEntryRequest from a dict
create_ip_allowlist_entry_request_from_dict = CreateIpAllowlistEntryRequest.from_dict(create_ip_allowlist_entry_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


