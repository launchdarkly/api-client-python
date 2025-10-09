# BigSegmentStoreIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**BigSegmentStoreIntegrationLinks**](BigSegmentStoreIntegrationLinks.md) |  | 
**id** | **str** | The integration ID | 
**integration_key** | **str** | The integration key | 
**project_key** | **str** | The project key | 
**environment_key** | **str** | The environment key | 
**config** | **Dict[str, object]** |  | 
**on** | **bool** | Whether the configuration is turned on | 
**tags** | **List[str]** | List of tags for this configuration | 
**name** | **str** | Name of the configuration | 
**version** | **int** | Version of the current configuration | 
**access** | [**Access**](Access.md) |  | [optional] 
**status** | [**BigSegmentStoreStatus**](BigSegmentStoreStatus.md) |  | 

## Example

```python
from launchdarkly_api.models.big_segment_store_integration import BigSegmentStoreIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of BigSegmentStoreIntegration from a JSON string
big_segment_store_integration_instance = BigSegmentStoreIntegration.from_json(json)
# print the JSON string representation of the object
print(BigSegmentStoreIntegration.to_json())

# convert the object into a dict
big_segment_store_integration_dict = big_segment_store_integration_instance.to_dict()
# create an instance of BigSegmentStoreIntegration from a dict
big_segment_store_integration_from_dict = BigSegmentStoreIntegration.from_dict(big_segment_store_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


