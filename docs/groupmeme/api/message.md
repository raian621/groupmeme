## `Message`
---
### `Message.__init__`
`Group` constructor
    
**params:**
- **`id (str)`**: The ID of the `Message`.
- **`source_guid (str)`**: The guid of the `Message`. Can be used as a client-side
ID for the message. The server scans the `source_guid` of each `Message` for
duplication; If two messages are sent with the same `source_guid` within one
minute, the second message will fail to send and yield a 409 Conflict HTTP 
response code.
- **`created_at (int)`**: The time (UNIX time) that the `Message` was created at.
- **`user_id (str)`**: The id of the `User` that sent the `Message`.
- **`group_id (str)`**: The `Group` that the message was sent in.
- **`name (str)`**: The name of the sender of the message.
- **`avatar_url (str)`**: URL to the profile picture of the `User` that sent the 
message. The URL will always be what the senders profile picture URL was when
they sent the message.
- **`text (str)`**: The text content of the message.
- **`system (bool)`**: Whether the message was sent by the system.
- **`favorited_by (list[str])`**: A list of the user ids of `User`s that liked the
message
- **`attachments (list[Attachment])`**: A list of attachments on the message.


### `Message.from_dict`
Returns a `Message` object initialized using the `message_dict` parameter.
    
**params:**
- **`message_dict (dict)`**: Used to initialize the returned `Message` object.
Must contain keys and values corresponding to the parameters in 
`Message.__init__`.

**example:**

```py
message = Message.from_dict({
  "id": "<id>",
  "source_guid": "<source_guid>",
  "created_at": 123456789,
  "user_id": "<user_id>",
  "group_id": "<group_id>",
  "name": "<name>",
  "avatar_url": "<avatar_url>",
  "text": "<text>",
  "system": False,
  "favorited_by": ["123", "1234"],
  "attachments": [Attachment(type="image", url="<image_url>")],
})
```

### `Message._messages`
Returns a list of messages for a given time period in a `Group`.
    
**params:**
- **`group_id (str)`**: The ID of the group you want to retrieve messages from.
- **`before_id (str)`**: Get messages created before the message with ID 
`before_id`
- **`after_id (str)`**: Get messages created immediately after the message with
ID `after_id`.
- **`since_id (str)`**: Get the most recent messages created since the message
with ID `since_id`.
- **`limit (int)`**: Limit the number of messages returned (default=20, max=100).

**raises:**
- `UnexpectedStatusCodeError`
- `APIParameterError`

### `Message._create`
Posts a message to the group given by `group_id`.
    
**params:**
- **`group_id (str)`**: ID of the group to post the message to
- **`text (str)`**: Text content of the message
- **`source_guid (str)`**: The guid of the `Message`. Can be used as client-side
IDs for messages. The server scans the `source_guid` of each `Message` for
duplication; If two messages are sent with the same `source_guid` within one
minute the second message will fail to send, yielding a 409 Conflict HTTP 
response code.
- **`attachments (list[Attachment])`**: Attachments on the message to be posted

**raises:**
- `UnexpectedStatusCodeError`
