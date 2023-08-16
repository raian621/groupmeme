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


## `ChatMessage`
### `ChatMessage.__init__`
`ChatMessage` constructor.
    
**params:**
- **`id (str)`**: The ID of the chat.
- **`name (str)`**: The name of the user that sent the message.
- **`conversation_id (str)`**: The ID of the conversation / chat.
- **`created_at (int)`**: The time (Unix time) that the message was created.
- **`recipient_id (str)`**: The ID of the user that received the message.
- **`sender_id (str)`**: The ID of the user that sent the message.
- **`sender_type (str)`**: The type of sender that sent the message (ex. "user", "system).
- **`source_guid (str)`**: The `source_guid` of the message.
- **`attachments (list[Attachment])`**: Attachments on the message.
- **`favorited_by (list[str])`**: List of user IDs of users that liked the message.
- **`user_id (str)`**: The ID of the user requesting ChatMessage info(?).
- **`avatar_url (str|None)`** *optional*: The URL to the profile picture of the user that sent the message.


### `ChatMessage.from_dict`
Returns a `ChatMessage` object initialized using `chat_message_dict`.
    
**params:**
- **`chat_message_dict (dict)`**: Dictionary used to initialize the returned
`ChatMessage`, must have keys and values corresponding to the params in
`ChatMessage.__init__`