# IterationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hypothesis** | **str** | The expected outcome of this experiment | 
**can_reshuffle_traffic** | **bool** | Whether to allow the experiment to reassign traffic to different variations when you increase or decrease the traffic in your experiment audience (true) or keep all traffic assigned to its initial variation (false). Defaults to true. | [optional] 
**metrics** | [**List[MetricInput]**](MetricInput.md) |  | 
**primary_single_metric_key** | **str** | The key of the primary metric for this experiment. Either &lt;code&gt;primarySingleMetricKey&lt;/code&gt; or &lt;code&gt;primaryFunnelKey&lt;/code&gt; must be present. | [optional] 
**primary_funnel_key** | **str** | The key of the primary funnel group for this experiment. Either &lt;code&gt;primarySingleMetricKey&lt;/code&gt; or &lt;code&gt;primaryFunnelKey&lt;/code&gt; must be present. | [optional] 
**treatments** | [**List[TreatmentInput]**](TreatmentInput.md) |  | 
**flags** | [**Dict[str, FlagInput]**](FlagInput.md) |  | 
**randomization_unit** | **str** | The unit of randomization for this iteration. Defaults to user. | [optional] 
**covariance_id** | **str** | The ID of the covariance CSV | [optional] 
**attributes** | **List[str]** | The attributes that this iteration&#39;s results can be sliced by | [optional] 

## Example

```python
from launchdarkly_api.models.iteration_input import IterationInput

# TODO update the JSON string below
json = "{}"
# create an instance of IterationInput from a JSON string
iteration_input_instance = IterationInput.from_json(json)
# print the JSON string representation of the object
print(IterationInput.to_json())

# convert the object into a dict
iteration_input_dict = iteration_input_instance.to_dict()
# create an instance of IterationInput from a dict
iteration_input_from_dict = IterationInput.from_dict(iteration_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


