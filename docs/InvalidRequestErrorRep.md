# InvalidRequestErrorRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specific error code encountered | 
**message** | **str** | Description of the error | 

## Example

```python
from launchdarkly_api.models.invalid_request_error_rep import InvalidRequestErrorRep

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidRequestErrorRep from a JSON string
invalid_request_error_rep_instance = InvalidRequestErrorRep.from_json(json)
# print the JSON string representation of the object
print(InvalidRequestErrorRep.to_json())

# convert the object into a dict
invalid_request_error_rep_dict = invalid_request_error_rep_instance.to_dict()
# create an instance of InvalidRequestErrorRep from a dict
invalid_request_error_rep_from_dict = InvalidRequestErrorRep.from_dict(invalid_request_error_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


