# AccessDenied


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**reason** | [**AccessDeniedReason**](AccessDeniedReason.md) |  | 

## Example

```python
from launchdarkly_api.models.access_denied import AccessDenied

# TODO update the JSON string below
json = "{}"
# create an instance of AccessDenied from a JSON string
access_denied_instance = AccessDenied.from_json(json)
# print the JSON string representation of the object
print(AccessDenied.to_json())

# convert the object into a dict
access_denied_dict = access_denied_instance.to_dict()
# create an instance of AccessDenied from a dict
access_denied_from_dict = AccessDenied.from_dict(access_denied_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


