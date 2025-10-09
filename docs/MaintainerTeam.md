# MaintainerTeam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the maintainer team | 
**name** | **str** | A human-friendly name for the maintainer team | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 

## Example

```python
from launchdarkly_api.models.maintainer_team import MaintainerTeam

# TODO update the JSON string below
json = "{}"
# create an instance of MaintainerTeam from a JSON string
maintainer_team_instance = MaintainerTeam.from_json(json)
# print the JSON string representation of the object
print(MaintainerTeam.to_json())

# convert the object into a dict
maintainer_team_dict = maintainer_team_instance.to_dict()
# create an instance of MaintainerTeam from a dict
maintainer_team_from_dict = MaintainerTeam.from_dict(maintainer_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


