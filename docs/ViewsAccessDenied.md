# ViewsAccessDenied


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**reason** | [**ViewsAccessDeniedReason**](ViewsAccessDeniedReason.md) |  | 

## Example

```python
from launchdarkly_api.models.views_access_denied import ViewsAccessDenied

# TODO update the JSON string below
json = "{}"
# create an instance of ViewsAccessDenied from a JSON string
views_access_denied_instance = ViewsAccessDenied.from_json(json)
# print the JSON string representation of the object
print(ViewsAccessDenied.to_json())

# convert the object into a dict
views_access_denied_dict = views_access_denied_instance.to_dict()
# create an instance of ViewsAccessDenied from a dict
views_access_denied_from_dict = ViewsAccessDenied.from_dict(views_access_denied_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


