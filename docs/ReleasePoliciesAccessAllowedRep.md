# ReleasePoliciesAccessAllowedRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**reason** | [**ReleasePoliciesAccessAllowedReason**](ReleasePoliciesAccessAllowedReason.md) |  | 

## Example

```python
from launchdarkly_api.models.release_policies_access_allowed_rep import ReleasePoliciesAccessAllowedRep

# TODO update the JSON string below
json = "{}"
# create an instance of ReleasePoliciesAccessAllowedRep from a JSON string
release_policies_access_allowed_rep_instance = ReleasePoliciesAccessAllowedRep.from_json(json)
# print the JSON string representation of the object
print(ReleasePoliciesAccessAllowedRep.to_json())

# convert the object into a dict
release_policies_access_allowed_rep_dict = release_policies_access_allowed_rep_instance.to_dict()
# create an instance of ReleasePoliciesAccessAllowedRep from a dict
release_policies_access_allowed_rep_from_dict = ReleasePoliciesAccessAllowedRep.from_dict(release_policies_access_allowed_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


