# ViewLinkedResourceDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | [**View**](View.md) |  | [optional] 
**flag** | [**ExpandedFlag**](ExpandedFlag.md) |  | [optional] 
**segment** | [**ExpandedSegment**](ExpandedSegment.md) |  | [optional] 
**ai_config** | [**ExpandedAIConfig**](ExpandedAIConfig.md) |  | [optional] 
**metric** | [**ExpandedMetric**](ExpandedMetric.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.view_linked_resource_details import ViewLinkedResourceDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ViewLinkedResourceDetails from a JSON string
view_linked_resource_details_instance = ViewLinkedResourceDetails.from_json(json)
# print the JSON string representation of the object
print(ViewLinkedResourceDetails.to_json())

# convert the object into a dict
view_linked_resource_details_dict = view_linked_resource_details_instance.to_dict()
# create an instance of ViewLinkedResourceDetails from a dict
view_linked_resource_details_from_dict = ViewLinkedResourceDetails.from_dict(view_linked_resource_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


