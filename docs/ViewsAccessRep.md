# ViewsAccessRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**denied** | [**List[ViewsAccessDenied]**](ViewsAccessDenied.md) |  | 
**allowed** | [**List[ViewsAccessAllowedRep]**](ViewsAccessAllowedRep.md) |  | 

## Example

```python
from launchdarkly_api.models.views_access_rep import ViewsAccessRep

# TODO update the JSON string below
json = "{}"
# create an instance of ViewsAccessRep from a JSON string
views_access_rep_instance = ViewsAccessRep.from_json(json)
# print the JSON string representation of the object
print(ViewsAccessRep.to_json())

# convert the object into a dict
views_access_rep_dict = views_access_rep_instance.to_dict()
# create an instance of ViewsAccessRep from a dict
views_access_rep_from_dict = ViewsAccessRep.from_dict(views_access_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


