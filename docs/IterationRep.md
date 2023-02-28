# IterationRep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hypothesis** | **str** | The expected outcome of this experiment | 
**status** | **str** | The status of the iteration: &lt;code&gt;not_started&lt;/code&gt;, &lt;code&gt;running&lt;/code&gt;, &lt;code&gt;stopped&lt;/code&gt; | 
**created_at** | **int** |  | 
**id** | **str** | The iteration ID | [optional] 
**started_at** | **int** |  | [optional] 
**ended_at** | **int** |  | [optional] 
**winning_treatment_id** | **str** | The ID of the treatment chosen when the experiment stopped | [optional] 
**winning_reason** | **str** | The reason you stopped the experiment | [optional] 
**can_reshuffle_traffic** | **bool** | Whether the experiment may reassign traffic to different variations when the experiment audience changes (true) or must keep all traffic assigned to its initial variation (false). | [optional] 
**flags** | [**{str: (FlagRep,)}**](FlagRep.md) | Details on the flag used in this experiment | [optional] 
**primary_metric** | [**MetricV2Rep**](MetricV2Rep.md) |  | [optional] 
**randomization_unit** | **str** | The unit of randomization for this iteration | [optional] 
**treatments** | [**[TreatmentRep]**](TreatmentRep.md) | Details on the variations you are testing in the experiment | [optional] 
**secondary_metrics** | [**[MetricV2Rep]**](MetricV2Rep.md) | Details on the secondary metrics for this experiment | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


