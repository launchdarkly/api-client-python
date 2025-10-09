# AuditLogEventsHookCapabilityConfigRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statements** | [**List[Statement]**](Statement.md) | The set of resources you wish to subscribe to audit log notifications for. | [optional] 

## Example

```python
from launchdarkly_api.models.audit_log_events_hook_capability_config_rep import AuditLogEventsHookCapabilityConfigRep

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogEventsHookCapabilityConfigRep from a JSON string
audit_log_events_hook_capability_config_rep_instance = AuditLogEventsHookCapabilityConfigRep.from_json(json)
# print the JSON string representation of the object
print(AuditLogEventsHookCapabilityConfigRep.to_json())

# convert the object into a dict
audit_log_events_hook_capability_config_rep_dict = audit_log_events_hook_capability_config_rep_instance.to_dict()
# create an instance of AuditLogEventsHookCapabilityConfigRep from a dict
audit_log_events_hook_capability_config_rep_from_dict = AuditLogEventsHookCapabilityConfigRep.from_dict(audit_log_events_hook_capability_config_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


