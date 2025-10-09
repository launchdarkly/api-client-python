# AuditLogEntryRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**id** | **str** | The ID of the audit log entry | 
**account_id** | **str** | The ID of the account to which this audit log entry belongs | 
**var_date** | **int** |  | 
**accesses** | [**List[ResourceAccess]**](ResourceAccess.md) | Details on the actions performed and resources acted on in this audit log entry | 
**kind** | **str** |  | 
**name** | **str** | The name of the resource this audit log entry refers to | 
**description** | **str** | Description of the change recorded in the audit log entry | 
**short_description** | **str** | Shorter version of the change recorded in the audit log entry | 
**comment** | **str** | Optional comment for the audit log entry | [optional] 
**subject** | [**SubjectDataRep**](SubjectDataRep.md) |  | [optional] 
**member** | [**MemberDataRep**](MemberDataRep.md) |  | [optional] 
**token** | [**TokenSummary**](TokenSummary.md) |  | [optional] 
**app** | [**AuthorizedAppDataRep**](AuthorizedAppDataRep.md) |  | [optional] 
**title_verb** | **str** | The action and resource recorded in this audit log entry | [optional] 
**title** | **str** | A description of what occurred, in the format &lt;code&gt;member&lt;/code&gt; &lt;code&gt;titleVerb&lt;/code&gt; &lt;code&gt;target&lt;/code&gt; | [optional] 
**target** | [**TargetResourceRep**](TargetResourceRep.md) |  | [optional] 
**parent** | [**ParentResourceRep**](ParentResourceRep.md) |  | [optional] 
**delta** | **object** | If the audit log entry has been updated, this is the JSON patch body that was used in the request to update the entity | [optional] 
**trigger_body** | **object** | A JSON representation of the external trigger for this audit log entry, if any | [optional] 
**merge** | **object** | A JSON representation of the merge information for this audit log entry, if any | [optional] 
**previous_version** | **object** | If the audit log entry has been updated, this is a JSON representation of the previous version of the entity | [optional] 
**current_version** | **object** | If the audit log entry has been updated, this is a JSON representation of the current version of the entity | [optional] 
**subentries** | [**List[AuditLogEntryListingRep]**](AuditLogEntryListingRep.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.audit_log_entry_rep import AuditLogEntryRep

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogEntryRep from a JSON string
audit_log_entry_rep_instance = AuditLogEntryRep.from_json(json)
# print the JSON string representation of the object
print(AuditLogEntryRep.to_json())

# convert the object into a dict
audit_log_entry_rep_dict = audit_log_entry_rep_instance.to_dict()
# create an instance of AuditLogEntryRep from a dict
audit_log_entry_rep_from_dict = AuditLogEntryRep.from_dict(audit_log_entry_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


