# UpsertPayloadRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 
**tags** | **List[str]** | A list of default tags for each flag | 
**temporary** | **bool** | Whether the flag should be temporary by default | 
**boolean_defaults** | [**BooleanFlagDefaults**](BooleanFlagDefaults.md) |  | 
**default_client_side_availability** | [**DefaultClientSideAvailability**](DefaultClientSideAvailability.md) |  | 

## Example

```python
from launchdarkly_api.models.upsert_payload_rep import UpsertPayloadRep

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertPayloadRep from a JSON string
upsert_payload_rep_instance = UpsertPayloadRep.from_json(json)
# print the JSON string representation of the object
print(UpsertPayloadRep.to_json())

# convert the object into a dict
upsert_payload_rep_dict = upsert_payload_rep_instance.to_dict()
# create an instance of UpsertPayloadRep from a dict
upsert_payload_rep_from_dict = UpsertPayloadRep.from_dict(upsert_payload_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


