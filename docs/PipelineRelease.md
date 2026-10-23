# PipelineRelease


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 
**name** | **str** | The release pipeline name | 
**release_pipeline_key** | **str** | The release pipeline key | 
**release_pipeline_description** | **str** | The release pipeline description | 
**phases** | [**List[PipelineReleasePhase]**](PipelineReleasePhase.md) | An ordered list of the release pipeline phases | 
**version** | **int** | The release version | 
**release_variation_id** | **str** | The chosen release variation ID to use across all phases of a release | [optional] 
**canceled_at** | **int** |  | [optional] 

## Example

```python
from launchdarkly_api.models.pipeline_release import PipelineRelease

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineRelease from a JSON string
pipeline_release_instance = PipelineRelease.from_json(json)
# print the JSON string representation of the object
print(PipelineRelease.to_json())

# convert the object into a dict
pipeline_release_dict = pipeline_release_instance.to_dict()
# create an instance of PipelineRelease from a dict
pipeline_release_from_dict = PipelineRelease.from_dict(pipeline_release_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


