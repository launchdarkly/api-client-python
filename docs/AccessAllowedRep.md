# AccessAllowedRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**reason** | [**AccessAllowedReason**](AccessAllowedReason.md) |  | 

## Example

```python
from launchdarkly_api.models.access_allowed_rep import AccessAllowedRep

# TODO update the JSON string below
json = "{}"
# create an instance of AccessAllowedRep from a JSON string
access_allowed_rep_instance = AccessAllowedRep.from_json(json)
# print the JSON string representation of the object
print(AccessAllowedRep.to_json())

# convert the object into a dict
access_allowed_rep_dict = access_allowed_rep_instance.to_dict()
# create an instance of AccessAllowedRep from a dict
access_allowed_rep_from_dict = AccessAllowedRep.from_dict(access_allowed_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


