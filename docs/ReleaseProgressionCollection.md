# ReleaseProgressionCollection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_count** | **int** | The number of active releases | 
**completed_count** | **int** | The number of completed releases | 
**items** | [**[ReleaseProgression]**](ReleaseProgression.md) | A list of details for each release, across all flags, for this release pipeline | 
**phases** | [**[PhaseInfo]**](PhaseInfo.md) | A list of details for each phase, across all releases, for this release pipeline | 
**total_count** | **int** | The total number of releases for this release pipeline | 
**links** | [**{str: (Link,)}**](Link.md) | The location and content type of related resources | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


