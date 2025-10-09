# RelayAutoConfigRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**creator** | [**MemberSummary**](MemberSummary.md) |  | [optional] 
**access** | [**Access**](Access.md) |  | [optional] 
**name** | **str** | A human-friendly name for the Relay Proxy configuration | 
**policy** | [**List[Statement]**](Statement.md) | A description of what environments and projects the Relay Proxy should include or exclude | 
**full_key** | **str** | The Relay Proxy configuration key | 
**display_key** | **str** | The last few characters of the Relay Proxy configuration key, displayed in the LaunchDarkly UI | 
**creation_date** | **int** |  | 
**last_modified** | **int** |  | 

## Example

```python
from launchdarkly_api.models.relay_auto_config_rep import RelayAutoConfigRep

# TODO update the JSON string below
json = "{}"
# create an instance of RelayAutoConfigRep from a JSON string
relay_auto_config_rep_instance = RelayAutoConfigRep.from_json(json)
# print the JSON string representation of the object
print(RelayAutoConfigRep.to_json())

# convert the object into a dict
relay_auto_config_rep_dict = relay_auto_config_rep_instance.to_dict()
# create an instance of RelayAutoConfigRep from a dict
relay_auto_config_rep_from_dict = RelayAutoConfigRep.from_dict(relay_auto_config_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


