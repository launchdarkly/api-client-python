# launchdarkly_api.InsightsFlagEventsBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_flag_events**](InsightsFlagEventsBetaApi.md#get_flag_events) | **GET** /api/v2/engineering-insights/flag-events | List flag events


# **get_flag_events**
> FlagEventCollectionRep get_flag_events(project_key, environment_key)

List flag events

Get a list of flag events  ### Expanding the flag event collection response  LaunchDarkly supports expanding the flag event collection response to include additional fields.  To expand the response, append the `expand` query parameter and include the following:  * `experiments` includes details on all of the experiments run on each flag  For example, use `?expand=experiments` to include the `experiments` field in the response. By default, this field is **not** included in the response. 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import insights_flag_events_beta_api
from launchdarkly_api.model.validation_failed_error_rep import ValidationFailedErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.flag_event_collection_rep import FlagEventCollectionRep
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
    api_instance = insights_flag_events_beta_api.InsightsFlagEventsBetaApi(api_client)
    project_key = "projectKey_example" # str | The project key
    environment_key = "environmentKey_example" # str | The environment key
    application_key = "applicationKey_example" # str | Comma separated list of application keys (optional)
    query = "query_example" # str | Filter events by flag key (optional)
    impact_size = "impactSize_example" # str | Filter events by impact size. A small impact created a less than 20% change in the proportion of end users receiving one or more flag variations. A medium impact created between a 20%-80% change. A large impact created a more than 80% change. Options: `none`, `small`, `medium`, `large` (optional)
    has_experiments = True # bool | Filter events to those associated with an experiment (optional)
    _global = "global_example" # str | Filter to include or exclude global events. Default value is `include`. Options: `include`, `exclude` (optional)
    expand = "expand_example" # str | Expand properties in response. Options: `experiments` (optional)
    limit = 1 # int | The number of deployments to return. Default is 20. Maximum allowed is 100. (optional)
    _from = 1 # int | Unix timestamp in milliseconds. Default value is 7 days ago. (optional)
    to = 1 # int | Unix timestamp in milliseconds. Default value is now. (optional)
    after = "after_example" # str | Identifier used for pagination (optional)
    before = "before_example" # str | Identifier used for pagination (optional)

    # example passing only required values which don't have defaults set
    try:
        # List flag events
        api_response = api_instance.get_flag_events(project_key, environment_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling InsightsFlagEventsBetaApi->get_flag_events: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List flag events
        api_response = api_instance.get_flag_events(project_key, environment_key, application_key=application_key, query=query, impact_size=impact_size, has_experiments=has_experiments, _global=_global, expand=expand, limit=limit, _from=_from, to=to, after=after, before=before)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling InsightsFlagEventsBetaApi->get_flag_events: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **environment_key** | **str**| The environment key |
 **application_key** | **str**| Comma separated list of application keys | [optional]
 **query** | **str**| Filter events by flag key | [optional]
 **impact_size** | **str**| Filter events by impact size. A small impact created a less than 20% change in the proportion of end users receiving one or more flag variations. A medium impact created between a 20%-80% change. A large impact created a more than 80% change. Options: &#x60;none&#x60;, &#x60;small&#x60;, &#x60;medium&#x60;, &#x60;large&#x60; | [optional]
 **has_experiments** | **bool**| Filter events to those associated with an experiment | [optional]
 **_global** | **str**| Filter to include or exclude global events. Default value is &#x60;include&#x60;. Options: &#x60;include&#x60;, &#x60;exclude&#x60; | [optional]
 **expand** | **str**| Expand properties in response. Options: &#x60;experiments&#x60; | [optional]
 **limit** | **int**| The number of deployments to return. Default is 20. Maximum allowed is 100. | [optional]
 **_from** | **int**| Unix timestamp in milliseconds. Default value is 7 days ago. | [optional]
 **to** | **int**| Unix timestamp in milliseconds. Default value is now. | [optional]
 **after** | **str**| Identifier used for pagination | [optional]
 **before** | **str**| Identifier used for pagination | [optional]

### Return type

[**FlagEventCollectionRep**](FlagEventCollectionRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Flag event collection response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

