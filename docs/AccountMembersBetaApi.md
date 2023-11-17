# launchdarkly_api.AccountMembersBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**patch_members**](AccountMembersBetaApi.md#patch_members) | **PATCH** /api/v2/members | Modify account members


# **patch_members**
> BulkEditMembersRep patch_members(members_patch_input)

Modify account members

Perform a partial update to multiple members. Updating members uses the semantic patch format.  To make a semantic patch request, you must append `domain-model=launchdarkly.semanticpatch` to your `Content-Type` header. To learn more, read [Updates using semantic patch](/reference#updates-using-semantic-patch).  ### Instructions  Semantic patch requests support the following `kind` instructions for updating members.  <details> <summary>Click to expand instructions for <strong>updating members</strong></summary>  #### replaceMembersRoles  Replaces the roles of the specified members. This also removes all custom roles assigned to the specified members.  ##### Parameters  - `value`: The new role. Must be a valid built-in role. To learn more about built-in roles, read [LaunchDarkly's built-in roles](https://docs.launchdarkly.com/home/members/built-in-roles). - `memberIDs`: List of member IDs.  Here's an example:  ```json {   \"instructions\": [{     \"kind\": \"replaceMemberRoles\",     \"value\": \"reader\",     \"memberIDs\": [       \"1234a56b7c89d012345e678f\",       \"507f1f77bcf86cd799439011\"     ]   }] } ```  #### replaceAllMembersRoles  Replaces the roles of all members. This also removes all custom roles assigned to the specified members.  Members that match any of the filters are **excluded** from the update.  ##### Parameters  - `value`: The new role. Must be a valid built-in role. To learn more about built-in roles, read [LaunchDarkly's built-in roles](https://docs.launchdarkly.com/home/members/built-in-roles). - `filterLastSeen`: (Optional) A JSON object with one of the following formats:   - `{\"never\": true}` - Members that have never been active, such as those who have not accepted their invitation to LaunchDarkly, or have not logged in after being provisioned via SCIM.   - `{\"noData\": true}` - Members that have not been active since LaunchDarkly began recording last seen timestamps.   - `{\"before\": 1608672063611}` - Members that have not been active since the provided value, which should be a timestamp in Unix epoch milliseconds. - `filterQuery`: (Optional) A string that matches against the members' emails and names. It is not case sensitive. - `filterRoles`: (Optional) A `|` separated list of roles and custom roles. For the purposes of this filtering, `Owner` counts as `Admin`. - `filterTeamKey`: (Optional) A string that matches against the key of the team the members belong to. It is not case sensitive. - `ignoredMemberIDs`: (Optional) A list of member IDs.  Here's an example:  ```json {   \"instructions\": [{     \"kind\": \"replaceAllMembersRoles\",     \"value\": \"reader\",     \"filterLastSeen\": { \"never\": true }   }] } ```  #### replaceMembersCustomRoles  Replaces the custom roles of the specified members.  ##### Parameters  - `values`: List of new custom roles. Must be a valid custom role key or ID. - `memberIDs`: List of member IDs.  Here's an example:  ```json {   \"instructions\": [{     \"kind\": \"replaceMembersCustomRoles\",     \"values\": [ \"example-custom-role\" ],     \"memberIDs\": [       \"1234a56b7c89d012345e678f\",       \"507f1f77bcf86cd799439011\"     ]   }] } ```  #### replaceAllMembersCustomRoles  Replaces the custom roles of all members. Members that match any of the filters are **excluded** from the update.  ##### Parameters  - `values`: List of new roles. Must be a valid custom role key or ID. - `filterLastSeen`: (Optional) A JSON object with one of the following formats:   - `{\"never\": true}` - Members that have never been active, such as those who have not accepted their invitation to LaunchDarkly, or have not logged in after being provisioned via SCIM.   - `{\"noData\": true}` - Members that have not been active since LaunchDarkly began recording last seen timestamps.   - `{\"before\": 1608672063611}` - Members that have not been active since the provided value, which should be a timestamp in Unix epoch milliseconds. - `filterQuery`: (Optional) A string that matches against the members' emails and names. It is not case sensitive. - `filterRoles`: (Optional) A `|` separated list of roles and custom roles. For the purposes of this filtering, `Owner` counts as `Admin`. - `filterTeamKey`: (Optional) A string that matches against the key of the team the members belong to. It is not case sensitive. - `ignoredMemberIDs`: (Optional) A list of member IDs.  Here's an example:  ```json {   \"instructions\": [{     \"kind\": \"replaceAllMembersCustomRoles\",     \"values\": [ \"example-custom-role\" ],     \"filterLastSeen\": { \"never\": true }   }] } ```  </details> 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import account_members_beta_api
from launchdarkly_api.model.members_patch_input import MembersPatchInput
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.bulk_edit_members_rep import BulkEditMembersRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.status_conflict_error_rep import StatusConflictErrorRep
from pprint import pprint
# Defining the host is optional and defaults to https://app.launchdarkly.com
# See configuration.py for a list of all supported configuration parameters.
configuration = launchdarkly_api.Configuration(
    host = "https://app.launchdarkly.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with launchdarkly_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = account_members_beta_api.AccountMembersBetaApi(api_client)
    members_patch_input = MembersPatchInput(
        comment="Optional comment about the update",
        instructions=Instructions([
            Instruction(
                key=None,
            ),
        ]),
    ) # MembersPatchInput | 

    # example passing only required values which don't have defaults set
    try:
        # Modify account members
        api_response = api_instance.patch_members(members_patch_input)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AccountMembersBetaApi->patch_members: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **members_patch_input** | [**MembersPatchInput**](MembersPatchInput.md)|  |

### Return type

[**BulkEditMembersRep**](BulkEditMembersRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Members response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

