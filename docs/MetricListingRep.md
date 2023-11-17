# MetricListingRep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of this metric | 
**key** | **str** | A unique key to reference the metric | 
**name** | **str** | A human-friendly name for the metric | 
**kind** | **str** | The kind of event the metric tracks | 
**links** | [**{str: (Link,)}**](Link.md) | The location and content type of related resources | 
**tags** | **[str]** | Tags for the metric | 
**creation_date** | **int** |  | 
**experiment_count** | **int** | The number of experiments using this metric | [optional] 
**attached_flag_count** | **int** | The number of feature flags currently attached to this metric | [optional] 
**site** | [**Link**](Link.md) |  | [optional] 
**access** | [**Access**](Access.md) |  | [optional] 
**last_modified** | [**Modification**](Modification.md) |  | [optional] 
**maintainer_id** | **str** | The ID of the member who maintains this metric | [optional] 
**maintainer** | [**MemberSummary**](MemberSummary.md) |  | [optional] 
**description** | **str** | Description of the metric | [optional] 
**is_numeric** | **bool** | For custom metrics, whether to track numeric changes in value against a baseline (&lt;code&gt;true&lt;/code&gt;) or to track a conversion when an end user takes an action (&lt;code&gt;false&lt;/code&gt;). | [optional] 
**success_criteria** | **str** | For custom metrics, the success criteria | [optional] 
**unit** | **str** | For numeric custom metrics, the unit of measure | [optional] 
**event_key** | **str** | For custom metrics, the event key to use in your code | [optional] 
**randomization_units** | **[str]** | An array of randomization units allowed for this metric | [optional] 
**unit_aggregation_type** | **str** | The method in which multiple unit event values are aggregated | [optional] 
**analysis_type** | **str** | The strategy for analyzing metric events | [optional] 
**percentile_value** | **int** | The percentile, an integer denoting the target percentile between 0 and 100. Only present when &lt;code&gt;analysisType&lt;/code&gt; is &lt;code&gt;percentile&lt;/code&gt;. | [optional] 
**event_default** | [**MetricEventDefaultRep**](MetricEventDefaultRep.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


