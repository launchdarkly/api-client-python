# Export


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The export ID | 
**segment_key** | **str** | The segment key | 
**creation_time** | **int** |  | 
**status** | **str** | The export status | 
**size_bytes** | **int** | The export size, in bytes | 
**size** | **str** | The export size, with units | 
**initiator** | [**InitiatorRep**](InitiatorRep.md) |  | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources, including the location of the exported file | 

## Example

```python
from launchdarkly_api.models.export import Export

# TODO update the JSON string below
json = "{}"
# create an instance of Export from a JSON string
export_instance = Export.from_json(json)
# print the JSON string representation of the object
print(Export.to_json())

# convert the object into a dict
export_dict = export_instance.to_dict()
# create an instance of Export from a dict
export_from_dict = Export.from_dict(export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


