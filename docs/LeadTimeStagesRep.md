# LeadTimeStagesRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coding_duration_ms** | **int** | The coding duration in milliseconds | 
**review_duration_ms** | **int** | The review duration in milliseconds | [optional] 
**wait_duration_ms** | **int** | The wait duration between merge time and deploy start time in milliseconds | [optional] 
**deploy_duration_ms** | **int** | The deploy duration in milliseconds | [optional] 
**total_lead_time_ms** | **int** | The total lead time in milliseconds | [optional] 

## Example

```python
from launchdarkly_api.models.lead_time_stages_rep import LeadTimeStagesRep

# TODO update the JSON string below
json = "{}"
# create an instance of LeadTimeStagesRep from a JSON string
lead_time_stages_rep_instance = LeadTimeStagesRep.from_json(json)
# print the JSON string representation of the object
print(LeadTimeStagesRep.to_json())

# convert the object into a dict
lead_time_stages_rep_dict = lead_time_stages_rep_instance.to_dict()
# create an instance of LeadTimeStagesRep from a dict
lead_time_stages_rep_from_dict = LeadTimeStagesRep.from_dict(lead_time_stages_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


