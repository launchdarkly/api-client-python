# ExperimentBayesianResultsRep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**{str: (Link,)}**](Link.md) | The location and content type of related resources | [optional] 
**treatment_results** | [**[TreatmentResultRep]**](TreatmentResultRep.md) | Deprecated, use &lt;code&gt;results&lt;/code&gt; instead. Only populated when response does not contain results sliced by multiple attributes. | [optional] 
**metric_seen** | [**MetricSeen**](MetricSeen.md) |  | [optional] 
**probability_of_mismatch** | **float** | The probability of a Sample Ratio Mismatch | [optional] 
**results** | [**[SlicedResultsRep]**](SlicedResultsRep.md) | A list of attribute values and their corresponding treatment results | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


