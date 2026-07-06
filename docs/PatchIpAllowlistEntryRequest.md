# PatchIpAllowlistEntryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 

## Example

```python
from launchdarkly_api.models.patch_ip_allowlist_entry_request import PatchIpAllowlistEntryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchIpAllowlistEntryRequest from a JSON string
patch_ip_allowlist_entry_request_instance = PatchIpAllowlistEntryRequest.from_json(json)
# print the JSON string representation of the object
print(PatchIpAllowlistEntryRequest.to_json())

# convert the object into a dict
patch_ip_allowlist_entry_request_dict = patch_ip_allowlist_entry_request_instance.to_dict()
# create an instance of PatchIpAllowlistEntryRequest from a dict
patch_ip_allowlist_entry_request_from_dict = PatchIpAllowlistEntryRequest.from_dict(patch_ip_allowlist_entry_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


