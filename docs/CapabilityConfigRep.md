# CapabilityConfigRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approvals** | [**ApprovalsCapabilityConfig**](ApprovalsCapabilityConfig.md) |  | [optional] 
**audit_log_events_hook** | [**AuditLogEventsHookCapabilityConfigRep**](AuditLogEventsHookCapabilityConfigRep.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.capability_config_rep import CapabilityConfigRep

# TODO update the JSON string below
json = "{}"
# create an instance of CapabilityConfigRep from a JSON string
capability_config_rep_instance = CapabilityConfigRep.from_json(json)
# print the JSON string representation of the object
print(CapabilityConfigRep.to_json())

# convert the object into a dict
capability_config_rep_dict = capability_config_rep_instance.to_dict()
# create an instance of CapabilityConfigRep from a dict
capability_config_rep_from_dict = CapabilityConfigRep.from_dict(capability_config_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


