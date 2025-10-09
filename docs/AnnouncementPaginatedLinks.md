# AnnouncementPaginatedLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | [**AnnouncementLink**](AnnouncementLink.md) |  | [optional] 
**last** | [**AnnouncementLink**](AnnouncementLink.md) |  | [optional] 
**next** | [**AnnouncementLink**](AnnouncementLink.md) |  | [optional] 
**prev** | [**AnnouncementLink**](AnnouncementLink.md) |  | [optional] 
**var_self** | [**AnnouncementLink**](AnnouncementLink.md) |  | 

## Example

```python
from launchdarkly_api.models.announcement_paginated_links import AnnouncementPaginatedLinks

# TODO update the JSON string below
json = "{}"
# create an instance of AnnouncementPaginatedLinks from a JSON string
announcement_paginated_links_instance = AnnouncementPaginatedLinks.from_json(json)
# print the JSON string representation of the object
print(AnnouncementPaginatedLinks.to_json())

# convert the object into a dict
announcement_paginated_links_dict = announcement_paginated_links_instance.to_dict()
# create an instance of AnnouncementPaginatedLinks from a dict
announcement_paginated_links_from_dict = AnnouncementPaginatedLinks.from_dict(announcement_paginated_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


