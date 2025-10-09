# StatusConflictErrorRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specific error code encountered | 
**message** | **str** | Description of the error | 

## Example

```python
from launchdarkly_api.models.status_conflict_error_rep import StatusConflictErrorRep

# TODO update the JSON string below
json = "{}"
# create an instance of StatusConflictErrorRep from a JSON string
status_conflict_error_rep_instance = StatusConflictErrorRep.from_json(json)
# print the JSON string representation of the object
print(StatusConflictErrorRep.to_json())

# convert the object into a dict
status_conflict_error_rep_dict = status_conflict_error_rep_instance.to_dict()
# create an instance of StatusConflictErrorRep from a dict
status_conflict_error_rep_from_dict = StatusConflictErrorRep.from_dict(status_conflict_error_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


