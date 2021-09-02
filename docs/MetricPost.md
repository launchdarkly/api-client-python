# MetricPost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**kind** | **str** |  | 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**selector** | **str** | Required for click metrics | [optional] 
**urls** | [**[UrlPost]**](UrlPost.md) | Required for click and pageview metrics | [optional] 
**is_active** | **bool** |  | [optional] 
**is_numeric** | **bool** |  | [optional] 
**unit** | **str** |  | [optional] 
**event_key** | **str** | Required for custom metrics | [optional] 
**success_criteria** | **int** |  | [optional] 
**tags** | **[str]** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


