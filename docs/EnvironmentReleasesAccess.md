# EnvironmentReleasesAccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**denied** | [**List[EnvironmentReleasesAccessDenied]**](EnvironmentReleasesAccessDenied.md) |  | 
**allowed** | [**List[EnvironmentReleasesAccessAllowedRep]**](EnvironmentReleasesAccessAllowedRep.md) |  | 

## Example

```python
from launchdarkly_api.models.environment_releases_access import EnvironmentReleasesAccess

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentReleasesAccess from a JSON string
environment_releases_access_instance = EnvironmentReleasesAccess.from_json(json)
# print the JSON string representation of the object
print(EnvironmentReleasesAccess.to_json())

# convert the object into a dict
environment_releases_access_dict = environment_releases_access_instance.to_dict()
# create an instance of EnvironmentReleasesAccess from a dict
environment_releases_access_from_dict = EnvironmentReleasesAccess.from_dict(environment_releases_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


