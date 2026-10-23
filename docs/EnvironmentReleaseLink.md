# EnvironmentReleaseLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from launchdarkly_api.models.environment_release_link import EnvironmentReleaseLink

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentReleaseLink from a JSON string
environment_release_link_instance = EnvironmentReleaseLink.from_json(json)
# print the JSON string representation of the object
print(EnvironmentReleaseLink.to_json())

# convert the object into a dict
environment_release_link_dict = environment_release_link_instance.to_dict()
# create an instance of EnvironmentReleaseLink from a dict
environment_release_link_from_dict = EnvironmentReleaseLink.from_dict(environment_release_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


