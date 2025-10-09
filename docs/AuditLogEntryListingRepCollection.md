# AuditLogEntryListingRepCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AuditLogEntryListingRep]**](AuditLogEntryListingRep.md) | An array of audit log entries | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 

## Example

```python
from launchdarkly_api.models.audit_log_entry_listing_rep_collection import AuditLogEntryListingRepCollection

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogEntryListingRepCollection from a JSON string
audit_log_entry_listing_rep_collection_instance = AuditLogEntryListingRepCollection.from_json(json)
# print the JSON string representation of the object
print(AuditLogEntryListingRepCollection.to_json())

# convert the object into a dict
audit_log_entry_listing_rep_collection_dict = audit_log_entry_listing_rep_collection_instance.to_dict()
# create an instance of AuditLogEntryListingRepCollection from a dict
audit_log_entry_listing_rep_collection_from_dict = AuditLogEntryListingRepCollection.from_dict(audit_log_entry_listing_rep_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


