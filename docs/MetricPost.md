# MetricPost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A unique key to reference the metric | 
**kind** | **str** | The kind of event your metric will track | 
**name** | **str** | A human-friendly name for the metric | [optional] 
**description** | **str** | Description of the metric | [optional] 
**selector** | **str** | One or more CSS selectors. Required for click metrics only. | [optional] 
**urls** | [**[UrlPost]**](UrlPost.md) | One or more target URLs. Required for click and pageview metrics only. | [optional] 
**is_active** | **bool** | Whether the metric is active. Set to &lt;code&gt;true&lt;/code&gt; to record click or pageview metrics. Not applicable for custom metrics. | [optional] 
**is_numeric** | **bool** | Whether to track numeric changes in value against a baseline (&lt;code&gt;true&lt;/code&gt;) or to track a conversion when an end user takes an action (&lt;code&gt;false&lt;/code&gt;). Required for custom metrics only. | [optional] 
**unit** | **str** | The unit of measure. Applicable for numeric custom metrics only. | [optional] 
**event_key** | **str** | The event key to use in your code. Required for custom metrics only. | [optional] 
**success_criteria** | **str** | Success criteria. Required for custom numeric metrics, optional for custom conversion metrics. | [optional] 
**tags** | **[str]** | Tags for the metric | [optional] 
**randomization_units** | **[str]** | An array of randomization units allowed for this metric | [optional] 
**unit_aggregation_type** | **str** | The method in which multiple unit event values are aggregated | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


