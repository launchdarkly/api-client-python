# CompletedBy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | [**MemberSummary**](MemberSummary.md) |  | [optional] 
**token** | [**TokenSummary**](TokenSummary.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.completed_by import CompletedBy

# TODO update the JSON string below
json = "{}"
# create an instance of CompletedBy from a JSON string
completed_by_instance = CompletedBy.from_json(json)
# print the JSON string representation of the object
print(CompletedBy.to_json())

# convert the object into a dict
completed_by_dict = completed_by_instance.to_dict()
# create an instance of CompletedBy from a dict
completed_by_from_dict = CompletedBy.from_dict(completed_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


