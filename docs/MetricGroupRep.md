# MetricGroupRep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of this metric group | 
**key** | **str** | A unique key to reference the metric group | 
**name** | **str** | A human-friendly name for the metric group | 
**kind** | **str** | The type of the metric group | 
**links** | [**{str: (Link,)}**](Link.md) | The location and content type of related resources | 
**tags** | **[str]** | Tags for the metric group | 
**creation_date** | **int** |  | 
**last_modified** | **int** |  | 
**maintainer** | [**MaintainerRep**](MaintainerRep.md) |  | 
**metrics** | [**[MetricInGroupRep]**](MetricInGroupRep.md) | An ordered list of the metrics in this metric group | 
**version** | **int** | The version of this metric group | 
**description** | **str** | Description of the metric group | [optional] 
**access** | [**Access**](Access.md) |  | [optional] 
**experiments** | [**DependentExperimentListRep**](DependentExperimentListRep.md) |  | [optional] 
**experiment_count** | **int** | The number of experiments using this metric group | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


