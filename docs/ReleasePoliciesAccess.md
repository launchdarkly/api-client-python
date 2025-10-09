# ReleasePoliciesAccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**denied** | [**List[ReleasePoliciesAccessDenied]**](ReleasePoliciesAccessDenied.md) |  | 
**allowed** | [**List[ReleasePoliciesAccessAllowedRep]**](ReleasePoliciesAccessAllowedRep.md) |  | 

## Example

```python
from launchdarkly_api.models.release_policies_access import ReleasePoliciesAccess

# TODO update the JSON string below
json = "{}"
# create an instance of ReleasePoliciesAccess from a JSON string
release_policies_access_instance = ReleasePoliciesAccess.from_json(json)
# print the JSON string representation of the object
print(ReleasePoliciesAccess.to_json())

# convert the object into a dict
release_policies_access_dict = release_policies_access_instance.to_dict()
# create an instance of ReleasePoliciesAccess from a dict
release_policies_access_from_dict = ReleasePoliciesAccess.from_dict(release_policies_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


