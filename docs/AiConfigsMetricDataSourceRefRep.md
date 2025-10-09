# AiConfigsMetricDataSourceRefRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**environment_key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**integration_key** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.ai_configs_metric_data_source_ref_rep import AiConfigsMetricDataSourceRefRep

# TODO update the JSON string below
json = "{}"
# create an instance of AiConfigsMetricDataSourceRefRep from a JSON string
ai_configs_metric_data_source_ref_rep_instance = AiConfigsMetricDataSourceRefRep.from_json(json)
# print the JSON string representation of the object
print(AiConfigsMetricDataSourceRefRep.to_json())

# convert the object into a dict
ai_configs_metric_data_source_ref_rep_dict = ai_configs_metric_data_source_ref_rep_instance.to_dict()
# create an instance of AiConfigsMetricDataSourceRefRep from a dict
ai_configs_metric_data_source_ref_rep_from_dict = AiConfigsMetricDataSourceRefRep.from_dict(ai_configs_metric_data_source_ref_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


