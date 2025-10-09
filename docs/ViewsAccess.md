# ViewsAccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**denied** | [**List[ViewsAccessDenied]**](ViewsAccessDenied.md) |  | 
**allowed** | [**List[ViewsAccessAllowedRep]**](ViewsAccessAllowedRep.md) |  | 

## Example

```python
from launchdarkly_api.models.views_access import ViewsAccess

# TODO update the JSON string below
json = "{}"
# create an instance of ViewsAccess from a JSON string
views_access_instance = ViewsAccess.from_json(json)
# print the JSON string representation of the object
print(ViewsAccess.to_json())

# convert the object into a dict
views_access_dict = views_access_instance.to_dict()
# create an instance of ViewsAccess from a dict
views_access_from_dict = ViewsAccess.from_dict(views_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


