# swagger_client.RootApi

All URIs are relative to *https://app.launchdarkly.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_root**](RootApi.md#get_root) | **GET** / | Get the root resource


# **get_root**
> Links get_root()

Get the root resource

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RootApi()

try: 
    # Get the root resource
    api_response = api_instance.get_root()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RootApi->get_root: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Links**](Links.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

