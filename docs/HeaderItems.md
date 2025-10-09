# HeaderItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.header_items import HeaderItems

# TODO update the JSON string below
json = "{}"
# create an instance of HeaderItems from a JSON string
header_items_instance = HeaderItems.from_json(json)
# print the JSON string representation of the object
print(HeaderItems.to_json())

# convert the object into a dict
header_items_dict = header_items_instance.to_dict()
# create an instance of HeaderItems from a dict
header_items_from_dict = HeaderItems.from_dict(header_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


