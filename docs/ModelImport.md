# ModelImport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The import ID | 
**segment_key** | **str** | The segment key | 
**creation_time** | **int** |  | 
**mode** | **str** | The import mode used, either &lt;code&gt;merge&lt;/code&gt; or &lt;code&gt;replace&lt;/code&gt; | 
**status** | **str** | The import status | 
**files** | [**List[FileRep]**](FileRep.md) | The imported files and their status | [optional] 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 

## Example

```python
from launchdarkly_api.models.model_import import ModelImport

# TODO update the JSON string below
json = "{}"
# create an instance of ModelImport from a JSON string
model_import_instance = ModelImport.from_json(json)
# print the JSON string representation of the object
print(ModelImport.to_json())

# convert the object into a dict
model_import_dict = model_import_instance.to_dict()
# create an instance of ModelImport from a dict
model_import_from_dict = ModelImport.from_dict(model_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


