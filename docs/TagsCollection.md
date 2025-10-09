# TagsCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **List[str]** | List of tags | 
**links** | [**Dict[str, TagsLink]**](TagsLink.md) |  | 
**total_count** | **int** | The total number of tags | [optional] 

## Example

```python
from launchdarkly_api.models.tags_collection import TagsCollection

# TODO update the JSON string below
json = "{}"
# create an instance of TagsCollection from a JSON string
tags_collection_instance = TagsCollection.from_json(json)
# print the JSON string representation of the object
print(TagsCollection.to_json())

# convert the object into a dict
tags_collection_dict = tags_collection_instance.to_dict()
# create an instance of TagsCollection from a dict
tags_collection_from_dict = TagsCollection.from_dict(tags_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


