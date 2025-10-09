# NotFoundErrorRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specific error code encountered | 
**message** | **str** | Description of the error | 

## Example

```python
from launchdarkly_api.models.not_found_error_rep import NotFoundErrorRep

# TODO update the JSON string below
json = "{}"
# create an instance of NotFoundErrorRep from a JSON string
not_found_error_rep_instance = NotFoundErrorRep.from_json(json)
# print the JSON string representation of the object
print(NotFoundErrorRep.to_json())

# convert the object into a dict
not_found_error_rep_dict = not_found_error_rep_instance.to_dict()
# create an instance of NotFoundErrorRep from a dict
not_found_error_rep_from_dict = NotFoundErrorRep.from_dict(not_found_error_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


