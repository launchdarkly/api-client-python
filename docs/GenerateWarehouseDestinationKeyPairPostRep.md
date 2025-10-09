# GenerateWarehouseDestinationKeyPairPostRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_key** | **str** | The public key used by LaunchDarkly | [optional] 
**public_key_pkcs8** | **str** | The public key to assign in your Snowflake worksheet | [optional] 

## Example

```python
from launchdarkly_api.models.generate_warehouse_destination_key_pair_post_rep import GenerateWarehouseDestinationKeyPairPostRep

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateWarehouseDestinationKeyPairPostRep from a JSON string
generate_warehouse_destination_key_pair_post_rep_instance = GenerateWarehouseDestinationKeyPairPostRep.from_json(json)
# print the JSON string representation of the object
print(GenerateWarehouseDestinationKeyPairPostRep.to_json())

# convert the object into a dict
generate_warehouse_destination_key_pair_post_rep_dict = generate_warehouse_destination_key_pair_post_rep_instance.to_dict()
# create an instance of GenerateWarehouseDestinationKeyPairPostRep from a dict
generate_warehouse_destination_key_pair_post_rep_from_dict = GenerateWarehouseDestinationKeyPairPostRep.from_dict(generate_warehouse_destination_key_pair_post_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


