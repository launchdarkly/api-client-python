# DenominatorPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_name** | **str** | The warehouse event column for the denominator. Required. | [optional] 
**is_numeric** | **bool** | Whether the denominator aggregates a numeric value | [optional] 
**data_source** | [**MetricDataSourceRefRep**](MetricDataSourceRefRep.md) |  | [optional] 
**unit_aggregation_type** | **str** | How individual unit values are aggregated. One of: average, sum, count_distinct | [optional] 
**unit_aggregation_field** | **str** | The warehouse column to use for counting distinct values. Required when the unitAggregationType is count_distinct. | [optional] 
**filters** | [**EventFilter**](EventFilter.md) |  | [optional] 
**window_start_offset** | **int** | Start of the measurement window in milliseconds | [optional] 
**window_end_offset** | **int** | End of the measurement window in milliseconds | [optional] 
**winsor_lower_percentile** | **float** | Lower winsorization percentile in the open interval (0, 100) | [optional] 
**winsor_upper_percentile** | **float** | Upper winsorization percentile in the open interval (0, 100) | [optional] 
**winsor_exclude_imputed** | **bool** | Deprecated and ignored. Use winsorIncludeImputed instead. | [optional] 
**winsor_include_imputed** | **bool** | When true, includes imputed zeros in the percentile bound calculation | [optional] 

## Example

```python
from launchdarkly_api.models.denominator_post import DenominatorPost

# TODO update the JSON string below
json = "{}"
# create an instance of DenominatorPost from a JSON string
denominator_post_instance = DenominatorPost.from_json(json)
# print the JSON string representation of the object
print(DenominatorPost.to_json())

# convert the object into a dict
denominator_post_dict = denominator_post_instance.to_dict()
# create an instance of DenominatorPost from a dict
denominator_post_from_dict = DenominatorPost.from_dict(denominator_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


