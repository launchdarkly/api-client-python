# FailureReasonRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** | The attribute that failed validation | 
**reason** | **str** | The reason the attribute failed validation | 

## Example

```python
from launchdarkly_api.models.failure_reason_rep import FailureReasonRep

# TODO update the JSON string below
json = "{}"
# create an instance of FailureReasonRep from a JSON string
failure_reason_rep_instance = FailureReasonRep.from_json(json)
# print the JSON string representation of the object
print(FailureReasonRep.to_json())

# convert the object into a dict
failure_reason_rep_dict = failure_reason_rep_instance.to_dict()
# create an instance of FailureReasonRep from a dict
failure_reason_rep_from_dict = FailureReasonRep.from_dict(failure_reason_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


