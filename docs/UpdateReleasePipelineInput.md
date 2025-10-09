# UpdateReleasePipelineInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The release pipeline description | [optional] 
**name** | **str** | The name of the release pipeline | 
**phases** | [**List[CreatePhaseInput]**](CreatePhaseInput.md) | A logical grouping of one or more environments that share attributes for rolling out changes | 
**tags** | **List[str]** | A list of tags for this release pipeline | [optional] 

## Example

```python
from launchdarkly_api.models.update_release_pipeline_input import UpdateReleasePipelineInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateReleasePipelineInput from a JSON string
update_release_pipeline_input_instance = UpdateReleasePipelineInput.from_json(json)
# print the JSON string representation of the object
print(UpdateReleasePipelineInput.to_json())

# convert the object into a dict
update_release_pipeline_input_dict = update_release_pipeline_input_instance.to_dict()
# create an instance of UpdateReleasePipelineInput from a dict
update_release_pipeline_input_from_dict = UpdateReleasePipelineInput.from_dict(update_release_pipeline_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


