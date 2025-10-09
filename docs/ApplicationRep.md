# ApplicationRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flags** | [**ApplicationFlagCollectionRep**](ApplicationFlagCollectionRep.md) |  | [optional] 
**access** | [**Access**](Access.md) |  | [optional] 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 
**version** | **int** | Version of the application | [optional] 
**auto_added** | **bool** | Whether the application was automatically created because it was included in a context when a LaunchDarkly SDK evaluated a feature flag, or was created through the LaunchDarkly UI or REST API. | 
**creation_date** | **int** |  | [optional] 
**description** | **str** | The application description | [optional] 
**key** | **str** | The unique identifier of this application | 
**kind** | **str** | To distinguish the kind of application | 
**maintainer** | [**MaintainerRep**](MaintainerRep.md) |  | [optional] 
**name** | **str** | The name of the application | 

## Example

```python
from launchdarkly_api.models.application_rep import ApplicationRep

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationRep from a JSON string
application_rep_instance = ApplicationRep.from_json(json)
# print the JSON string representation of the object
print(ApplicationRep.to_json())

# convert the object into a dict
application_rep_dict = application_rep_instance.to_dict()
# create an instance of ApplicationRep from a dict
application_rep_from_dict = ApplicationRep.from_dict(application_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


