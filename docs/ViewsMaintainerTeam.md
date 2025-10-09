# ViewsMaintainerTeam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**key** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from launchdarkly_api.models.views_maintainer_team import ViewsMaintainerTeam

# TODO update the JSON string below
json = "{}"
# create an instance of ViewsMaintainerTeam from a JSON string
views_maintainer_team_instance = ViewsMaintainerTeam.from_json(json)
# print the JSON string representation of the object
print(ViewsMaintainerTeam.to_json())

# convert the object into a dict
views_maintainer_team_dict = views_maintainer_team_instance.to_dict()
# create an instance of ViewsMaintainerTeam from a dict
views_maintainer_team_from_dict = ViewsMaintainerTeam.from_dict(views_maintainer_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


