# ApplicationMaintainerRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | [**MemberSummary**](MemberSummary.md) |  | [optional] 
**team** | [**MemberTeamSummaryRep**](MemberTeamSummaryRep.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.application_maintainer_rep import ApplicationMaintainerRep

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationMaintainerRep from a JSON string
application_maintainer_rep_instance = ApplicationMaintainerRep.from_json(json)
# print the JSON string representation of the object
print(ApplicationMaintainerRep.to_json())

# convert the object into a dict
application_maintainer_rep_dict = application_maintainer_rep_instance.to_dict()
# create an instance of ApplicationMaintainerRep from a dict
application_maintainer_rep_from_dict = ApplicationMaintainerRep.from_dict(application_maintainer_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


