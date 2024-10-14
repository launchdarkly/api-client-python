# ReleasePipeline


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Timestamp of when the release pipeline was created | 
**key** | **str** | The release pipeline key | 
**name** | **str** | The release pipeline name | 
**phases** | [**[Phase]**](Phase.md) | An ordered list of the release pipeline phases. Each phase is a logical grouping of one or more environments that share attributes for rolling out changes. | 
**description** | **str** | The release pipeline description | [optional] 
**tags** | **[str]** | A list of the release pipeline&#39;s tags | [optional] 
**version** | **int** | The release pipeline version | [optional] 
**access** | [**Access**](Access.md) |  | [optional] 
**is_project_default** | **bool** | Whether this release pipeline is the default pipeline for the project | [optional] 
**is_legacy** | **bool** | Whether this release pipeline is a legacy pipeline | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


