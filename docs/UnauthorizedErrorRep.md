# UnauthorizedErrorRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specific error code encountered | 
**message** | **str** | Description of the error | 

## Example

```python
from launchdarkly_api.models.unauthorized_error_rep import UnauthorizedErrorRep

# TODO update the JSON string below
json = "{}"
# create an instance of UnauthorizedErrorRep from a JSON string
unauthorized_error_rep_instance = UnauthorizedErrorRep.from_json(json)
# print the JSON string representation of the object
print(UnauthorizedErrorRep.to_json())

# convert the object into a dict
unauthorized_error_rep_dict = unauthorized_error_rep_instance.to_dict()
# create an instance of UnauthorizedErrorRep from a dict
unauthorized_error_rep_from_dict = UnauthorizedErrorRep.from_dict(unauthorized_error_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


