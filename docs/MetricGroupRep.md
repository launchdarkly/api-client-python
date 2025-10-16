# MetricGroupRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of this metric group | 
**key** | **str** | A unique key to reference the metric group | 
**name** | **str** | A human-friendly name for the metric group | 
**kind** | **str** | The type of the metric group | 
**description** | **str** | Description of the metric group | [optional] 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**access** | [**Access**](Access.md) |  | [optional] 
**tags** | **List[str]** | Tags for the metric group | 
**creation_date** | **int** |  | 
**last_modified** | **int** |  | 
**maintainer** | [**MaintainerRep**](MaintainerRep.md) |  | 
**metrics** | [**List[MetricInGroupRep]**](MetricInGroupRep.md) | An ordered list of the metrics in this metric group | 
**version** | **int** | The version of this metric group | 
**experiments** | [**List[DependentExperimentRep]**](DependentExperimentRep.md) |  | [optional] 
**experiment_count** | **int** | The number of experiments using this metric group | [optional] 
**active_experiment_count** | **int** | The number of active experiments using this metric group | [optional] 
**active_guarded_rollout_count** | **int** | The number of active guarded rollouts using this metric group | [optional] 
**total_connections_count** | **int** | The total number of connections using this metric group | [optional] 
**total_active_connections_count** | **int** | The total number of active connections using this metric group | [optional] 

## Example

```python
from launchdarkly_api.models.metric_group_rep import MetricGroupRep

# TODO update the JSON string below
json = "{}"
# create an instance of MetricGroupRep from a JSON string
metric_group_rep_instance = MetricGroupRep.from_json(json)
# print the JSON string representation of the object
print(MetricGroupRep.to_json())

# convert the object into a dict
metric_group_rep_dict = metric_group_rep_instance.to_dict()
# create an instance of MetricGroupRep from a dict
metric_group_rep_from_dict = MetricGroupRep.from_dict(metric_group_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


