# MethodNotAllowedErrorRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specific error code encountered | 
**message** | **str** | Description of the error | 

## Example

```python
from launchdarkly_api.models.method_not_allowed_error_rep import MethodNotAllowedErrorRep

# TODO update the JSON string below
json = "{}"
# create an instance of MethodNotAllowedErrorRep from a JSON string
method_not_allowed_error_rep_instance = MethodNotAllowedErrorRep.from_json(json)
# print the JSON string representation of the object
print(MethodNotAllowedErrorRep.to_json())

# convert the object into a dict
method_not_allowed_error_rep_dict = method_not_allowed_error_rep_instance.to_dict()
# create an instance of MethodNotAllowedErrorRep from a dict
method_not_allowed_error_rep_from_dict = MethodNotAllowedErrorRep.from_dict(method_not_allowed_error_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


