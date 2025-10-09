# ContextKindRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The context kind key | 
**name** | **str** | The context kind name | 
**description** | **str** | The context kind description | 
**version** | **int** | The context kind version | 
**creation_date** | **int** |  | 
**last_modified** | **int** |  | 
**last_seen** | **int** |  | [optional] 
**created_from** | **str** |  | 
**hide_in_targeting** | **bool** | Alias for archived. | [optional] 
**archived** | **bool** | Whether the context kind is archived. Archived context kinds are unavailable for targeting. | [optional] 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 

## Example

```python
from launchdarkly_api.models.context_kind_rep import ContextKindRep

# TODO update the JSON string below
json = "{}"
# create an instance of ContextKindRep from a JSON string
context_kind_rep_instance = ContextKindRep.from_json(json)
# print the JSON string representation of the object
print(ContextKindRep.to_json())

# convert the object into a dict
context_kind_rep_dict = context_kind_rep_instance.to_dict()
# create an instance of ContextKindRep from a dict
context_kind_rep_from_dict = ContextKindRep.from_dict(context_kind_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


