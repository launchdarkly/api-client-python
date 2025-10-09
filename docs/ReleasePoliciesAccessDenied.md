# ReleasePoliciesAccessDenied


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**reason** | [**ReleasePoliciesAccessDeniedReason**](ReleasePoliciesAccessDeniedReason.md) |  | 

## Example

```python
from launchdarkly_api.models.release_policies_access_denied import ReleasePoliciesAccessDenied

# TODO update the JSON string below
json = "{}"
# create an instance of ReleasePoliciesAccessDenied from a JSON string
release_policies_access_denied_instance = ReleasePoliciesAccessDenied.from_json(json)
# print the JSON string representation of the object
print(ReleasePoliciesAccessDenied.to_json())

# convert the object into a dict
release_policies_access_denied_dict = release_policies_access_denied_instance.to_dict()
# create an instance of ReleasePoliciesAccessDenied from a dict
release_policies_access_denied_from_dict = ReleasePoliciesAccessDenied.from_dict(release_policies_access_denied_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


