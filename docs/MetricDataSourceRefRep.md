# MetricDataSourceRefRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**environment_key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**integration_key** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.metric_data_source_ref_rep import MetricDataSourceRefRep

# TODO update the JSON string below
json = "{}"
# create an instance of MetricDataSourceRefRep from a JSON string
metric_data_source_ref_rep_instance = MetricDataSourceRefRep.from_json(json)
# print the JSON string representation of the object
print(MetricDataSourceRefRep.to_json())

# convert the object into a dict
metric_data_source_ref_rep_dict = metric_data_source_ref_rep_instance.to_dict()
# create an instance of MetricDataSourceRefRep from a dict
metric_data_source_ref_rep_from_dict = MetricDataSourceRefRep.from_dict(metric_data_source_ref_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


