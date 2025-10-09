# ForbiddenErrorRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specific error code encountered | 
**message** | **str** | Description of the error | 

## Example

```python
from launchdarkly_api.models.forbidden_error_rep import ForbiddenErrorRep

# TODO update the JSON string below
json = "{}"
# create an instance of ForbiddenErrorRep from a JSON string
forbidden_error_rep_instance = ForbiddenErrorRep.from_json(json)
# print the JSON string representation of the object
print(ForbiddenErrorRep.to_json())

# convert the object into a dict
forbidden_error_rep_dict = forbidden_error_rep_instance.to_dict()
# create an instance of ForbiddenErrorRep from a dict
forbidden_error_rep_from_dict = ForbiddenErrorRep.from_dict(forbidden_error_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


