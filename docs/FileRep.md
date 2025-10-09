# FileRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | The imported file name, including the extension | [optional] 
**status** | **str** | The imported file status | [optional] 

## Example

```python
from launchdarkly_api.models.file_rep import FileRep

# TODO update the JSON string below
json = "{}"
# create an instance of FileRep from a JSON string
file_rep_instance = FileRep.from_json(json)
# print the JSON string representation of the object
print(FileRep.to_json())

# convert the object into a dict
file_rep_dict = file_rep_instance.to_dict()
# create an instance of FileRep from a dict
file_rep_from_dict = FileRep.from_dict(file_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


