# ExpandedMetric

Metric representation for Views API - contains only fields actually used by the Views service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A unique key used to reference the metric | [optional] 
**name** | **str** | A human-friendly name for the metric | [optional] 
**creation_date** | **int** | Creation date in milliseconds | [optional] 
**last_modified** | **int** | Last modification date in milliseconds | [optional] 
**is_active** | **bool** | Whether the metric is active | [optional] 
**event_key** | **str** | Event key for the metric | [optional] 
**id** | **str** | ID of the metric | [optional] 
**version_id** | **str** | Version ID of the metric | [optional] 
**kind** | **str** | Kind of the Metric | [optional] 
**category** | **str** | Category of the Metric | [optional] 
**description** | **str** | Description of the Metric | [optional] 
**is_numeric** | **bool** |  | [optional] 
**last_seen** | **int** | Last seen date in milliseconds | [optional] 
**links** | [**ParentAndSelfLinks**](ParentAndSelfLinks.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.expanded_metric import ExpandedMetric

# TODO update the JSON string below
json = "{}"
# create an instance of ExpandedMetric from a JSON string
expanded_metric_instance = ExpandedMetric.from_json(json)
# print the JSON string representation of the object
print(ExpandedMetric.to_json())

# convert the object into a dict
expanded_metric_dict = expanded_metric_instance.to_dict()
# create an instance of ExpandedMetric from a dict
expanded_metric_from_dict = ExpandedMetric.from_dict(expanded_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


