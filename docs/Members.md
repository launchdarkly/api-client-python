# Members


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Member]**](Member.md) | An array of members | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**total_count** | **int** | The number of members returned | [optional] 

## Example

```python
from launchdarkly_api.models.members import Members

# TODO update the JSON string below
json = "{}"
# create an instance of Members from a JSON string
members_instance = Members.from_json(json)
# print the JSON string representation of the object
print(Members.to_json())

# convert the object into a dict
members_dict = members_instance.to_dict()
# create an instance of Members from a dict
members_from_dict = Members.from_dict(members_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


