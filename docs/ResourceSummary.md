# ResourceSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flag_count** | **int** |  | 
**segment_count** | **int** |  | [optional] 
**metric_count** | **int** |  | [optional] 
**ai_config_count** | **int** |  | [optional] 
**total_count** | **int** |  | 

## Example

```python
from launchdarkly_api.models.resource_summary import ResourceSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSummary from a JSON string
resource_summary_instance = ResourceSummary.from_json(json)
# print the JSON string representation of the object
print(ResourceSummary.to_json())

# convert the object into a dict
resource_summary_dict = resource_summary_instance.to_dict()
# create an instance of ResourceSummary from a dict
resource_summary_from_dict = ResourceSummary.from_dict(resource_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


