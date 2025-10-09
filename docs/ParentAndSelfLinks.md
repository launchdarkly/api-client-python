# ParentAndSelfLinks

The location and content type of related resources

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**CoreLink**](CoreLink.md) |  | 
**parent** | [**CoreLink**](CoreLink.md) |  | 

## Example

```python
from launchdarkly_api.models.parent_and_self_links import ParentAndSelfLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ParentAndSelfLinks from a JSON string
parent_and_self_links_instance = ParentAndSelfLinks.from_json(json)
# print the JSON string representation of the object
print(ParentAndSelfLinks.to_json())

# convert the object into a dict
parent_and_self_links_dict = parent_and_self_links_instance.to_dict()
# create an instance of ParentAndSelfLinks from a dict
parent_and_self_links_from_dict = ParentAndSelfLinks.from_dict(parent_and_self_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


