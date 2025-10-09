# StatisticRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The repository name | 
**type** | **str** | The type of repository | 
**source_link** | **str** | A URL to access the repository | 
**default_branch** | **str** | The repository&#39;s default branch | 
**enabled** | **bool** | Whether or not a repository is enabled for code reference scanning | 
**version** | **int** | The version of the repository&#39;s saved information | 
**hunk_count** | **int** | The number of code reference hunks in which the flag appears in this repository | 
**file_count** | **int** | The number of files in which the flag appears in this repository | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**latest_commit_time** | **int** |  | [optional] 

## Example

```python
from launchdarkly_api.models.statistic_rep import StatisticRep

# TODO update the JSON string below
json = "{}"
# create an instance of StatisticRep from a JSON string
statistic_rep_instance = StatisticRep.from_json(json)
# print the JSON string representation of the object
print(StatisticRep.to_json())

# convert the object into a dict
statistic_rep_dict = statistic_rep_instance.to_dict()
# create an instance of StatisticRep from a dict
statistic_rep_from_dict = StatisticRep.from_dict(statistic_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


