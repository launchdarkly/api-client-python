# MetricDenominatorRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_name** | **str** | The warehouse event column for the denominator | [optional] 
**is_numeric** | **bool** | Whether the denominator aggregates a numeric value | [optional] 
**unit_aggregation_type** | **str** | How individual unit values are aggregated for the denominator | [optional] 
**unit_aggregation_field** | **str** | The column to count distinct values of; required when unitAggregationType is count_distinct | [optional] 
**data_source** | [**MetricDataSourceRefRep**](MetricDataSourceRefRep.md) |  | [optional] 
**filters** | [**Filter**](Filter.md) |  | [optional] 
**window_start_offset** | **int** | Start of the measurement window in milliseconds | [optional] 
**window_end_offset** | **int** | End of the measurement window in milliseconds | [optional] 
**winsor_lower_percentile** | **float** | Lower winsorization percentile in the open interval (0, 100) | [optional] 
**winsor_upper_percentile** | **float** | Upper winsorization percentile in the open interval (0, 100) | [optional] 
**winsor_exclude_imputed** | **bool** | Deprecated and ignored. Use winsorIncludeImputed instead. | [optional] 
**winsor_include_imputed** | **bool** | When true, the percentile bound calculation includes imputed zeros | [optional] 

## Example

```python
from launchdarkly_api.models.metric_denominator_rep import MetricDenominatorRep

# TODO update the JSON string below
json = "{}"
# create an instance of MetricDenominatorRep from a JSON string
metric_denominator_rep_instance = MetricDenominatorRep.from_json(json)
# print the JSON string representation of the object
print(MetricDenominatorRep.to_json())

# convert the object into a dict
metric_denominator_rep_dict = metric_denominator_rep_instance.to_dict()
# create an instance of MetricDenominatorRep from a dict
metric_denominator_rep_from_dict = MetricDenominatorRep.from_dict(metric_denominator_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


