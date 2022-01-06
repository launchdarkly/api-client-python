# launchdarkly_api.CodeReferencesApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_branches**](CodeReferencesApi.md#delete_branches) | **POST** /api/v2/code-refs/repositories/{repo}/branch-delete-tasks | Delete branches
[**delete_repository**](CodeReferencesApi.md#delete_repository) | **DELETE** /api/v2/code-refs/repositories/{repo} | Delete repository
[**get_branch**](CodeReferencesApi.md#get_branch) | **GET** /api/v2/code-refs/repositories/{repo}/branches/{branch} | Get branch
[**get_branches**](CodeReferencesApi.md#get_branches) | **GET** /api/v2/code-refs/repositories/{repo}/branches | List branches
[**get_extinctions**](CodeReferencesApi.md#get_extinctions) | **GET** /api/v2/code-refs/extinctions | List extinctions
[**get_repositories**](CodeReferencesApi.md#get_repositories) | **GET** /api/v2/code-refs/repositories | List repositories
[**get_repository**](CodeReferencesApi.md#get_repository) | **GET** /api/v2/code-refs/repositories/{repo} | Get repository
[**get_root_statistic**](CodeReferencesApi.md#get_root_statistic) | **GET** /api/v2/code-refs/statistics | Get links to code reference repositories for each project
[**get_statistics**](CodeReferencesApi.md#get_statistics) | **GET** /api/v2/code-refs/statistics/{projKey} | Get number of code references for flags
[**patch_repository**](CodeReferencesApi.md#patch_repository) | **PATCH** /api/v2/code-refs/repositories/{repo} | Update repository
[**post_extinction**](CodeReferencesApi.md#post_extinction) | **POST** /api/v2/code-refs/repositories/{repo}/branches/{branch}/extinction-events | Create extinction
[**post_repository**](CodeReferencesApi.md#post_repository) | **POST** /api/v2/code-refs/repositories | Create repository
[**put_branch**](CodeReferencesApi.md#put_branch) | **PUT** /api/v2/code-refs/repositories/{repo}/branches/{branch} | Upsert branch


# **delete_branches**
> delete_branches(repo, request_body)

Delete branches

Asynchronously delete a number of branches.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import code_references_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
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
    api_instance = code_references_api.CodeReferencesApi(api_client)
    repo = "repo_example" # str | The repository name to delete branches for.
    request_body = [
        "request_body_example",
    ] # [str] | 

    # example passing only required values which don't have defaults set
    try:
        # Delete branches
        api_instance.delete_branches(repo, request_body)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling CodeReferencesApi->delete_branches: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| The repository name to delete branches for. |
 **request_body** | **[str]**|  |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Action succeeded |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_repository**
> delete_repository(repo)

Delete repository

Delete a repository with the specified name

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import code_references_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
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
    api_instance = code_references_api.CodeReferencesApi(api_client)
    repo = "repo_example" # str | The repository name

    # example passing only required values which don't have defaults set
    try:
        # Delete repository
        api_instance.delete_repository(repo)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling CodeReferencesApi->delete_repository: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| The repository name |

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
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_branch**
> BranchRep get_branch(repo, branch)

Get branch

Get a specific branch in a repository

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import code_references_api
from launchdarkly_api.model.branch_rep import BranchRep
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
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
    api_instance = code_references_api.CodeReferencesApi(api_client)
    repo = "repo_example" # str | The repository name
    branch = "branch_example" # str | The url-encoded branch name
    proj_key = "projKey_example" # str | Filter results to a specific project (optional)
    flag_key = "flagKey_example" # str | Filter results to a specific flag key (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get branch
        api_response = api_instance.get_branch(repo, branch)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling CodeReferencesApi->get_branch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get branch
        api_response = api_instance.get_branch(repo, branch, proj_key=proj_key, flag_key=flag_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling CodeReferencesApi->get_branch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| The repository name |
 **branch** | **str**| The url-encoded branch name |
 **proj_key** | **str**| Filter results to a specific project | [optional]
 **flag_key** | **str**| Filter results to a specific flag key | [optional]

### Return type

[**BranchRep**](BranchRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Branch response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_branches**
> BranchCollectionRep get_branches(repo)

List branches

Get a list of branches.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import code_references_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.branch_collection_rep import BranchCollectionRep
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
    api_instance = code_references_api.CodeReferencesApi(api_client)
    repo = "repo_example" # str | The repository name

    # example passing only required values which don't have defaults set
    try:
        # List branches
        api_response = api_instance.get_branches(repo)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling CodeReferencesApi->get_branches: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| The repository name |

### Return type

[**BranchCollectionRep**](BranchCollectionRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Branch collection response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_extinctions**
> ExtinctionCollectionRep get_extinctions()

List extinctions

Get a list of all extinctions.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import code_references_api
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.extinction_collection_rep import ExtinctionCollectionRep
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
    api_instance = code_references_api.CodeReferencesApi(api_client)
    repo_name = "repoName_example" # str | Filter results to a specific repository (optional)
    branch_name = "branchName_example" # str | Filter results to a specific branch. By default, only the default branch will be queried for extinctions. (optional)
    proj_key = "projKey_example" # str | Filter results to a specific project (optional)
    flag_key = "flagKey_example" # str | Filter results to a specific flag key (optional)
    _from = 1 # int | Filter results to a specific timeframe based on commit time, expressed as a Unix epoch time in milliseconds. Must be used with `to`. (optional)
    to = 1 # int | Filter results to a specific timeframe based on commit time, expressed as a Unix epoch time in milliseconds. Must be used with `from`. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List extinctions
        api_response = api_instance.get_extinctions(repo_name=repo_name, branch_name=branch_name, proj_key=proj_key, flag_key=flag_key, _from=_from, to=to)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling CodeReferencesApi->get_extinctions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Filter results to a specific repository | [optional]
 **branch_name** | **str**| Filter results to a specific branch. By default, only the default branch will be queried for extinctions. | [optional]
 **proj_key** | **str**| Filter results to a specific project | [optional]
 **flag_key** | **str**| Filter results to a specific flag key | [optional]
 **_from** | **int**| Filter results to a specific timeframe based on commit time, expressed as a Unix epoch time in milliseconds. Must be used with &#x60;to&#x60;. | [optional]
 **to** | **int**| Filter results to a specific timeframe based on commit time, expressed as a Unix epoch time in milliseconds. Must be used with &#x60;from&#x60;. | [optional]

### Return type

[**ExtinctionCollectionRep**](ExtinctionCollectionRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Extinction collection response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories**
> RepositoryCollectionRep get_repositories()

List repositories

Get a list of connected repositories. Optionally, you can include branch metadata with the `withBranches` query parameter. Embed references for the default branch with `ReferencesForDefaultBranch`. You can also filter the list of code references by project key and flag key.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import code_references_api
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.repository_collection_rep import RepositoryCollectionRep
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
    api_instance = code_references_api.CodeReferencesApi(api_client)
    with_branches = "withBranches_example" # str | If set to any value, the endpoint returns repositories with associated branch data (optional)
    with_references_for_default_branch = "withReferencesForDefaultBranch_example" # str | If set to any value, the endpoint returns repositories with associated branch data, as well as code references for the default git branch (optional)
    proj_key = "projKey_example" # str | A LaunchDarkly project key. If provided, this filters code reference results to the specified project. (optional)
    flag_key = "flagKey_example" # str | If set to any value, the endpoint returns repositories with associated branch data, as well as code references for the default git branch (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List repositories
        api_response = api_instance.get_repositories(with_branches=with_branches, with_references_for_default_branch=with_references_for_default_branch, proj_key=proj_key, flag_key=flag_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling CodeReferencesApi->get_repositories: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **with_branches** | **str**| If set to any value, the endpoint returns repositories with associated branch data | [optional]
 **with_references_for_default_branch** | **str**| If set to any value, the endpoint returns repositories with associated branch data, as well as code references for the default git branch | [optional]
 **proj_key** | **str**| A LaunchDarkly project key. If provided, this filters code reference results to the specified project. | [optional]
 **flag_key** | **str**| If set to any value, the endpoint returns repositories with associated branch data, as well as code references for the default git branch | [optional]

### Return type

[**RepositoryCollectionRep**](RepositoryCollectionRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Repository collection response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository**
> RepositoryRep get_repository(repo)

Get repository

Get a single repository by name.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import code_references_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.repository_rep import RepositoryRep
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
    api_instance = code_references_api.CodeReferencesApi(api_client)
    repo = "repo_example" # str | The repository name

    # example passing only required values which don't have defaults set
    try:
        # Get repository
        api_response = api_instance.get_repository(repo)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling CodeReferencesApi->get_repository: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| The repository name |

### Return type

[**RepositoryRep**](RepositoryRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Repository response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_root_statistic**
> StatisticsRoot get_root_statistic()

Get links to code reference repositories for each project

Get links for all projects that have Code References.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import code_references_api
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.statistics_root import StatisticsRoot
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
    api_instance = code_references_api.CodeReferencesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get links to code reference repositories for each project
        api_response = api_instance.get_root_statistic()
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling CodeReferencesApi->get_root_statistic: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**StatisticsRoot**](StatisticsRoot.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statistic root response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statistics**
> StatisticCollectionRep get_statistics(proj_key)

Get number of code references for flags

Get the number of code references across repositories for all flags in your project that have code references in the default branch (for example: master). You can optionally include the `flagKey` query parameter to get the number of code references across repositories for a single flag. This endpoint returns the number of times your flag keys are referenced in your repositories. You can filter to a single flag with by passing in a flag key.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import code_references_api
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.statistic_collection_rep import StatisticCollectionRep
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
    api_instance = code_references_api.CodeReferencesApi(api_client)
    proj_key = "projKey_example" # str | The project key
    flag_key = "flagKey_example" # str | Filter results to a specific flag key (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get number of code references for flags
        api_response = api_instance.get_statistics(proj_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling CodeReferencesApi->get_statistics: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get number of code references for flags
        api_response = api_instance.get_statistics(proj_key, flag_key=flag_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling CodeReferencesApi->get_statistics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key |
 **flag_key** | **str**| Filter results to a specific flag key | [optional]

### Return type

[**StatisticCollectionRep**](StatisticCollectionRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statistic collection response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_repository**
> RepositoryRep patch_repository(repo, json_patch)

Update repository

Update a repository's settings. The request must be a valid JSON Patch document describing the changes to be made to the repository.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import code_references_api
from launchdarkly_api.model.json_patch import JSONPatch
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.repository_rep import RepositoryRep
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
    api_instance = code_references_api.CodeReferencesApi(api_client)
    repo = "repo_example" # str | The repository name
    json_patch = JSONPatch([
        PatchOperation(
            op="replace",
            path="/biscuits",
            value=None,
        ),
    ]) # JSONPatch | 

    # example passing only required values which don't have defaults set
    try:
        # Update repository
        api_response = api_instance.patch_repository(repo, json_patch)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling CodeReferencesApi->patch_repository: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| The repository name |
 **json_patch** | [**JSONPatch**](JSONPatch.md)|  |

### Return type

[**RepositoryRep**](RepositoryRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Repository response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_extinction**
> post_extinction(repo, branch, extinction_list_post)

Create extinction

Create a new extinction

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import code_references_api
from launchdarkly_api.model.extinction_list_post import ExtinctionListPost
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
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
    api_instance = code_references_api.CodeReferencesApi(api_client)
    repo = "repo_example" # str | The repository name
    branch = "branch_example" # str | The url-encoded branch name
    extinction_list_post = ExtinctionListPost([
        Extinction(
            revision="a94a8fe5ccb19ba61c4c0873d391e987982fbbd3",
            message="Remove flag for launched feature",
            time=1,
            flag_key="enable-feature",
            proj_key="default",
        ),
    ]) # ExtinctionListPost | 

    # example passing only required values which don't have defaults set
    try:
        # Create extinction
        api_instance.post_extinction(repo, branch, extinction_list_post)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling CodeReferencesApi->post_extinction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| The repository name |
 **branch** | **str**| The url-encoded branch name |
 **extinction_list_post** | [**ExtinctionListPost**](ExtinctionListPost.md)|  |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Action succeeded |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_repository**
> RepositoryRep post_repository(repository_post)

Create repository

Create a repository with the specified name.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import code_references_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.repository_post import RepositoryPost
from launchdarkly_api.model.repository_rep import RepositoryRep
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
    api_instance = code_references_api.CodeReferencesApi(api_client)
    repository_post = RepositoryPost(
        name="LaunchDarkly-Docs",
        source_link="https://github.com/launchdarkly/LaunchDarkly-Docs",
        commit_url_template="/commit/${sha}",
        hunk_url_template="/blob/${sha}/${filePath}#L${lineNumber}",
        type="github",
        default_branch="main",
    ) # RepositoryPost | 

    # example passing only required values which don't have defaults set
    try:
        # Create repository
        api_response = api_instance.post_repository(repository_post)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling CodeReferencesApi->post_repository: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_post** | [**RepositoryPost**](RepositoryPost.md)|  |

### Return type

[**RepositoryRep**](RepositoryRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Repository response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_branch**
> put_branch(repo, branch, put_branch)

Upsert branch

Create a new branch if it doesn't exist, or updates the branch if it already exists.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import code_references_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.put_branch import PutBranch
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
    api_instance = code_references_api.CodeReferencesApi(api_client)
    repo = "repo_example" # str | The repository name
    branch = "branch_example" # str | The url-encoded branch name
    put_branch = PutBranch(
        name="main",
        head="a94a8fe5ccb19ba61c4c0873d391e987982fbbd3",
        update_sequence_id=25,
        sync_time=1,
        references=[
            ReferenceRep(
                path="/main/index.js",
                hint="javascript",
                hunks=[
                    HunkRep(
                        starting_line_number=45,
                        lines="var enableFeature = 'enable-feature';",
                        proj_key="default",
                        flag_key="enable-feature",
                        aliases=["enableFeature","EnableFeature"],
                    ),
                ],
            ),
        ],
        commit_time=1,
    ) # PutBranch | 

    # example passing only required values which don't have defaults set
    try:
        # Upsert branch
        api_instance.put_branch(repo, branch, put_branch)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling CodeReferencesApi->put_branch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| The repository name |
 **branch** | **str**| The url-encoded branch name |
 **put_branch** | [**PutBranch**](PutBranch.md)|  |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Action succeeded |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

