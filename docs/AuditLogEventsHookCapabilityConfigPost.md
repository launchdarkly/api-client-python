# AuditLogEventsHookCapabilityConfigPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statements** | [**List[StatementPost]**](StatementPost.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.audit_log_events_hook_capability_config_post import AuditLogEventsHookCapabilityConfigPost

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogEventsHookCapabilityConfigPost from a JSON string
audit_log_events_hook_capability_config_post_instance = AuditLogEventsHookCapabilityConfigPost.from_json(json)
# print the JSON string representation of the object
print(AuditLogEventsHookCapabilityConfigPost.to_json())

# convert the object into a dict
audit_log_events_hook_capability_config_post_dict = audit_log_events_hook_capability_config_post_instance.to_dict()
# create an instance of AuditLogEventsHookCapabilityConfigPost from a dict
audit_log_events_hook_capability_config_post_from_dict = AuditLogEventsHookCapabilityConfigPost.from_dict(audit_log_events_hook_capability_config_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


