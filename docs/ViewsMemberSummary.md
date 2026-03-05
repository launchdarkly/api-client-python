# ViewsMemberSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, ViewsLink]**](ViewsLink.md) | The location and content type of related resources | 
**id** | **str** | The member&#39;s ID | 
**first_name** | **str** | The member&#39;s first name | [optional] 
**last_name** | **str** | The member&#39;s last name | [optional] 
**role** | **str** | The member&#39;s base role. If the member has no additional roles, this role will be in effect. | 
**email** | **str** | The member&#39;s email address | 

## Example

```python
from launchdarkly_api.models.views_member_summary import ViewsMemberSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ViewsMemberSummary from a JSON string
views_member_summary_instance = ViewsMemberSummary.from_json(json)
# print the JSON string representation of the object
print(ViewsMemberSummary.to_json())

# convert the object into a dict
views_member_summary_dict = views_member_summary_instance.to_dict()
# create an instance of ViewsMemberSummary from a dict
views_member_summary_from_dict = ViewsMemberSummary.from_dict(views_member_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


