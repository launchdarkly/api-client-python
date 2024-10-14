# CreateReleasePipelineInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The unique identifier of this release pipeline | 
**name** | **str** | The name of the release pipeline | 
**phases** | [**[CreatePhaseInput]**](CreatePhaseInput.md) | A logical grouping of one or more environments that share attributes for rolling out changes | 
**description** | **str** | The release pipeline description | [optional] 
**tags** | **[str]** | A list of tags for this release pipeline | [optional] 
**is_project_default** | **bool** | Whether or not the newly created pipeline should be set as the default pipeline for this project | [optional] 
**is_legacy** | **bool** | Whether or not the pipeline is enabled for Release Automation. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


