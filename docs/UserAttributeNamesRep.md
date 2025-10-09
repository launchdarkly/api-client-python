# UserAttributeNamesRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private** | **List[str]** | private attributes | [optional] 
**custom** | **List[str]** | custom attributes | [optional] 
**standard** | **List[str]** | standard attributes | [optional] 

## Example

```python
from launchdarkly_api.models.user_attribute_names_rep import UserAttributeNamesRep

# TODO update the JSON string below
json = "{}"
# create an instance of UserAttributeNamesRep from a JSON string
user_attribute_names_rep_instance = UserAttributeNamesRep.from_json(json)
# print the JSON string representation of the object
print(UserAttributeNamesRep.to_json())

# convert the object into a dict
user_attribute_names_rep_dict = user_attribute_names_rep_instance.to_dict()
# create an instance of UserAttributeNamesRep from a dict
user_attribute_names_rep_from_dict = UserAttributeNamesRep.from_dict(user_attribute_names_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


