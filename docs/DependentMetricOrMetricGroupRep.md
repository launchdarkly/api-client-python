# DependentMetricOrMetricGroupRep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A unique key to reference the metric or metric group | 
**version_id** | **str** | The version ID of the metric or metric group | 
**name** | **str** | A human-friendly name for the metric or metric group | 
**kind** | **str** | If this is a metric, then it represents the kind of event the metric tracks. If this is a metric group, then it represents the group type | 
**links** | [**{str: (Link,)}**](Link.md) | The location and content type of related resources | 
**is_group** | **bool** | Whether this is a metric group or a metric | 
**is_numeric** | **bool** | For custom metrics, whether to track numeric changes in value against a baseline (&lt;code&gt;true&lt;/code&gt;) or to track a conversion when an end user takes an action (&lt;code&gt;false&lt;/code&gt;). | [optional] 
**metrics** | [**[MetricInGroupRep]**](MetricInGroupRep.md) | An ordered list of the metrics in this metric group | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


