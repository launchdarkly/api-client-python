# WarehouseSetupScriptPostBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**snowflake_host_address** | **str** |  | [optional] 
**database_name** | **str** |  | [optional] 
**warehouse_name** | **str** |  | [optional] 
**role_name** | **str** |  | [optional] 
**schema_name** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 
**include_network_policy** | **bool** |  | [optional] 
**cluster_identifier** | **str** |  | [optional] 
**cluster_region** | **str** |  | [optional] 
**cluster_aws_account_id** | **str** |  | [optional] 
**endpoint** | **str** |  | [optional] 
**click_house_database_name** | **str** |  | [optional] 
**click_house_user_name** | **str** |  | [optional] 
**click_house_s3_bucket_name** | **str** |  | [optional] 
**click_house_include_host_restriction** | **bool** |  | [optional] 
**click_house_service_role_arn** | **str** |  | [optional] 
**click_house_password** | **str** |  | [optional] 
**s3_bucket_name** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.warehouse_setup_script_post_body import WarehouseSetupScriptPostBody

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseSetupScriptPostBody from a JSON string
warehouse_setup_script_post_body_instance = WarehouseSetupScriptPostBody.from_json(json)
# print the JSON string representation of the object
print(WarehouseSetupScriptPostBody.to_json())

# convert the object into a dict
warehouse_setup_script_post_body_dict = warehouse_setup_script_post_body_instance.to_dict()
# create an instance of WarehouseSetupScriptPostBody from a dict
warehouse_setup_script_post_body_from_dict = WarehouseSetupScriptPostBody.from_dict(warehouse_setup_script_post_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


