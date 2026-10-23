# DataExportProjectRankingScopeRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | The included usage source. | 
**dimension** | **str** | The ranked dimension. | 
**var_from** | **int** | Inclusive UTC range start in Unix milliseconds. | 
**to** | **int** | Exclusive UTC range end in Unix milliseconds. | 

## Example

```python
from launchdarkly_api.models.data_export_project_ranking_scope_rep import DataExportProjectRankingScopeRep

# TODO update the JSON string below
json = "{}"
# create an instance of DataExportProjectRankingScopeRep from a JSON string
data_export_project_ranking_scope_rep_instance = DataExportProjectRankingScopeRep.from_json(json)
# print the JSON string representation of the object
print(DataExportProjectRankingScopeRep.to_json())

# convert the object into a dict
data_export_project_ranking_scope_rep_dict = data_export_project_ranking_scope_rep_instance.to_dict()
# create an instance of DataExportProjectRankingScopeRep from a dict
data_export_project_ranking_scope_rep_from_dict = DataExportProjectRankingScopeRep.from_dict(data_export_project_ranking_scope_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


