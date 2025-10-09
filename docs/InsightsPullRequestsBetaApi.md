# launchdarkly_api.InsightsPullRequestsBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pull_requests**](InsightsPullRequestsBetaApi.md#get_pull_requests) | **GET** /api/v2/engineering-insights/pull-requests | List pull requests


# **get_pull_requests**
> PullRequestCollectionRep get_pull_requests(project_key, environment_key=environment_key, application_key=application_key, status=status, query=query, limit=limit, expand=expand, sort=sort, var_from=var_from, to=to, after=after, before=before)

List pull requests

Get a list of pull requests  ### Expanding the pull request collection response  LaunchDarkly supports expanding the pull request collection response to include additional fields.  To expand the response, append the `expand` query parameter and include the following:  * `deployments` includes details on all of the deployments associated with each pull request * `flagReferences` includes details on all of the references to flags in each pull request * `leadTime` includes details about the lead time of the pull request for each stage  For example, use `?expand=deployments` to include the `deployments` field in the response. By default, this field is **not** included in the response. 

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.pull_request_collection_rep import PullRequestCollectionRep
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
    api_instance = launchdarkly_api.InsightsPullRequestsBetaApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | Required if you are using the <code>sort</code> parameter's <code>leadTime</code> option to sort pull requests. (optional)
    application_key = 'application_key_example' # str | Filter the results to pull requests deployed to a comma separated list of applications (optional)
    status = 'status_example' # str | Filter results to pull requests with the given status. Options: `open`, `merged`, `closed`, `deployed`. (optional)
    query = 'query_example' # str | Filter list of pull requests by title or author (optional)
    limit = 56 # int | The number of pull requests to return. Default is 20. Maximum allowed is 100. (optional)
    expand = 'expand_example' # str | Expand properties in response. Options: `deployments`, `flagReferences`, `leadTime`. (optional)
    sort = 'sort_example' # str | Sort results. Requires the `environmentKey` to be set. Options: `leadTime` (asc) and `-leadTime` (desc). When query option is excluded, default sort is by created or merged date. (optional)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | Unix timestamp in milliseconds. Default value is 7 days ago. (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime | Unix timestamp in milliseconds. Default value is now. (optional)
    after = 'after_example' # str | Identifier used for pagination (optional)
    before = 'before_example' # str | Identifier used for pagination (optional)

    try:
        # List pull requests
        api_response = api_instance.get_pull_requests(project_key, environment_key=environment_key, application_key=application_key, status=status, query=query, limit=limit, expand=expand, sort=sort, var_from=var_from, to=to, after=after, before=before)
        print("The response of InsightsPullRequestsBetaApi->get_pull_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsightsPullRequestsBetaApi->get_pull_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **environment_key** | **str**| Required if you are using the &lt;code&gt;sort&lt;/code&gt; parameter&#39;s &lt;code&gt;leadTime&lt;/code&gt; option to sort pull requests. | [optional] 
 **application_key** | **str**| Filter the results to pull requests deployed to a comma separated list of applications | [optional] 
 **status** | **str**| Filter results to pull requests with the given status. Options: &#x60;open&#x60;, &#x60;merged&#x60;, &#x60;closed&#x60;, &#x60;deployed&#x60;. | [optional] 
 **query** | **str**| Filter list of pull requests by title or author | [optional] 
 **limit** | **int**| The number of pull requests to return. Default is 20. Maximum allowed is 100. | [optional] 
 **expand** | **str**| Expand properties in response. Options: &#x60;deployments&#x60;, &#x60;flagReferences&#x60;, &#x60;leadTime&#x60;. | [optional] 
 **sort** | **str**| Sort results. Requires the &#x60;environmentKey&#x60; to be set. Options: &#x60;leadTime&#x60; (asc) and &#x60;-leadTime&#x60; (desc). When query option is excluded, default sort is by created or merged date. | [optional] 
 **var_from** | **datetime**| Unix timestamp in milliseconds. Default value is 7 days ago. | [optional] 
 **to** | **datetime**| Unix timestamp in milliseconds. Default value is now. | [optional] 
 **after** | **str**| Identifier used for pagination | [optional] 
 **before** | **str**| Identifier used for pagination | [optional] 

### Return type

[**PullRequestCollectionRep**](PullRequestCollectionRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pull request collection response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

