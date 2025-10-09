# UpsertContextKindPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The context kind name | 
**description** | **str** | The context kind description | [optional] 
**hide_in_targeting** | **bool** | Alias for archived. | [optional] 
**archived** | **bool** | Whether the context kind is archived. Archived context kinds are unavailable for targeting. | [optional] 
**version** | **int** | The context kind version. If not specified when the context kind is created, defaults to 1. | [optional] 

## Example

```python
from launchdarkly_api.models.upsert_context_kind_payload import UpsertContextKindPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertContextKindPayload from a JSON string
upsert_context_kind_payload_instance = UpsertContextKindPayload.from_json(json)
# print the JSON string representation of the object
print(UpsertContextKindPayload.to_json())

# convert the object into a dict
upsert_context_kind_payload_dict = upsert_context_kind_payload_instance.to_dict()
# create an instance of UpsertContextKindPayload from a dict
upsert_context_kind_payload_from_dict = UpsertContextKindPayload.from_dict(upsert_context_kind_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


