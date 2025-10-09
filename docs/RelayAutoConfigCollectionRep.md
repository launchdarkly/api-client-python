# RelayAutoConfigCollectionRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[RelayAutoConfigRep]**](RelayAutoConfigRep.md) | An array of Relay Proxy configurations | 

## Example

```python
from launchdarkly_api.models.relay_auto_config_collection_rep import RelayAutoConfigCollectionRep

# TODO update the JSON string below
json = "{}"
# create an instance of RelayAutoConfigCollectionRep from a JSON string
relay_auto_config_collection_rep_instance = RelayAutoConfigCollectionRep.from_json(json)
# print the JSON string representation of the object
print(RelayAutoConfigCollectionRep.to_json())

# convert the object into a dict
relay_auto_config_collection_rep_dict = relay_auto_config_collection_rep_instance.to_dict()
# create an instance of RelayAutoConfigCollectionRep from a dict
relay_auto_config_collection_rep_from_dict = RelayAutoConfigCollectionRep.from_dict(relay_auto_config_collection_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


