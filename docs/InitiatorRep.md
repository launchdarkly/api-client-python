# InitiatorRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the member who initiated the export | [optional] 
**email** | **str** | The email address of the member who initiated the export | [optional] 

## Example

```python
from launchdarkly_api.models.initiator_rep import InitiatorRep

# TODO update the JSON string below
json = "{}"
# create an instance of InitiatorRep from a JSON string
initiator_rep_instance = InitiatorRep.from_json(json)
# print the JSON string representation of the object
print(InitiatorRep.to_json())

# convert the object into a dict
initiator_rep_dict = initiator_rep_instance.to_dict()
# create an instance of InitiatorRep from a dict
initiator_rep_from_dict = InitiatorRep.from_dict(initiator_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


