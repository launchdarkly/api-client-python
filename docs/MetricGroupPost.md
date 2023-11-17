# MetricGroupPost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A unique key to reference the metric group | 
**name** | **str** | A human-friendly name for the metric group | 
**maintainer_id** | **str** | The ID of the member who maintains this metric group | 
**tags** | **[str]** | Tags for the metric group | 
**metrics** | [**[MetricInMetricGroupInput]**](MetricInMetricGroupInput.md) | An ordered list of the metrics in this metric group | 
**kind** | **str** | The type of the metric group | defaults to "funnel"
**description** | **str** | Description of the metric group | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


