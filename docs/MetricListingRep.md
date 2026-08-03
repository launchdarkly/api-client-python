# MetricListingRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**experiment_count** | **int** | The number of experiments using this metric | [optional] 
**metric_group_count** | **int** | The number of metric groups using this metric | [optional] 
**active_experiment_count** | **int** | The number of active experiments using this metric | [optional] 
**active_guarded_rollout_count** | **int** | The number of active guarded rollouts using this metric | [optional] 
**id** | **str** | The ID of this metric | 
**version_id** | **str** | The version ID of the metric | 
**version** | **int** | Version of the metric | [optional] 
**key** | **str** | A unique key to reference the metric | 
**name** | **str** | A human-friendly name for the metric | 
**kind** | **str** | The kind of event the metric tracks | 
**attached_flag_count** | **int** | The number of feature flags currently attached to this metric | [optional] 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**site** | [**Link**](Link.md) |  | [optional] 
**access** | [**Access**](Access.md) |  | [optional] 
**tags** | **List[str]** | Tags for the metric | 
**creation_date** | **int** |  | 
**last_modified** | [**Modification**](Modification.md) |  | [optional] 
**maintainer_id** | **str** | The ID of the member who maintains this metric | [optional] 
**maintainer** | [**MemberSummary**](MemberSummary.md) |  | [optional] 
**description** | **str** | Description of the metric | [optional] 
**category** | **str** | The category of the metric | [optional] 
**is_numeric** | **bool** | For custom and trace metrics, whether to track numeric changes in value against a baseline (&lt;code&gt;true&lt;/code&gt;) or to track a conversion when an end user takes an action (&lt;code&gt;false&lt;/code&gt;). | [optional] 
**success_criteria** | **str** | For custom and trace metrics, the success criteria | [optional] 
**unit** | **str** | For numeric custom and trace metrics, the unit of measure | [optional] 
**event_key** | **str** | For custom metrics, the event key to use in your code | [optional] 
**randomization_units** | **List[str]** | Deprecated, use &lt;code&gt;analysisUnits&lt;/code&gt; instead. | [optional] 
**analysis_units** | **List[str]** | An array of analysis units allowed for this metric. | [optional] 
**filters** | [**Filter**](Filter.md) |  | [optional] 
**unit_aggregation_type** | **str** | The method by which multiple unit event values are aggregated | [optional] 
**analysis_type** | **str** | The method for analyzing metric events | [optional] 
**percentile_value** | **int** | The percentile for the analysis method. An integer denoting the target percentile between 0 and 100. Required when &lt;code&gt;analysisType&lt;/code&gt; is &lt;code&gt;percentile&lt;/code&gt;. | [optional] 
**event_default** | [**MetricEventDefaultRep**](MetricEventDefaultRep.md) |  | [optional] 
**data_source** | [**MetricDataSourceRefRep**](MetricDataSourceRefRep.md) |  | 
**last_seen** | **int** |  | [optional] 
**archived** | **bool** | Whether the metric version is archived | [optional] 
**archived_at** | **int** |  | [optional] 
**selector** | **str** | For click metrics, the CSS selectors | [optional] 
**urls** | **List[Dict[str, object]]** |  | [optional] 
**window_start_offset** | **int** | Not yet implemented - The start of the measurement window, in milliseconds relative to the unit&#39;s first exposure to a flag variation | [optional] 
**window_end_offset** | **int** | Not yet implemented - The end of the measurement window, in milliseconds relative to the unit&#39;s first exposure to a flag variation | [optional] 
**winsor_lower_percentile** | **float** | Lower winsorization percentile, expressed as a percent in the open interval (0, 100). When both bounds are set, defines a two-sided clamp range. Otherwise lower-only winsorization. | [optional] 
**winsor_upper_percentile** | **float** | Upper winsorization percentile, expressed as a percent in the open interval (0, 100). When both bounds are set, must be greater than winsorLowerPercentile. | [optional] 
**winsor_include_imputed** | **bool** | When true, the percentile bound calculation includes imputed zeros. Only meaningful when at least one bound is set and the metric includes units that didn&#39;t send events. | [optional] 
**trace_query** | **str** | For trace metrics, the trace query to use for the metric. | [optional] 
**trace_value_location** | **str** | For trace metrics, the location in the trace to use for numeric values. | [optional] 
**denominator** | [**MetricDenominatorRep**](MetricDenominatorRep.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.metric_listing_rep import MetricListingRep

# TODO update the JSON string below
json = "{}"
# create an instance of MetricListingRep from a JSON string
metric_listing_rep_instance = MetricListingRep.from_json(json)
# print the JSON string representation of the object
print(MetricListingRep.to_json())

# convert the object into a dict
metric_listing_rep_dict = metric_listing_rep_instance.to_dict()
# create an instance of MetricListingRep from a dict
metric_listing_rep_from_dict = MetricListingRep.from_dict(metric_listing_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


