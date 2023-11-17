# DesignRep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hypothesis** | **str** | The expected outcome of this experiment | 
**can_reshuffle_traffic** | **bool** | Whether the experiment can reassign traffic to different variations when you increase or decrease the traffic in your experiment audience (true) or keep all traffic assigned to its initial variation (false). | [optional] 
**flags** | [**{str: (FlagRep,)}**](FlagRep.md) | Details on the flag used in this experiment | [optional] 
**primary_metric** | [**DependentMetricOrMetricGroupRep**](DependentMetricOrMetricGroupRep.md) |  | [optional] 
**randomization_unit** | **str** | The unit of randomization for this iteration | [optional] 
**treatments** | [**[TreatmentRep]**](TreatmentRep.md) | Details on the variations you are testing in the experiment | [optional] 
**secondary_metrics** | [**[MetricV2Rep]**](MetricV2Rep.md) | Details on the secondary metrics for this experiment | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


