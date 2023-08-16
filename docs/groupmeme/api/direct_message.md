# `DirectMessage`
## `DirectMessage.__init__`
`DirectMessage` constructor.
    
**params:**
- **`id (str)`**: The ID of the direct message.
- **`source_guid (str)`**: The guid of the direct message.
- **`recipient_id (str)`**: The ID of the user who recieved the DM.
- **`user_id (str)`**: The ID of the user that sent the message.
- **`created_at (int)`**: The time (Unix time) that the DM was created.
- **`name (str)`**: The name of the user that sent the DM.
- **`text (str)`**: The text content of the message.
- **`favorited_by (str)`**: A list of user IDs of users that liked the DM.
- **`attachments (list[Attachment])`**: A list of attachments on the DM.
- **`avatar_url (str)`** *optional*: URL to the profile picture of the user
that sent the DM.


## `DirectMessage._list`
Returns a `DirectMessage` object initialized using `dm_dict`.
    
**params:**
- **`dm_dict(dict)`**: Used to initialize the returned `DirectMessage` object.
Must contain keys and values corresponding to the params in
`DirectMessage.__init__`

**raises:**
- `UnexpectedStatusCodeError`


## `DirectMessage._create`
Create a direct message and return the direct message as a `DirectMessage` object.
    
**params:**
- **`source_guid (str)`**: GUID of the direct message.
- **`recipient_id (str)`**: ID of the recipient of the direct message.
- **`text (str)`**: Text content of the direct message.
- **`attachments (list[Attachment])`**: Attachments on the direct message.

**raises:**
- `UnexpectedStatusCodeError`