# RelayAutoConfigPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name for the Relay Proxy configuration | 
**policy** | [**List[Statement]**](Statement.md) | A description of what environments and projects the Relay Proxy should include or exclude. To learn more, read [Write an inline policy](https://launchdarkly.com/docs/sdk/relay-proxy/automatic-configuration#write-an-inline-policy). | 

## Example

```python
from launchdarkly_api.models.relay_auto_config_post import RelayAutoConfigPost

# TODO update the JSON string below
json = "{}"
# create an instance of RelayAutoConfigPost from a JSON string
relay_auto_config_post_instance = RelayAutoConfigPost.from_json(json)
# print the JSON string representation of the object
print(RelayAutoConfigPost.to_json())

# convert the object into a dict
relay_auto_config_post_dict = relay_auto_config_post_instance.to_dict()
# create an instance of RelayAutoConfigPost from a dict
relay_auto_config_post_from_dict = RelayAutoConfigPost.from_dict(relay_auto_config_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


