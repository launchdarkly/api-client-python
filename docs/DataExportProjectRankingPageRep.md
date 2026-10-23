# DataExportProjectRankingPageRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The bounded page size requested. | 
**count** | **int** | The number of items on this page. | 
**total_count** | **int** | The number of matching projects with usage. | 
**next_cursor** | **str** | An opaque cursor for the next page. | [optional] 

## Example

```python
from launchdarkly_api.models.data_export_project_ranking_page_rep import DataExportProjectRankingPageRep

# TODO update the JSON string below
json = "{}"
# create an instance of DataExportProjectRankingPageRep from a JSON string
data_export_project_ranking_page_rep_instance = DataExportProjectRankingPageRep.from_json(json)
# print the JSON string representation of the object
print(DataExportProjectRankingPageRep.to_json())

# convert the object into a dict
data_export_project_ranking_page_rep_dict = data_export_project_ranking_page_rep_instance.to_dict()
# create an instance of DataExportProjectRankingPageRep from a dict
data_export_project_ranking_page_rep_from_dict = DataExportProjectRankingPageRep.from_dict(data_export_project_ranking_page_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


