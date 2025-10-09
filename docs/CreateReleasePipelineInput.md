# CreateReleasePipelineInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The release pipeline description | [optional] 
**key** | **str** | The unique identifier of this release pipeline | 
**name** | **str** | The name of the release pipeline | 
**phases** | [**List[CreatePhaseInput]**](CreatePhaseInput.md) | A logical grouping of one or more environments that share attributes for rolling out changes | 
**tags** | **List[str]** | A list of tags for this release pipeline | [optional] 
**is_project_default** | **bool** | Whether or not the newly created pipeline should be set as the default pipeline for this project | [optional] 
**is_legacy** | **bool** | Whether or not the pipeline is enabled for Release Automation. | [optional] 

## Example

```python
from launchdarkly_api.models.create_release_pipeline_input import CreateReleasePipelineInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateReleasePipelineInput from a JSON string
create_release_pipeline_input_instance = CreateReleasePipelineInput.from_json(json)
# print the JSON string representation of the object
print(CreateReleasePipelineInput.to_json())

# convert the object into a dict
create_release_pipeline_input_dict = create_release_pipeline_input_instance.to_dict()
# create an instance of CreateReleasePipelineInput from a dict
create_release_pipeline_input_from_dict = CreateReleasePipelineInput.from_dict(create_release_pipeline_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


