# DataExportProjectRankingRep

A bounded Streaming project ranking.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DataExportProjectRankRep]**](DataExportProjectRankRep.md) | Projects in deterministic rank order. | 
**page** | [**DataExportProjectRankingPageRep**](DataExportProjectRankingPageRep.md) |  | 
**scope** | [**DataExportProjectRankingScopeRep**](DataExportProjectRankingScopeRep.md) |  | 

## Example

```python
from launchdarkly_api.models.data_export_project_ranking_rep import DataExportProjectRankingRep

# TODO update the JSON string below
json = "{}"
# create an instance of DataExportProjectRankingRep from a JSON string
data_export_project_ranking_rep_instance = DataExportProjectRankingRep.from_json(json)
# print the JSON string representation of the object
print(DataExportProjectRankingRep.to_json())

# convert the object into a dict
data_export_project_ranking_rep_dict = data_export_project_ranking_rep_instance.to_dict()
# create an instance of DataExportProjectRankingRep from a dict
data_export_project_ranking_rep_from_dict = DataExportProjectRankingRep.from_dict(data_export_project_ranking_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


