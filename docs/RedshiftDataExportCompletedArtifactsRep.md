# RedshiftDataExportCompletedArtifactsRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sql_setup_script** | **str** | The SQL setup script originally run against the Redshift cluster, rehydrated from the destination&#39;s persisted custom names. | [optional] 
**s3_bucket_name** | **str** | The auto-generated S3 staging bucket name. | [optional] 

## Example

```python
from launchdarkly_api.models.redshift_data_export_completed_artifacts_rep import RedshiftDataExportCompletedArtifactsRep

# TODO update the JSON string below
json = "{}"
# create an instance of RedshiftDataExportCompletedArtifactsRep from a JSON string
redshift_data_export_completed_artifacts_rep_instance = RedshiftDataExportCompletedArtifactsRep.from_json(json)
# print the JSON string representation of the object
print(RedshiftDataExportCompletedArtifactsRep.to_json())

# convert the object into a dict
redshift_data_export_completed_artifacts_rep_dict = redshift_data_export_completed_artifacts_rep_instance.to_dict()
# create an instance of RedshiftDataExportCompletedArtifactsRep from a dict
redshift_data_export_completed_artifacts_rep_from_dict = RedshiftDataExportCompletedArtifactsRep.from_dict(redshift_data_export_completed_artifacts_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


