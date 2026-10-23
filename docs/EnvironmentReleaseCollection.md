# EnvironmentReleaseCollection

One page of environment releases for one flag in one environment, newest first.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[EnvironmentRelease]**](EnvironmentRelease.md) | The releases on this page. | 
**total_count** | **int** | The total number of releases that match the request, before &#x60;limit&#x60; and &#x60;offset&#x60; are applied. | 
**links** | [**Dict[str, EnvironmentReleaseLink]**](EnvironmentReleaseLink.md) | Links to this page (&#x60;self&#x60;), the flag (&#x60;parent&#x60;), and, where they apply, the &#x60;first&#x60;, &#x60;prev&#x60;, &#x60;next&#x60;, and &#x60;last&#x60; pages. | [optional] 

## Example

```python
from launchdarkly_api.models.environment_release_collection import EnvironmentReleaseCollection

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentReleaseCollection from a JSON string
environment_release_collection_instance = EnvironmentReleaseCollection.from_json(json)
# print the JSON string representation of the object
print(EnvironmentReleaseCollection.to_json())

# convert the object into a dict
environment_release_collection_dict = environment_release_collection_instance.to_dict()
# create an instance of EnvironmentReleaseCollection from a dict
environment_release_collection_from_dict = EnvironmentReleaseCollection.from_dict(environment_release_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


