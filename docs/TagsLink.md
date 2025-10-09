# TagsLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.tags_link import TagsLink

# TODO update the JSON string below
json = "{}"
# create an instance of TagsLink from a JSON string
tags_link_instance = TagsLink.from_json(json)
# print the JSON string representation of the object
print(TagsLink.to_json())

# convert the object into a dict
tags_link_dict = tags_link_instance.to_dict()
# create an instance of TagsLink from a dict
tags_link_from_dict = TagsLink.from_dict(tags_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


