# CreatePipelineReleaseInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**release_variation_id** | **str** | The variation id to release to across all phases | [optional] 
**release_pipeline_key** | **str** | The key of the release pipeline to attach the flag to | 

## Example

```python
from launchdarkly_api.models.create_pipeline_release_input import CreatePipelineReleaseInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePipelineReleaseInput from a JSON string
create_pipeline_release_input_instance = CreatePipelineReleaseInput.from_json(json)
# print the JSON string representation of the object
print(CreatePipelineReleaseInput.to_json())

# convert the object into a dict
create_pipeline_release_input_dict = create_pipeline_release_input_instance.to_dict()
# create an instance of CreatePipelineReleaseInput from a dict
create_pipeline_release_input_from_dict = CreatePipelineReleaseInput.from_dict(create_pipeline_release_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


