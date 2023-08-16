# `Chat`

## `Chat.__init__`
`Chat` constructor

**params:**
- **`created_at (int)`**: Time (Unix time) the chat was created.
- **`updated_at (int)`**: Time (Unix time) the chat was last updated.
- **`last_message (ChatMessage)`**: The last message in the chat.
- **`messages_count (int)`**: The number of messages in the chat.
- **`other_user (user)`**: The other user in the chat.


## `Chat.from_dict`
Returns a `Chat` object initialized using `chat_dict`

**params:**
- **`chat_dict (dict)`**: Used to initialize returned `Chat` object. Must have
keys and values corresponding to the params in `Chat.__init__`.

**example:**
```py
chat = Chat.from_dict({
  "created_at": 1352299338,
  "updated_at": 1352299338,
  "last_message": {
    "attachments": [

    ],
    "avatar_url": "https://i.groupme.com/200x200.jpeg.abcdef",
    "conversation_id": "12345+67890",
    "created_at": 1352299338,
    "favorited_by": [

    ],
    "id": "1234567890",
    "name": "John Doe",
    "recipient_id": "67890",
    "sender_id": "12345",
    "sender_type": "user",
    "source_guid": "GUID",
    "text": "Hello world",
    "user_id": "12345"
  },
  "messages_count": 10,
  "other_user": {
    "avatar_url": "https://i.groupme.com/200x200.jpeg.abcdef",
    "id": 12345,
    "name": "John Doe"
  }
})
```


## `Chat._chats`
Returns a paginated list of `Chat` objects.
    
**params:**
- **`page (int)`**: Page of chat results.
- **`per_page (int)`**: `Chat` objects per page.

raises:
- `UnexpectedStatusCodeError`
