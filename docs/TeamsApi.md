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

Delete a team by key. To learn more, read [Deleting a team](https://docs.launchdarkly.com/home/teams/managing#deleting-a-team).

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import teams_api
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
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
    api_instance = teams_api.TeamsApi(api_client)
    team_key = "teamKey_example" # str | The team key

    # example passing only required values which don't have defaults set
    try:
        # Delete team
        api_instance.delete_team(team_key)
    except launchdarkly_api.ApiException as e:
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
> Team get_team(team_key)

Get team

Fetch a team by key.  ### Expanding the teams response LaunchDarkly supports four fields for expanding the \"Get team\" response. By default, these fields are **not** included in the response.  To expand the response, append the `expand` query parameter and add a comma-separated list with any of the following fields:  * `members` includes the total count of members that belong to the team. * `roles` includes a paginated list of the custom roles that you have assigned to the team. * `projects` includes a paginated list of the projects that the team has any write access to. * `maintainers` includes a paginated list of the maintainers that you have assigned to the team.  For example, `expand=members,roles` includes the `members` and `roles` fields in the response. 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import teams_api
from launchdarkly_api.model.team import Team
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.method_not_allowed_error_rep import MethodNotAllowedErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
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
    api_instance = teams_api.TeamsApi(api_client)
    team_key = "teamKey_example" # str | The team key.
    expand = "expand_example" # str | A comma-separated list of properties that can reveal additional information in the response. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get team
        api_response = api_instance.get_team(team_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling TeamsApi->get_team: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get team
        api_response = api_instance.get_team(team_key, expand=expand)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
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
**200** | Teams response JSON |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**405** | Method not allowed |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_maintainers**
> TeamMaintainers get_team_maintainers(team_key)

Get team maintainers

Fetch the maintainers that have been assigned to the team. To learn more, read [Managing team maintainers](https://docs.launchdarkly.com/home/teams/managing#managing-team-maintainers).

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import teams_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.method_not_allowed_error_rep import MethodNotAllowedErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.team_maintainers import TeamMaintainers
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
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
    api_instance = teams_api.TeamsApi(api_client)
    team_key = "teamKey_example" # str | The team key
    limit = 1 # int | The number of maintainers to return in the response. Defaults to 20. (optional)
    offset = 1 # int | Where to start in the list. This is for use with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get team maintainers
        api_response = api_instance.get_team_maintainers(team_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling TeamsApi->get_team_maintainers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get team maintainers
        api_response = api_instance.get_team_maintainers(team_key, limit=limit, offset=offset)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
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
**200** | Team maintainers response JSON |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**405** | Method not allowed |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_roles**
> TeamCustomRoles get_team_roles(team_key)

Get team custom roles

Fetch the custom roles that have been assigned to the team. To learn more, read [Managing team permissions](https://docs.launchdarkly.com/home/teams/managing#managing-team-permissions).

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import teams_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.method_not_allowed_error_rep import MethodNotAllowedErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.team_custom_roles import TeamCustomRoles
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
    api_instance = teams_api.TeamsApi(api_client)
    team_key = "teamKey_example" # str | The team key
    limit = 1 # int | The number of roles to return in the response. Defaults to 20. (optional)
    offset = 1 # int | Where to start in the list. This is for use with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get team custom roles
        api_response = api_instance.get_team_roles(team_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling TeamsApi->get_team_roles: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get team custom roles
        api_response = api_instance.get_team_roles(team_key, limit=limit, offset=offset)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
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
**200** | Team roles response JSON |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**405** | Method not allowed |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_teams**
> Teams get_teams()

List teams

Return a list of teams.  By default, this returns the first 20 teams. Page through this list with the `limit` parameter and by following the `first`, `prev`, `next`, and `last` links in the `_links` field that returns. If those links do not appear, the pages they refer to don't exist. For example, the `first` and `prev` links will be missing from the response on the first page, because there is no previous page and you cannot return to the first page when you are already on the first page.  ### Filtering teams  LaunchDarkly supports the `query` field for filtering. `query` is a string that matches against the teams' names and keys. For example, the filter `query:abc` matches teams with the string `abc` in their name or key. The filter is not case-sensitive.  ### Expanding the teams response LaunchDarkly supports four fields for expanding the \"List teams\" response. By default, these fields are **not** included in the response.  To expand the response, append the `expand` query parameter and add a comma-separated list with any of the following fields:  * `members` includes the total count of members that belong to the team. * `roles` includes a paginated list of the custom roles that you have assigned to the team. * `projects` includes a paginated list of the projects that the team has any write access to. * `maintainers` includes a paginated list of the maintainers that you have assigned to the team.  For example, `expand=members,roles` includes the `members` and `roles` fields in the response. 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import teams_api
from launchdarkly_api.model.method_not_allowed_error_rep import MethodNotAllowedErrorRep
from launchdarkly_api.model.teams import Teams
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
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
    api_instance = teams_api.TeamsApi(api_client)
    limit = 1 # int | The number of teams to return in the response. Defaults to 20. (optional)
    offset = 1 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and returns the next `limit` items. (optional)
    filter = "filter_example" # str | A comma-separated list of filters. Each filter is constructed as `field:value`. (optional)
    expand = "expand_example" # str | A comma-separated list of properties that can reveal additional information in the response. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List teams
        api_response = api_instance.get_teams(limit=limit, offset=offset, filter=filter, expand=expand)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
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
**200** | Teams collection response JSON |  -  |
**401** | Invalid access token |  -  |
**405** | Method not allowed |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_team**
> Team patch_team(team_key, team_patch_input)

Update team

Perform a partial update to a team. Updating a team uses the semantic patch format.  To make a semantic patch request, you must append `domain-model=launchdarkly.semanticpatch` to your `Content-Type` header. To learn more, read [Updates using semantic patch](/reference#updates-using-semantic-patch).  ### Instructions  Semantic patch requests support the following `kind` instructions for updating teams.  #### addCustomRoles  Adds custom roles to the team. Team members will have these custom roles granted to them.  ##### Parameters  - `values`: List of custom role keys.  #### removeCustomRoles  Removes custom roles from the team. The app will no longer grant these custom roles to the team members.  ##### Parameters  - `values`: List of custom role keys.  #### addMembers  Adds members to the team.  ##### Parameters  - `values`: List of member IDs.  #### removeMembers  Removes members from the team.  ##### Parameters  - `values`: List of member IDs.  #### addPermissionGrants  Adds permission grants to members for the team. For example, a permission grant could allow a member to act as a team maintainer. A permission grant may have either an `actionSet` or a list of `actions` but not both at the same time. The members do not have to be team members to have a permission grant for the team.  ##### Parameters  - `actionSet`: Name of the action set. - `actions`: List of actions. - `memberIDs`: List of member IDs.  #### removePermissionGrants  Removes permission grants from members for the team. The `actionSet` and `actions` must match an existing permission grant.  ##### Parameters  - `actionSet`: Name of the action set. - `actions`: List of actions. - `memberIDs`: List of member IDs.  #### updateDescription  Updates the description of the team.  ##### Parameters  - `value`: The new description.  #### updateName  Updates the name of the team.  ##### Parameters  - `value`: The new name.  ### Expanding the teams response LaunchDarkly supports four fields for expanding the \"Update team\" response. By default, these fields are **not** included in the response.  To expand the response, append the `expand` query parameter and add a comma-separated list with any of the following fields:  * `members` includes the total count of members that belong to the team. * `roles` includes a paginated list of the custom roles that you have assigned to the team. * `projects` includes a paginated list of the projects that the team has any write access to. * `maintainers` includes a paginated list of the maintainers that you have assigned to the team.  For example, `expand=members,roles` includes the `members` and `roles` fields in the response. 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import teams_api
from launchdarkly_api.model.team import Team
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.method_not_allowed_error_rep import MethodNotAllowedErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.team_patch_input import TeamPatchInput
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
    api_instance = teams_api.TeamsApi(api_client)
    team_key = "teamKey_example" # str | The team key
    team_patch_input = TeamPatchInput(
        comment="Optional comment about the update",
        instructions=Instructions([
            Instruction(
                key=None,
            ),
        ]),
    ) # TeamPatchInput | 
    expand = "expand_example" # str | A comma-separated list of properties that can reveal additional information in the response. Supported fields are explained above. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update team
        api_response = api_instance.patch_team(team_key, team_patch_input)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling TeamsApi->patch_team: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update team
        api_response = api_instance.patch_team(team_key, team_patch_input, expand=expand)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
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
**200** | Teams response JSON |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**404** | Invalid resource identifier |  -  |
**405** | Method not allowed |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_team**
> Team post_team(team_post_input)

Create team

Create a team. To learn more, read [Creating a team](https://docs.launchdarkly.com/home/teams/creating).  ### Expanding the teams response LaunchDarkly supports four fields for expanding the \"Create team\" response. By default, these fields are **not** included in the response.  To expand the response, append the `expand` query parameter and add a comma-separated list with any of the following fields:  * `members` includes the total count of members that belong to the team. * `roles` includes a paginated list of the custom roles that you have assigned to the team. * `projects` includes a paginated list of the projects that the team has any write access to. * `maintainers` includes a paginated list of the maintainers that you have assigned to the team.  For example, `expand=members,roles` includes the `members` and `roles` fields in the response. 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import teams_api
from launchdarkly_api.model.team import Team
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.method_not_allowed_error_rep import MethodNotAllowedErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.team_post_input import TeamPostInput
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
    api_instance = teams_api.TeamsApi(api_client)
    team_post_input = TeamPostInput(
        custom_role_keys=["example-role1","example-role2"],
        description="An example team",
        key="example-team",
        member_ids=["12ab3c45de678910fgh12345"],
        name="Example team",
        permission_grants=[
            PermissionGrantInput(
                action_set="maintainTeam",
                actions=["updateTeamMembers"],
                member_ids=["12ab3c45de678910fgh12345"],
            ),
        ],
    ) # TeamPostInput | 
    expand = "expand_example" # str | A comma-separated list of properties that can reveal additional information in the response. Supported fields are explained above. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create team
        api_response = api_instance.post_team(team_post_input)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling TeamsApi->post_team: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create team
        api_response = api_instance.post_team(team_post_input, expand=expand)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
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
**201** | Successful teams response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**405** | Method not allowed |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_team_members**
> TeamImportsRep post_team_members(team_key)

Add multiple members to team

Add multiple members to an existing team by uploading a CSV file of member email addresses. Your CSV file must include email addresses in the first column. You can include data in additional columns, but LaunchDarkly ignores all data outside the first column. Headers are optional. To learn more, read [Managing team members](https://docs.launchdarkly.com/home/teams/managing#managing-team-members).  **Members are only added on a `201` response.** A `207` indicates the CSV file contains a combination of valid and invalid entries. A `207` results in no members being added to the team.  On a `207` response, if an entry contains bad user input, the `message` field contains the row number as well as the reason for the error. The `message` field is omitted if the entry is valid.  Example `207` response: ```json {   \"items\": [     {       \"status\": \"success\",       \"value\": \"a-valid-email@launchdarkly.com\"     },     {       \"message\": \"Line 2: empty row\",       \"status\": \"error\",       \"value\": \"\"     },     {       \"message\": \"Line 3: email already exists in the specified team\",       \"status\": \"error\",       \"value\": \"existing-team-member@launchdarkly.com\"     },     {       \"message\": \"Line 4: invalid email formatting\",       \"status\": \"error\",       \"value\": \"invalid email format\"     }   ] } ```  Message | Resolution --- | --- Empty row | This line is blank. Add an email address and try again. Duplicate entry | This email address appears in the file twice. Remove the email from the file and try again. Email already exists in the specified team | This member is already on your team. Remove the email from the file and try again. Invalid formatting | This email address is not formatted correctly. Fix the formatting and try again. Email does not belong to a LaunchDarkly member | The email address doesn't belong to a LaunchDarkly account member. Invite them to LaunchDarkly, then re-add them to the team.  On a `400` response, the `message` field may contain errors specific to this endpoint.  Example `400` response: ```json {   \"code\": \"invalid_request\",   \"message\": \"Unable to process file\" } ```  Message | Resolution --- | --- Unable to process file | LaunchDarkly could not process the file for an unspecified reason. Review your file for errors and try again. File exceeds 25mb | Break up your file into multiple files of less than 25mbs each. All emails have invalid formatting | None of the email addresses in the file are in the correct format. Fix the formatting and try again. All emails belong to existing team members | All listed members are already on this team. Populate the file with member emails that do not belong to the team and try again. File is empty | The CSV file does not contain any email addresses. Populate the file and try again. No emails belong to members of your LaunchDarkly organization | None of the email addresses belong to members of your LaunchDarkly account. Invite these members to LaunchDarkly, then re-add them to the team. 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import teams_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.method_not_allowed_error_rep import MethodNotAllowedErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.team_imports_rep import TeamImportsRep
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
    api_instance = teams_api.TeamsApi(api_client)
    team_key = "teamKey_example" # str | The team key
    file = open('/path/to/file', 'rb') # file_type | CSV file containing email addresses (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add multiple members to team
        api_response = api_instance.post_team_members(team_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling TeamsApi->post_team_members: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add multiple members to team
        api_response = api_instance.post_team_members(team_key, file=file)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling TeamsApi->post_team_members: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_key** | **str**| The team key |
 **file** | **file_type**| CSV file containing email addresses | [optional]

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
**201** | Team member imports response JSON |  -  |
**207** | Partial Success |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**405** | Method not allowed |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

