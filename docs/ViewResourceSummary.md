# ViewResourceSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flag_count** | **int** | The number of flags associated with the view. | 
**segment_count** | **int** | The number of segments associated with the view. | 

## Example

```python
from launchdarkly_api.models.view_resource_summary import ViewResourceSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ViewResourceSummary from a JSON string
view_resource_summary_instance = ViewResourceSummary.from_json(json)
# print the JSON string representation of the object
print(ViewResourceSummary.to_json())

# convert the object into a dict
view_resource_summary_dict = view_resource_summary_instance.to_dict()
# create an instance of ViewResourceSummary from a dict
view_resource_summary_from_dict = ViewResourceSummary.from_dict(view_resource_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


