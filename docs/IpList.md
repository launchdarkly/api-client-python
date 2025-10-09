# IpList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** | A list of the IP addresses LaunchDarkly&#39;s service uses | 
**outbound_addresses** | **List[str]** | A list of the IP addresses outgoing webhook notifications use | 

## Example

```python
from launchdarkly_api.models.ip_list import IpList

# TODO update the JSON string below
json = "{}"
# create an instance of IpList from a JSON string
ip_list_instance = IpList.from_json(json)
# print the JSON string representation of the object
print(IpList.to_json())

# convert the object into a dict
ip_list_dict = ip_list_instance.to_dict()
# create an instance of IpList from a dict
ip_list_from_dict = IpList.from_dict(ip_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


