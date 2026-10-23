# EnvironmentReleasesAccessAllowedRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**reason** | [**AccessAllowedReason**](AccessAllowedReason.md) |  | 

## Example

```python
from launchdarkly_api.models.environment_releases_access_allowed_rep import EnvironmentReleasesAccessAllowedRep

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentReleasesAccessAllowedRep from a JSON string
environment_releases_access_allowed_rep_instance = EnvironmentReleasesAccessAllowedRep.from_json(json)
# print the JSON string representation of the object
print(EnvironmentReleasesAccessAllowedRep.to_json())

# convert the object into a dict
environment_releases_access_allowed_rep_dict = environment_releases_access_allowed_rep_instance.to_dict()
# create an instance of EnvironmentReleasesAccessAllowedRep from a dict
environment_releases_access_allowed_rep_from_dict = EnvironmentReleasesAccessAllowedRep.from_dict(environment_releases_access_allowed_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


