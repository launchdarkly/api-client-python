# DataExportProjectRankRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_key** | **str** | The canonical project key. | 
**project_name** | **str** | The current project name. | 
**rank** | **int** | The one-based rank within all matching projects. | 
**usage** | **int** | Successful Streaming transfers in the requested range. | 
**components** | [**DataExportProjectRankComponentsRep**](DataExportProjectRankComponentsRep.md) |  | 

## Example

```python
from launchdarkly_api.models.data_export_project_rank_rep import DataExportProjectRankRep

# TODO update the JSON string below
json = "{}"
# create an instance of DataExportProjectRankRep from a JSON string
data_export_project_rank_rep_instance = DataExportProjectRankRep.from_json(json)
# print the JSON string representation of the object
print(DataExportProjectRankRep.to_json())

# convert the object into a dict
data_export_project_rank_rep_dict = data_export_project_rank_rep_instance.to_dict()
# create an instance of DataExportProjectRankRep from a dict
data_export_project_rank_rep_from_dict = DataExportProjectRankRep.from_dict(data_export_project_rank_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


