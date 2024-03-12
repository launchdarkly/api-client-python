# DeploymentRep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The deployment ID | 
**application_key** | **str** | The application key | 
**application_version** | **str** | The application version | 
**started_at** | **int** |  | 
**status** | **str** |  | 
**kind** | **str** |  | 
**active** | **bool** | Whether the deployment is active | 
**archived** | **bool** | Whether the deployment is archived | 
**environment_key** | **str** | The environment key | 
**number_of_contributors** | **int** | The number of contributors | 
**number_of_pull_requests** | **int** | The number of pull requests | 
**lines_added** | **int** | The number of lines added | 
**lines_deleted** | **int** | The number of lines deleted | 
**lead_time** | **int** | The total lead time from first commit to deployment end in milliseconds | 
**ended_at** | **int** |  | [optional] 
**duration_ms** | **int** | The duration of the deployment in milliseconds | [optional] 
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The metadata associated with the deployment | [optional] 
**pull_requests** | [**PullRequestCollectionRep**](PullRequestCollectionRep.md) |  | [optional] 
**flag_references** | [**FlagReferenceCollectionRep**](FlagReferenceCollectionRep.md) |  | [optional] 
**lead_time_stages** | [**LeadTimeStagesRep**](LeadTimeStagesRep.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


