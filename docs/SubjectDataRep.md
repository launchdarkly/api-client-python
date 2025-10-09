# SubjectDataRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) |  | [optional] 
**name** | **str** | The subject&#39;s name | [optional] 
**avatar_url** | **str** | The subject&#39;s avatar | [optional] 

## Example

```python
from launchdarkly_api.models.subject_data_rep import SubjectDataRep

# TODO update the JSON string below
json = "{}"
# create an instance of SubjectDataRep from a JSON string
subject_data_rep_instance = SubjectDataRep.from_json(json)
# print the JSON string representation of the object
print(SubjectDataRep.to_json())

# convert the object into a dict
subject_data_rep_dict = subject_data_rep_instance.to_dict()
# create an instance of SubjectDataRep from a dict
subject_data_rep_from_dict = SubjectDataRep.from_dict(subject_data_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


