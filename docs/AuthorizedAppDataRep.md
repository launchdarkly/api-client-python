# AuthorizedAppDataRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) |  | [optional] 
**id** | **str** | The ID of the authorized application | [optional] 
**is_scim** | **bool** | Whether the application is authorized through SCIM | [optional] 
**name** | **str** | The authorized application name | [optional] 
**icon_url** | **str** | The icon for this authorized application, if it has one | [optional] 
**maintainer_name** | **str** | The name of the maintainer for this authorized application | [optional] 
**is_agent** | **bool** | Whether this application acted on behalf of the member in this entry. When true, the member and the application are co-authors of the change rather than the member acting alone. Omitted for applications that act on their own. | [optional] 

## Example

```python
from launchdarkly_api.models.authorized_app_data_rep import AuthorizedAppDataRep

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizedAppDataRep from a JSON string
authorized_app_data_rep_instance = AuthorizedAppDataRep.from_json(json)
# print the JSON string representation of the object
print(AuthorizedAppDataRep.to_json())

# convert the object into a dict
authorized_app_data_rep_dict = authorized_app_data_rep_instance.to_dict()
# create an instance of AuthorizedAppDataRep from a dict
authorized_app_data_rep_from_dict = AuthorizedAppDataRep.from_dict(authorized_app_data_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


