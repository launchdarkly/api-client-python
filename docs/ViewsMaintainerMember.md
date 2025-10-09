# ViewsMaintainerMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**email** | **str** |  | 
**role** | **str** |  | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.views_maintainer_member import ViewsMaintainerMember

# TODO update the JSON string below
json = "{}"
# create an instance of ViewsMaintainerMember from a JSON string
views_maintainer_member_instance = ViewsMaintainerMember.from_json(json)
# print the JSON string representation of the object
print(ViewsMaintainerMember.to_json())

# convert the object into a dict
views_maintainer_member_dict = views_maintainer_member_instance.to_dict()
# create an instance of ViewsMaintainerMember from a dict
views_maintainer_member_from_dict = ViewsMaintainerMember.from_dict(views_maintainer_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


