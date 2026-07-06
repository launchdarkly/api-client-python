# WarehouseDestinationSetupScriptRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script** | **str** | The SQL setup script to run in your data warehouse | [optional] 
**public_key** | **str** | The RSA public key (Snowflake only) to store as the destination public_key | [optional] 
**public_key_pkcs8** | **str** | The PKCS8 RSA public key (Snowflake only) | [optional] 
**redshift_iam_permissions_policy** | **str** | For Redshift, present only when clusterIdentifier, clusterRegion, and clusterAwsAccountId are supplied in the request body. | [optional] 
**redshift_iam_trust_policy** | **str** | For Redshift, present only when clusterIdentifier, clusterRegion, and clusterAwsAccountId are supplied in the request body. | [optional] 
**s3_bucket_name** | **str** | The auto-generated S3 staging bucket name (ClickHouse and Redshift) | [optional] 

## Example

```python
from launchdarkly_api.models.warehouse_destination_setup_script_rep import WarehouseDestinationSetupScriptRep

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseDestinationSetupScriptRep from a JSON string
warehouse_destination_setup_script_rep_instance = WarehouseDestinationSetupScriptRep.from_json(json)
# print the JSON string representation of the object
print(WarehouseDestinationSetupScriptRep.to_json())

# convert the object into a dict
warehouse_destination_setup_script_rep_dict = warehouse_destination_setup_script_rep_instance.to_dict()
# create an instance of WarehouseDestinationSetupScriptRep from a dict
warehouse_destination_setup_script_rep_from_dict = WarehouseDestinationSetupScriptRep.from_dict(warehouse_destination_setup_script_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


