# EnvironmentReleasesAccessDenied


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**reason** | [**AccessDeniedReason**](AccessDeniedReason.md) |  | 

## Example

```python
from launchdarkly_api.models.environment_releases_access_denied import EnvironmentReleasesAccessDenied

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentReleasesAccessDenied from a JSON string
environment_releases_access_denied_instance = EnvironmentReleasesAccessDenied.from_json(json)
# print the JSON string representation of the object
print(EnvironmentReleasesAccessDenied.to_json())

# convert the object into a dict
environment_releases_access_denied_dict = environment_releases_access_denied_instance.to_dict()
# create an instance of EnvironmentReleasesAccessDenied from a dict
environment_releases_access_denied_from_dict = EnvironmentReleasesAccessDenied.from_dict(environment_releases_access_denied_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


