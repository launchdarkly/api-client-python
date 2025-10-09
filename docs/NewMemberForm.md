# NewMemberForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The member&#39;s email | 
**password** | **str** | The member&#39;s password | [optional] 
**first_name** | **str** | The member&#39;s first name | [optional] 
**last_name** | **str** | The member&#39;s last name | [optional] 
**role** | **str** | The member&#39;s initial role, if you are using a base role for the initial role | [optional] 
**custom_roles** | **List[str]** | An array of the member&#39;s initial roles, if you are using custom roles or preset roles provided by LaunchDarkly | [optional] 
**team_keys** | **List[str]** | An array of the member&#39;s teams | [optional] 
**role_attributes** | **Dict[str, List[str]]** |  | [optional] 

## Example

```python
from launchdarkly_api.models.new_member_form import NewMemberForm

# TODO update the JSON string below
json = "{}"
# create an instance of NewMemberForm from a JSON string
new_member_form_instance = NewMemberForm.from_json(json)
# print the JSON string representation of the object
print(NewMemberForm.to_json())

# convert the object into a dict
new_member_form_dict = new_member_form_instance.to_dict()
# create an instance of NewMemberForm from a dict
new_member_form_from_dict = NewMemberForm.from_dict(new_member_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


