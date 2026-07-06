# ViewSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ParentAndSelfLinks**](ParentAndSelfLinks.md) |  | [optional] 
**key** | **str** | The key of the view. | 
**name** | **str** | The human-readable name of the view. | 
**resource_summary** | [**ViewResourceSummary**](ViewResourceSummary.md) |  | 

## Example

```python
from launchdarkly_api.models.view_summary import ViewSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ViewSummary from a JSON string
view_summary_instance = ViewSummary.from_json(json)
# print the JSON string representation of the object
print(ViewSummary.to_json())

# convert the object into a dict
view_summary_dict = view_summary_instance.to_dict()
# create an instance of ViewSummary from a dict
view_summary_from_dict = ViewSummary.from_dict(view_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


