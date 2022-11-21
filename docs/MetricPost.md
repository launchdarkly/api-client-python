# MetricPost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A unique key to reference the metric | 
**kind** | **str** | The kind of event your metric will track | 
**name** | **str** | A human-friendly name for the metric | [optional] 
**description** | **str** | Description of the metric | [optional] 
**selector** | **str** | One or more CSS selectors. Required for click metrics. | [optional] 
**urls** | [**[UrlPost]**](UrlPost.md) | One or more target URLs. Required for click and pageview metrics. | [optional] 
**is_active** | **bool** | Whether the metric is active | [optional] 
**is_numeric** | **bool** | Whether to track numeric changes in value against a baseline (&lt;code&gt;true&lt;/code&gt;) or to track a conversion when users taken an action (&lt;code&gt;false&lt;/code&gt;). Required for custom metrics. | [optional] 
**unit** | **str** | The unit of measure. Only for numeric custom metrics. | [optional] 
**event_key** | **str** | The event name to use in your code. Required for custom metrics. | [optional] 
**success_criteria** | **str** | Success criteria. Required for numeric custom metrics. | [optional] 
**tags** | **[str]** | Tags for the metric | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


