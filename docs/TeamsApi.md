# launchdarkly_api.TeamsApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_team**](TeamsApi.md#delete_team) | **DELETE** /api/v2/teams/{teamKey} | Delete team
[**get_team**](TeamsApi.md#get_team) | **GET** /api/v2/teams/{teamKey} | Get team
[**get_team_maintainers**](TeamsApi.md#get_team_maintainers) | **GET** /api/v2/teams/{teamKey}/maintainers | Get team maintainers
[**get_team_roles**](TeamsApi.md#get_team_roles) | **GET** /api/v2/teams/{teamKey}/roles | Get team custom roles
[**get_teams**](TeamsApi.md#get_teams) | **GET** /api/v2/teams | List teams
[**patch_team**](TeamsApi.md#patch_team) | **PATCH** /api/v2/teams/{teamKey} | Update team
[**post_team**](TeamsApi.md#post_team) | **POST** /api/v2/teams | Create team
[**post_team_members**](TeamsApi.md#post_team_members) | **POST** /api/v2/teams/{teamKey}/members | Add multiple members to team


# **delete_team**
> delete_team(team_key)

Delete team

Delete a team by key. To learn more, read [Deleting teams](https://launchdarkly.com/docs/home/account/delete-teams).

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.rest import ApiException
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
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with launchdarkly_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = launchdarkly_api.TeamsApi(api_client)
    team_key = 'team_key_example' # str | The team key

    try:
        # Delete team
        api_instance.delete_team(team_key)
    except Exception as e:
        print("Exception when calling TeamsApi->delete_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_key** | **str**| The team key | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Action succeeded |  -  |
**401** | Invalid access token |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team**
> Team get_team(team_key, expand=expand)

Get team

Fetch a team by key.  ### Expanding the teams response LaunchDarkly supports several fields for expanding the \"Get team\" response. By default, these fields are **not** included in the response.  To expand the response, append the `expand` query parameter and add a comma-separated list with any of the following fields:  * `members` includes the total count of members that belong to the team. * `roles` includes a paginated list of the custom roles that you have assigned to the team. * `roleAttributes` includes a list of the role attributes that you have assigned to the team. * `projects` includes a paginated list of the projects that the team has any write access to. * `maintainers` includes a paginated list of the maintainers that you have assigned to the team.  For example, `expand=members,roles` includes the `members` and `roles` fields in the response. 

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.team import Team
from launchdarkly_api.rest import ApiException
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
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with launchdarkly_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = launchdarkly_api.TeamsApi(api_client)
    team_key = 'team_key_example' # str | The team key.
    expand = 'expand_example' # str | A comma-separated list of properties that can reveal additional information in the response. (optional)

    try:
        # Get team
        api_response = api_instance.get_team(team_key, expand=expand)
        print("The response of TeamsApi->get_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->get_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_key** | **str**| The team key. | 
 **expand** | **str**| A comma-separated list of properties that can reveal additional information in the response. | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Teams response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**405** | Method not allowed |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_maintainers**
> TeamMaintainers get_team_maintainers(team_key, limit=limit, offset=offset)

Get team maintainers

Fetch the maintainers that have been assigned to the team. To learn more, read [Managing team maintainers](https://launchdarkly.com/docs/home/account/team-maintainers).

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.team_maintainers import TeamMaintainers
from launchdarkly_api.rest import ApiException
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
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with launchdarkly_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = launchdarkly_api.TeamsApi(api_client)
    team_key = 'team_key_example' # str | The team key
    limit = 56 # int | The number of maintainers to return in the response. Defaults to 20. (optional)
    offset = 56 # int | Where to start in the list. This is for use with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)

    try:
        # Get team maintainers
        api_response = api_instance.get_team_maintainers(team_key, limit=limit, offset=offset)
        print("The response of TeamsApi->get_team_maintainers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->get_team_maintainers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_key** | **str**| The team key | 
 **limit** | **int**| The number of maintainers to return in the response. Defaults to 20. | [optional] 
 **offset** | **int**| Where to start in the list. This is for use with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] 

### Return type

[**TeamMaintainers**](TeamMaintainers.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Team maintainers response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**405** | Method not allowed |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_roles**
> TeamCustomRoles get_team_roles(team_key, limit=limit, offset=offset)

Get team custom roles

Fetch the custom roles that have been assigned to the team. To learn more, read [Managing team permissions](https://launchdarkly.com/docs/home/account/team-permissions).

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.team_custom_roles import TeamCustomRoles
from launchdarkly_api.rest import ApiException
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
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with launchdarkly_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = launchdarkly_api.TeamsApi(api_client)
    team_key = 'team_key_example' # str | The team key
    limit = 56 # int | The number of roles to return in the response. Defaults to 20. (optional)
    offset = 56 # int | Where to start in the list. This is for use with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)

    try:
        # Get team custom roles
        api_response = api_instance.get_team_roles(team_key, limit=limit, offset=offset)
        print("The response of TeamsApi->get_team_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->get_team_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_key** | **str**| The team key | 
 **limit** | **int**| The number of roles to return in the response. Defaults to 20. | [optional] 
 **offset** | **int**| Where to start in the list. This is for use with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] 

### Return type

[**TeamCustomRoles**](TeamCustomRoles.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Team roles response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**405** | Method not allowed |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_teams**
> Teams get_teams(limit=limit, offset=offset, filter=filter, expand=expand)

List teams

Return a list of teams.  By default, this returns the first 20 teams. Page through this list with the `limit` parameter and by following the `first`, `prev`, `next`, and `last` links in the `_links` field that returns. If those links do not appear, the pages they refer to don't exist. For example, the `first` and `prev` links will be missing from the response on the first page, because there is no previous page and you cannot return to the first page when you are already on the first page.  ### Filtering teams  LaunchDarkly supports the following fields for filters:  - `query` is a string that matches against the teams' names and keys. It is not case-sensitive.   - A request with `query:abc` returns teams with the string `abc` in their name or key. - `nomembers` is a boolean that filters the list of teams who have 0 members   - A request with `nomembers:true` returns teams that have 0 members   - A request with `nomembers:false` returns teams that have 1 or more members  ### Expanding the teams response LaunchDarkly supports expanding several fields in the \"List teams\" response. By default, these fields are **not** included in the response.  To expand the response, append the `expand` query parameter and add a comma-separated list with any of the following fields:  * `members` includes the total count of members that belong to the team. * `roles` includes a paginated list of the custom roles that you have assigned to the team. * `roleAttributes` includes a list of the role attributes that you have assigned to the team. * `projects` includes a paginated list of the projects that the team has any write access to. * `maintainers` includes a paginated list of the maintainers that you have assigned to the team.  For example, `expand=members,maintainers` includes the `members` and `maintainers` fields in the response. 

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.teams import Teams
from launchdarkly_api.rest import ApiException
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
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with launchdarkly_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = launchdarkly_api.TeamsApi(api_client)
    limit = 56 # int | The number of teams to return in the response. Defaults to 20. (optional)
    offset = 56 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and returns the next `limit` items. (optional)
    filter = 'filter_example' # str | A comma-separated list of filters. Each filter is constructed as `field:value`. (optional)
    expand = 'expand_example' # str | A comma-separated list of properties that can reveal additional information in the response. (optional)

    try:
        # List teams
        api_response = api_instance.get_teams(limit=limit, offset=offset, filter=filter, expand=expand)
        print("The response of TeamsApi->get_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->get_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of teams to return in the response. Defaults to 20. | [optional] 
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and returns the next &#x60;limit&#x60; items. | [optional] 
 **filter** | **str**| A comma-separated list of filters. Each filter is constructed as &#x60;field:value&#x60;. | [optional] 
 **expand** | **str**| A comma-separated list of properties that can reveal additional information in the response. | [optional] 

### Return type

[**Teams**](Teams.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Teams collection response |  -  |
**401** | Invalid access token |  -  |
**405** | Method not allowed |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_team**
> Team patch_team(team_key, team_patch_input, expand=expand)

Update team

Perform a partial update to a team. Updating a team uses the semantic patch format.  To make a semantic patch request, you must append `domain-model=launchdarkly.semanticpatch` to your `Content-Type` header. To learn more, read [Updates using semantic patch](https://launchdarkly.com/docs/api#updates-using-semantic-patch).  ### Instructions  Semantic patch requests support the following `kind` instructions for updating teams. Several of the instructions require one or more member IDs as parameters. The member ID is returned as part of the [List account members](https://launchdarkly.com/docs/api/account-members/get-members) response. It is the `_id` field of each element in the `items` array.   <details> <summary>Click to expand instructions for <strong>updating teams</strong></summary>  #### addCustomRoles  Adds custom roles to the team. Team members will have these custom roles granted to them.  ##### Parameters  - `values`: List of custom role keys.  Here's an example:  ```json {   \"instructions\": [{     \"kind\": \"addCustomRoles\",     \"values\": [ \"example-custom-role\" ]   }] } ```  #### addMembers  Adds members to the team.  ##### Parameters  - `values`: List of member IDs to add.  Here's an example:  ```json {   \"instructions\": [{     \"kind\": \"addMembers\",     \"values\": [ \"1234a56b7c89d012345e678f\", \"507f1f77bcf86cd799439011\" ]   }] } ```  #### addPermissionGrants  Adds permission grants to members for the team. For example, a permission grant could allow a member to act as a team maintainer. A permission grant may have either an `actionSet` or a list of `actions` but not both at the same time. The members do not have to be team members to have a permission grant for the team.  ##### Parameters  - `actionSet`: Name of the action set. - `actions`: List of actions. - `memberIDs`: List of member IDs.  Here's an example:  ```json {   \"instructions\": [{     \"kind\": \"addPermissionGrants\",     \"actions\": [ \"updateTeamName\", \"updateTeamDescription\" ],     \"memberIDs\": [ \"1234a56b7c89d012345e678f\", \"507f1f77bcf86cd799439011\" ]   }] } ```  #### addRoleAttribute  Adds a role attribute to a team. Team members will have these role attribute values scoped for all custom roles granted to them.  ##### Parameters  - `key`: The role attribute key to add. - `values`: List of role attribute values for that key.  Here's an example:  ```json {   \"instructions\": [     {       \"kind\": \"addRoleAttribute\",       \"key\": \"testAttribute\",       \"values\": [\"someNewValue\", \"someOtherNewValue\"]     }   ] } ```  #### removeCustomRoles  Removes custom roles from the team. The app will no longer grant these custom roles to the team members.  ##### Parameters  - `values`: List of custom role keys.  Here's an example:  ```json {   \"instructions\": [{     \"kind\": \"removeCustomRoles\",     \"values\": [ \"example-custom-role\" ]   }] } ```  #### removeMembers  Removes members from the team.  ##### Parameters  - `values`: List of member IDs to remove.  Here's an example:  ```json {   \"instructions\": [{     \"kind\": \"removeMembers\",     \"values\": [ \"1234a56b7c89d012345e678f\", \"507f1f77bcf86cd799439011\" ]   }] } ```  #### removePermissionGrants  Removes permission grants from members for the team. A permission grant may have either an `actionSet` or a list of `actions` but not both at the same time. The `actionSet` and `actions` must match an existing permission grant.  ##### Parameters  - `actionSet`: Name of the action set. - `actions`: List of actions. - `memberIDs`: List of member IDs.  Here's an example:  ```json {   \"instructions\": [{     \"kind\": \"removePermissionGrants\",     \"actions\": [ \"updateTeamName\", \"updateTeamDescription\" ],     \"memberIDs\": [ \"1234a56b7c89d012345e678f\", \"507f1f77bcf86cd799439011\" ]   }] } ```  #### removeRoleAttribute  Removes a role attribute from the team.  ##### Parameters  - `key`: The role attribute key to remove.  Here's an example: ```json {   \"instructions\": [     {       \"kind\": \"removeRoleAttribute\",       \"key\": \"testAttribute\"     }   ] } ```  #### replaceMembers  Replaces the existing members of the team with the new members.  ##### Parameters  - `values`: List of member IDs of the new members.  Here's an example:  ```json {   \"instructions\": [{     \"kind\": \"replaceMembers\",     \"values\": [ \"1234a56b7c89d012345e678f\", \"507f1f77bcf86cd799439011\" ]   }] } ```  #### replaceRoleAttributes  Replaces the existing role attributes for the team with new role attributes.  ##### Parameters  - `value`: A map of role attribute keys to lists of role attribute values  Here's an example:  ```json {   \"instructions\": [{     \"kind\": \"replaceRoleAttributes\",     \"value\": {       \"testAttribute\": [ \"someNewValue\", \"someOtherNewValue\" ],       \"projectRoleAttribute\": [ \"project1\", \"project2\"]     }   }] } ```  #### updateDescription  Updates the description of the team.  ##### Parameters  - `value`: The new description.  Here's an example:  ```json {   \"instructions\": [{     \"kind\": \"updateDescription\",     \"value\": \"Updated team description\"   }] } ```  #### updateName  Updates the name of the team.  ##### Parameters  - `value`: The new name.  Here's an example:  ```json {   \"instructions\": [{     \"kind\": \"updateName\",     \"value\": \"Updated team name\"   }] } ```  #### updateRoleAttribute  Updates a role attribute on the team. Any existing values for the given key will be replaced with the new values. Team members will have these role attribute values scoped for all custom roles granted to them.  ##### Parameters  - `key`: The role attribute key to update. - `values`: List of role attribute values for that key.  Here's an example: ```json {   \"instructions\": [     {       \"kind\": \"updateRoleAttribute\",       \"key\": \"testAttribute\",       \"values\": [\"someNewValue\", \"someOtherNewValue\"]     }   ] } ```  </details>  ### Expanding the teams response LaunchDarkly supports four fields for expanding the \"Update team\" response. By default, these fields are **not** included in the response.  To expand the response, append the `expand` query parameter and add a comma-separated list with any of the following fields:  * `members` includes the total count of members that belong to the team. * `roles` includes a paginated list of the custom roles that you have assigned to the team. * `projects` includes a paginated list of the projects that the team has any write access to. * `maintainers` includes a paginated list of the maintainers that you have assigned to the team.  For example, `expand=members,roles` includes the `members` and `roles` fields in the response. 

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.team import Team
from launchdarkly_api.models.team_patch_input import TeamPatchInput
from launchdarkly_api.rest import ApiException
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
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with launchdarkly_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = launchdarkly_api.TeamsApi(api_client)
    team_key = 'team_key_example' # str | The team key
    team_patch_input = {"comment":"Optional comment about the update","instructions":[{"kind":"updateDescription","value":"New description for the team"}]} # TeamPatchInput | 
    expand = 'expand_example' # str | A comma-separated list of properties that can reveal additional information in the response. Supported fields are explained above. (optional)

    try:
        # Update team
        api_response = api_instance.patch_team(team_key, team_patch_input, expand=expand)
        print("The response of TeamsApi->patch_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->patch_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_key** | **str**| The team key | 
 **team_patch_input** | [**TeamPatchInput**](TeamPatchInput.md)|  | 
 **expand** | **str**| A comma-separated list of properties that can reveal additional information in the response. Supported fields are explained above. | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Teams response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**404** | Invalid resource identifier |  -  |
**405** | Method not allowed |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_team**
> Team post_team(team_post_input, expand=expand)

Create team

Create a team. To learn more, read [Creating a team](https://launchdarkly.com/docs/home/account/create-teams).  ### Expanding the teams response LaunchDarkly supports four fields for expanding the \"Create team\" response. By default, these fields are **not** included in the response.  To expand the response, append the `expand` query parameter and add a comma-separated list with any of the following fields:  * `members` includes the total count of members that belong to the team. * `roles` includes a paginated list of the custom roles that you have assigned to the team. * `projects` includes a paginated list of the projects that the team has any write access to. * `maintainers` includes a paginated list of the maintainers that you have assigned to the team.  For example, `expand=members,roles` includes the `members` and `roles` fields in the response. 

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.team import Team
from launchdarkly_api.models.team_post_input import TeamPostInput
from launchdarkly_api.rest import ApiException
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
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with launchdarkly_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = launchdarkly_api.TeamsApi(api_client)
    team_post_input = {"customRoleKeys":["example-role1","example-role2"],"description":"An example team","key":"team-key-123abc","memberIDs":["12ab3c45de678910fgh12345"],"name":"Example team"} # TeamPostInput | 
    expand = 'expand_example' # str | A comma-separated list of properties that can reveal additional information in the response. Supported fields are explained above. (optional)

    try:
        # Create team
        api_response = api_instance.post_team(team_post_input, expand=expand)
        print("The response of TeamsApi->post_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->post_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_post_input** | [**TeamPostInput**](TeamPostInput.md)|  | 
 **expand** | **str**| A comma-separated list of properties that can reveal additional information in the response. Supported fields are explained above. | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Teams response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**405** | Method not allowed |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_team_members**
> TeamImportsRep post_team_members(team_key, file=file)

Add multiple members to team

Add multiple members to an existing team by uploading a CSV file of member email addresses. Your CSV file must include email addresses in the first column. You can include data in additional columns, but LaunchDarkly ignores all data outside the first column. Headers are optional. To learn more, read [Manage team members](https://launchdarkly.com/docs/home/account/manage-teams#manage-team-members).  **Members are only added on a `201` response.** A `207` indicates the CSV file contains a combination of valid and invalid entries. A `207` results in no members being added to the team.  On a `207` response, if an entry contains bad input, the `message` field contains the row number as well as the reason for the error. The `message` field is omitted if the entry is valid.  Example `207` response: ```json {   \"items\": [     {       \"status\": \"success\",       \"value\": \"new-team-member@acme.com\"     },     {       \"message\": \"Line 2: empty row\",       \"status\": \"error\",       \"value\": \"\"     },     {       \"message\": \"Line 3: email already exists in the specified team\",       \"status\": \"error\",       \"value\": \"existing-team-member@acme.com\"     },     {       \"message\": \"Line 4: invalid email formatting\",       \"status\": \"error\",       \"value\": \"invalid email format\"     }   ] } ```  Message | Resolution --- | --- Empty row | This line is blank. Add an email address and try again. Duplicate entry | This email address appears in the file twice. Remove the email from the file and try again. Email already exists in the specified team | This member is already on your team. Remove the email from the file and try again. Invalid formatting | This email address is not formatted correctly. Fix the formatting and try again. Email does not belong to a LaunchDarkly member | The email address doesn't belong to a LaunchDarkly account member. Invite them to LaunchDarkly, then re-add them to the team.  On a `400` response, the `message` field may contain errors specific to this endpoint.  Example `400` response: ```json {   \"code\": \"invalid_request\",   \"message\": \"Unable to process file\" } ```  Message | Resolution --- | --- Unable to process file | LaunchDarkly could not process the file for an unspecified reason. Review your file for errors and try again. File exceeds 25mb | Break up your file into multiple files of less than 25mbs each. All emails have invalid formatting | None of the email addresses in the file are in the correct format. Fix the formatting and try again. All emails belong to existing team members | All listed members are already on this team. Populate the file with member emails that do not belong to the team and try again. File is empty | The CSV file does not contain any email addresses. Populate the file and try again. No emails belong to members of your LaunchDarkly organization | None of the email addresses belong to members of your LaunchDarkly account. Invite these members to LaunchDarkly, then re-add them to the team. 

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.team_imports_rep import TeamImportsRep
from launchdarkly_api.rest import ApiException
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
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with launchdarkly_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = launchdarkly_api.TeamsApi(api_client)
    team_key = 'team_key_example' # str | The team key
    file = None # bytearray | CSV file containing email addresses (optional)

    try:
        # Add multiple members to team
        api_response = api_instance.post_team_members(team_key, file=file)
        print("The response of TeamsApi->post_team_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->post_team_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_key** | **str**| The team key | 
 **file** | **bytearray**| CSV file containing email addresses | [optional] 

### Return type

[**TeamImportsRep**](TeamImportsRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Team member imports response |  -  |
**207** | Partial Success |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**405** | Method not allowed |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

