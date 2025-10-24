# IterationRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The iteration ID | [optional] 
**hypothesis** | **str** | The expected outcome of this experiment | 
**status** | **str** | The status of the iteration: &lt;code&gt;not_started&lt;/code&gt;, &lt;code&gt;running&lt;/code&gt;, &lt;code&gt;stopped&lt;/code&gt; | 
**created_at** | **int** |  | 
**started_at** | **int** |  | [optional] 
**ended_at** | **int** |  | [optional] 
**winning_treatment_id** | **str** | The ID of the treatment chosen when the experiment stopped | [optional] 
**winning_reason** | **str** | The reason you stopped the experiment | [optional] 
**can_reshuffle_traffic** | **bool** | Whether the experiment may reassign traffic to different variations when the experiment audience changes (true) or must keep all traffic assigned to its initial variation (false). | [optional] 
**flags** | [**Dict[str, FlagRep]**](FlagRep.md) | Details on the flag used in this experiment | [optional] 
**reallocation_frequency_millis** | **int** | The cadence (in milliseconds) to update the allocation. Only present for multi-armed bandits. | [optional] 
**version** | **int** | The current version that the iteration is on | [optional] 
**primary_metric** | [**DependentMetricOrMetricGroupRep**](DependentMetricOrMetricGroupRep.md) |  | [optional] 
**primary_single_metric** | [**MetricV2Rep**](MetricV2Rep.md) |  | [optional] 
**primary_funnel** | [**DependentMetricGroupRepWithMetrics**](DependentMetricGroupRepWithMetrics.md) |  | [optional] 
**randomization_unit** | **str** | The unit of randomization for this iteration | [optional] 
**attributes** | **List[str]** | The available attribute filters for this iteration | [optional] 
**treatments** | [**List[TreatmentRep]**](TreatmentRep.md) | Details on the variations you are testing in the experiment | [optional] 
**secondary_metrics** | [**List[MetricV2Rep]**](MetricV2Rep.md) | Deprecated, use &lt;code&gt;metrics&lt;/code&gt; instead. Details on the secondary metrics for this experiment. | [optional] 
**metrics** | [**List[DependentMetricOrMetricGroupRep]**](DependentMetricOrMetricGroupRep.md) | Details on the metrics for this experiment | [optional] 
**layer_snapshot** | [**LayerSnapshotRep**](LayerSnapshotRep.md) |  | [optional] 
**covariance_info** | [**CovarianceInfoRep**](CovarianceInfoRep.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.iteration_rep import IterationRep

# TODO update the JSON string below
json = "{}"
# create an instance of IterationRep from a JSON string
iteration_rep_instance = IterationRep.from_json(json)
# print the JSON string representation of the object
print(IterationRep.to_json())

# convert the object into a dict
iteration_rep_dict = iteration_rep_instance.to_dict()
# create an instance of IterationRep from a dict
iteration_rep_from_dict = IterationRep.from_dict(iteration_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


