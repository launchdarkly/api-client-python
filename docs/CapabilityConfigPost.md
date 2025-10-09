# CapabilityConfigPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approvals** | [**ApprovalsCapabilityConfig**](ApprovalsCapabilityConfig.md) |  | [optional] 
**audit_log_events_hook** | [**AuditLogEventsHookCapabilityConfigPost**](AuditLogEventsHookCapabilityConfigPost.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.capability_config_post import CapabilityConfigPost

# TODO update the JSON string below
json = "{}"
# create an instance of CapabilityConfigPost from a JSON string
capability_config_post_instance = CapabilityConfigPost.from_json(json)
# print the JSON string representation of the object
print(CapabilityConfigPost.to_json())

# convert the object into a dict
capability_config_post_dict = capability_config_post_instance.to_dict()
# create an instance of CapabilityConfigPost from a dict
capability_config_post_from_dict = CapabilityConfigPost.from_dict(capability_config_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


