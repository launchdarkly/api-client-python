# ViewsPaginatedLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | [**ViewsLink**](ViewsLink.md) |  | [optional] 
**last** | [**ViewsLink**](ViewsLink.md) |  | [optional] 
**next** | [**ViewsLink**](ViewsLink.md) |  | [optional] 
**prev** | [**ViewsLink**](ViewsLink.md) |  | [optional] 
**var_self** | [**ViewsLink**](ViewsLink.md) |  | 

## Example

```python
from launchdarkly_api.models.views_paginated_links import ViewsPaginatedLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ViewsPaginatedLinks from a JSON string
views_paginated_links_instance = ViewsPaginatedLinks.from_json(json)
# print the JSON string representation of the object
print(ViewsPaginatedLinks.to_json())

# convert the object into a dict
views_paginated_links_dict = views_paginated_links_instance.to_dict()
# create an instance of ViewsPaginatedLinks from a dict
views_paginated_links_from_dict = ViewsPaginatedLinks.from_dict(views_paginated_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


