# ExpandedDirectlyLinkedFlag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**name** | **str** |  | 
**links** | [**ViewsSelfLink**](ViewsSelfLink.md) |  | 

## Example

```python
from launchdarkly_api.models.expanded_directly_linked_flag import ExpandedDirectlyLinkedFlag

# TODO update the JSON string below
json = "{}"
# create an instance of ExpandedDirectlyLinkedFlag from a JSON string
expanded_directly_linked_flag_instance = ExpandedDirectlyLinkedFlag.from_json(json)
# print the JSON string representation of the object
print(ExpandedDirectlyLinkedFlag.to_json())

# convert the object into a dict
expanded_directly_linked_flag_dict = expanded_directly_linked_flag_instance.to_dict()
# create an instance of ExpandedDirectlyLinkedFlag from a dict
expanded_directly_linked_flag_from_dict = ExpandedDirectlyLinkedFlag.from_dict(expanded_directly_linked_flag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


