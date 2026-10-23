# PipelineReleaseProgression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **int** |  | 
**completed_at** | **int** |  | [optional] 
**flag_key** | **str** | The flag key | 
**active_phase_id** | **str** | The ID of the currently active release phase | [optional] 
**active_phase_status** | **str** |  | [optional] 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 

## Example

```python
from launchdarkly_api.models.pipeline_release_progression import PipelineReleaseProgression

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineReleaseProgression from a JSON string
pipeline_release_progression_instance = PipelineReleaseProgression.from_json(json)
# print the JSON string representation of the object
print(PipelineReleaseProgression.to_json())

# convert the object into a dict
pipeline_release_progression_dict = pipeline_release_progression_instance.to_dict()
# create an instance of PipelineReleaseProgression from a dict
pipeline_release_progression_from_dict = PipelineReleaseProgression.from_dict(pipeline_release_progression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


