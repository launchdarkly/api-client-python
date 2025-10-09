# Release


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 
**name** | **str** | The release pipeline name | 
**release_pipeline_key** | **str** | The release pipeline key | 
**release_pipeline_description** | **str** | The release pipeline description | 
**phases** | [**List[ReleasePhase]**](ReleasePhase.md) | An ordered list of the release pipeline phases | 
**version** | **int** | The release version | 
**release_variation_id** | **str** | The chosen release variation ID to use across all phases of a release | [optional] 
**canceled_at** | **int** |  | [optional] 

## Example

```python
from launchdarkly_api.models.release import Release

# TODO update the JSON string below
json = "{}"
# create an instance of Release from a JSON string
release_instance = Release.from_json(json)
# print the JSON string representation of the object
print(Release.to_json())

# convert the object into a dict
release_dict = release_instance.to_dict()
# create an instance of Release from a dict
release_from_dict = Release.from_dict(release_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


