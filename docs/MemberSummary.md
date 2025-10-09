# MemberSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**id** | **str** | The member&#39;s ID | 
**first_name** | **str** | The member&#39;s first name | [optional] 
**last_name** | **str** | The member&#39;s last name | [optional] 
**role** | **str** | The member&#39;s base role. If the member has no additional roles, this role will be in effect. | 
**email** | **str** | The member&#39;s email address | 

## Example

```python
from launchdarkly_api.models.member_summary import MemberSummary

# TODO update the JSON string below
json = "{}"
# create an instance of MemberSummary from a JSON string
member_summary_instance = MemberSummary.from_json(json)
# print the JSON string representation of the object
print(MemberSummary.to_json())

# convert the object into a dict
member_summary_dict = member_summary_instance.to_dict()
# create an instance of MemberSummary from a dict
member_summary_from_dict = MemberSummary.from_dict(member_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


