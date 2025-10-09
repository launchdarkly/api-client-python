# ReleasePoliciesAccessRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**denied** | [**List[ReleasePoliciesAccessDenied]**](ReleasePoliciesAccessDenied.md) |  | 
**allowed** | [**List[ReleasePoliciesAccessAllowedRep]**](ReleasePoliciesAccessAllowedRep.md) |  | 

## Example

```python
from launchdarkly_api.models.release_policies_access_rep import ReleasePoliciesAccessRep

# TODO update the JSON string below
json = "{}"
# create an instance of ReleasePoliciesAccessRep from a JSON string
release_policies_access_rep_instance = ReleasePoliciesAccessRep.from_json(json)
# print the JSON string representation of the object
print(ReleasePoliciesAccessRep.to_json())

# convert the object into a dict
release_policies_access_rep_dict = release_policies_access_rep_instance.to_dict()
# create an instance of ReleasePoliciesAccessRep from a dict
release_policies_access_rep_from_dict = ReleasePoliciesAccessRep.from_dict(release_policies_access_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


