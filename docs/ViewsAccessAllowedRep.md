# ViewsAccessAllowedRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**reason** | [**ViewsAccessAllowedReason**](ViewsAccessAllowedReason.md) |  | 

## Example

```python
from launchdarkly_api.models.views_access_allowed_rep import ViewsAccessAllowedRep

# TODO update the JSON string below
json = "{}"
# create an instance of ViewsAccessAllowedRep from a JSON string
views_access_allowed_rep_instance = ViewsAccessAllowedRep.from_json(json)
# print the JSON string representation of the object
print(ViewsAccessAllowedRep.to_json())

# convert the object into a dict
views_access_allowed_rep_dict = views_access_allowed_rep_instance.to_dict()
# create an instance of ViewsAccessAllowedRep from a dict
views_access_allowed_rep_from_dict = ViewsAccessAllowedRep.from_dict(views_access_allowed_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


