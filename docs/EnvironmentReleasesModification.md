# EnvironmentReleasesModification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** |  | [optional] 

## Example

```python
from launchdarkly_api.models.environment_releases_modification import EnvironmentReleasesModification

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentReleasesModification from a JSON string
environment_releases_modification_instance = EnvironmentReleasesModification.from_json(json)
# print the JSON string representation of the object
print(EnvironmentReleasesModification.to_json())

# convert the object into a dict
environment_releases_modification_dict = environment_releases_modification_instance.to_dict()
# create an instance of EnvironmentReleasesModification from a dict
environment_releases_modification_from_dict = EnvironmentReleasesModification.from_dict(environment_releases_modification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


