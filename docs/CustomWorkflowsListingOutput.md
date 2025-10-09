# CustomWorkflowsListingOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CustomWorkflowOutput]**](CustomWorkflowOutput.md) | An array of workflows | 
**total_count** | **int** | Total number of workflows | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 

## Example

```python
from launchdarkly_api.models.custom_workflows_listing_output import CustomWorkflowsListingOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CustomWorkflowsListingOutput from a JSON string
custom_workflows_listing_output_instance = CustomWorkflowsListingOutput.from_json(json)
# print the JSON string representation of the object
print(CustomWorkflowsListingOutput.to_json())

# convert the object into a dict
custom_workflows_listing_output_dict = custom_workflows_listing_output_instance.to_dict()
# create an instance of CustomWorkflowsListingOutput from a dict
custom_workflows_listing_output_from_dict = CustomWorkflowsListingOutput.from_dict(custom_workflows_listing_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


