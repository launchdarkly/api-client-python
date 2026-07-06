# IpAllowlistResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_allowlist_enabled** | **bool** |  | 
**api_token_allowlist_enabled** | **bool** |  | 
**entries** | [**List[IpAllowlistEntryResponse]**](IpAllowlistEntryResponse.md) |  | 

## Example

```python
from launchdarkly_api.models.ip_allowlist_response import IpAllowlistResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IpAllowlistResponse from a JSON string
ip_allowlist_response_instance = IpAllowlistResponse.from_json(json)
# print the JSON string representation of the object
print(IpAllowlistResponse.to_json())

# convert the object into a dict
ip_allowlist_response_dict = ip_allowlist_response_instance.to_dict()
# create an instance of IpAllowlistResponse from a dict
ip_allowlist_response_from_dict = IpAllowlistResponse.from_dict(ip_allowlist_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


