# Objects

## `Attachment`
Stores data used for [`Message`](/groupmeme/api/#message) attachments.

Attachment Type (`_type`) | Parameters
--|--
`'image'` | `url` 
`'location'` | `lat`, `lng`, `name` 
`'split'` | `token`
`'emoji'` | `placeholder`, `charmap`

### `Attachment.__init__`
- **`_type (str)`**: type of attachment, can be (`'image'`|`'location'`|`'split'`|`'emoji'`)
- **`url (str|None)`**: GroupMe CDN url for `'image'` attachments
- **`lat (str|None)`**: Latitude value for `'location'` attachments
- **`lng (str|None)`**: Longitude value for `'location'` attachments
- **`name (str|None)`**: Name for `'location'` attachments
- **`token (str|None)`**: Token value for `'split'` attachments
- **`placeholder (str|None)`**: Placeholder for `'emoji'` attachments
- **`charmap (any)`**: Charmap for `'emoji'` attachments