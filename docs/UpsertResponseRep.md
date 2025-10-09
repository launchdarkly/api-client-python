# UpsertResponseRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the create or update operation | [optional] 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 

## Example

```python
from launchdarkly_api.models.upsert_response_rep import UpsertResponseRep

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertResponseRep from a JSON string
upsert_response_rep_instance = UpsertResponseRep.from_json(json)
# print the JSON string representation of the object
print(UpsertResponseRep.to_json())

# convert the object into a dict
upsert_response_rep_dict = upsert_response_rep_instance.to_dict()
# create an instance of UpsertResponseRep from a dict
upsert_response_rep_from_dict = UpsertResponseRep.from_dict(upsert_response_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


