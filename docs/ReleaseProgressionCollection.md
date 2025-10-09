# ReleaseProgressionCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_count** | **int** | The number of active releases | 
**completed_count** | **int** | The number of completed releases | 
**items** | [**List[ReleaseProgression]**](ReleaseProgression.md) | A list of details for each release, across all flags, for this release pipeline | 
**phases** | [**List[PhaseInfo]**](PhaseInfo.md) | A list of details for each phase, across all releases, for this release pipeline | 
**total_count** | **int** | The total number of releases for this release pipeline | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 

## Example

```python
from launchdarkly_api.models.release_progression_collection import ReleaseProgressionCollection

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseProgressionCollection from a JSON string
release_progression_collection_instance = ReleaseProgressionCollection.from_json(json)
# print the JSON string representation of the object
print(ReleaseProgressionCollection.to_json())

# convert the object into a dict
release_progression_collection_dict = release_progression_collection_instance.to_dict()
# create an instance of ReleaseProgressionCollection from a dict
release_progression_collection_from_dict = ReleaseProgressionCollection.from_dict(release_progression_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


