# DependentMetricOrMetricGroupRep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A unique key to reference the metric or metric group | 
**name** | **str** | A human-friendly name for the metric or metric group | 
**kind** | **str** | If this is a metric, then it represents the kind of event the metric tracks. If this is a metric group, then it represents the group type | 
**links** | [**{str: (Link,)}**](Link.md) | The location and content type of related resources | 
**is_group** | **bool** | Whether this is a metric group or a metric | 
**metrics** | [**[MetricInGroupRep]**](MetricInGroupRep.md) | An ordered list of the metrics in this metric group | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


