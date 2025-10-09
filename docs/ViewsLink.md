# ViewsLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.views_link import ViewsLink

# TODO update the JSON string below
json = "{}"
# create an instance of ViewsLink from a JSON string
views_link_instance = ViewsLink.from_json(json)
# print the JSON string representation of the object
print(ViewsLink.to_json())

# convert the object into a dict
views_link_dict = views_link_instance.to_dict()
# create an instance of ViewsLink from a dict
views_link_from_dict = ViewsLink.from_dict(views_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


