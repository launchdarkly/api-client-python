# PatchIpAllowlistConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_allowlist_enabled** | **bool** | Enable or disable session allowlist | [optional] 
**api_token_allowlist_enabled** | **bool** | Enable or disable API token allowlist | [optional] 

## Example

```python
from launchdarkly_api.models.patch_ip_allowlist_config_request import PatchIpAllowlistConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchIpAllowlistConfigRequest from a JSON string
patch_ip_allowlist_config_request_instance = PatchIpAllowlistConfigRequest.from_json(json)
# print the JSON string representation of the object
print(PatchIpAllowlistConfigRequest.to_json())

# convert the object into a dict
patch_ip_allowlist_config_request_dict = patch_ip_allowlist_config_request_instance.to_dict()
# create an instance of PatchIpAllowlistConfigRequest from a dict
patch_ip_allowlist_config_request_from_dict = PatchIpAllowlistConfigRequest.from_dict(patch_ip_allowlist_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


