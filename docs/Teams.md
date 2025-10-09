# Teams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Team]**](Team.md) | An array of teams | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 
**total_count** | **int** | The number of teams | [optional] 

## Example

```python
from launchdarkly_api.models.teams import Teams

# TODO update the JSON string below
json = "{}"
# create an instance of Teams from a JSON string
teams_instance = Teams.from_json(json)
# print the JSON string representation of the object
print(Teams.to_json())

# convert the object into a dict
teams_dict = teams_instance.to_dict()
# create an instance of Teams from a dict
teams_from_dict = Teams.from_dict(teams_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


