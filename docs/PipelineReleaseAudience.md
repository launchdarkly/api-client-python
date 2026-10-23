# PipelineReleaseAudience


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The audience ID | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 
**environment** | [**EnvironmentSummary**](EnvironmentSummary.md) |  | [optional] 
**name** | **str** | The release phase name | 
**configuration** | [**AudienceConfiguration**](AudienceConfiguration.md) |  | [optional] 
**segment_keys** | **List[str]** | A list of segment keys | [optional] 
**status** | **str** |  | [optional] 
**rule_ids** | **List[str]** | The rules IDs added or updated by this audience | [optional] 

## Example

```python
from launchdarkly_api.models.pipeline_release_audience import PipelineReleaseAudience

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineReleaseAudience from a JSON string
pipeline_release_audience_instance = PipelineReleaseAudience.from_json(json)
# print the JSON string representation of the object
print(PipelineReleaseAudience.to_json())

# convert the object into a dict
pipeline_release_audience_dict = pipeline_release_audience_instance.to_dict()
# create an instance of PipelineReleaseAudience from a dict
pipeline_release_audience_from_dict = PipelineReleaseAudience.from_dict(pipeline_release_audience_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


