# ValidationFailedErrorRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specific error code encountered | 
**message** | **str** | Description of the error | 
**errors** | [**List[FailureReasonRep]**](FailureReasonRep.md) | List of validation errors | 

## Example

```python
from launchdarkly_api.models.validation_failed_error_rep import ValidationFailedErrorRep

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationFailedErrorRep from a JSON string
validation_failed_error_rep_instance = ValidationFailedErrorRep.from_json(json)
# print the JSON string representation of the object
print(ValidationFailedErrorRep.to_json())

# convert the object into a dict
validation_failed_error_rep_dict = validation_failed_error_rep_instance.to_dict()
# create an instance of ValidationFailedErrorRep from a dict
validation_failed_error_rep_from_dict = ValidationFailedErrorRep.from_dict(validation_failed_error_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


