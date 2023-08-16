## `Bot`
---
### `Bot.__init__`
`Bot` constructor.
    
**params:**
- **`name (str)`**: Name of the `Bot` (this is what the `Bot` appears as in 
the `Group`)
- **`group_id (str)`**: ID of the [`Group`](#group) that the `Bot` is in 
- **`bot_id (str)`**: ID of the `Bot`
- **`avatar_url (str)`** *optional*: URL to the profile picture of the `Bot`
- **`callback_url (str)`** *optional*: URL that messages received by the `Bot` will be sent to via an HTTP POST request


### `Bot.from_dict`
Returns a `Bot` object initialized using the `bot_dict` parameter

`bot_dict` must contain the keys `name`, `group_id`, `bot_id`, and 
optionally `avatar_url`, `callback_url`.

**params:**
- **`bot_dict (dict)`:** Used to initialize the returned `Bot` object


### `Bot._create`
Creates a `Bot` and returns a `Bot` object.
    
**params:**
- **`name (str)`**: Name of the `Bot`
- **`group_id (str)`**: ID for the `Group` that the `Bot` will be added to
- **`avatar_url (str)`**: URL for the profile picture of the `Bot`
- **`callback_url (str)`** *optional*: URL that messages received by the 
`Bot` will be sent to via an HTTP POST request

**raises:**
- `UnexpectedStatusCodeError` 

### `Bot._send_message`
Sends a [`Message`](#message) in the [`Group`](#group) that the `Bot` is in. Returns the status code of the `Message` creation request.

**params:**
- **`bot_id (str)`**: ID of the `Bot` you wish to send the `Message` as
- **`text (str)`**: Text of the `Message` (max length is 1000 characters)
- **`attachments (list[Attachment])`**: List of [`Attachment`](/groupmeme/objects/#attachment)s for the `Message`

**raises:**
- `APIParameterError` 


### `Bot._get_bots`
Returns a list of all the `Bot`s you have created but not deleted.
    
**raises:**
- `UnexpectedStatusCodeError`


### `Bot._destroy`
Destroys the `Bot` with ID `bot_id`. Returns the status code of the request to destroy the `Bot`.
    
params:
- **`bot_id (str)`**: ID of the `Bot` you intend to destroy

### `Bot.send_message`
Sends a [`Message`](#message) in the [`Group`](#group) that the `Bot` is in. Returns the status code of the `Message` creation request.
    
**params:**
- **`text (str)`**: Text of the `Message` (max length is 1000 characters)
- **`attachments (list[Attachment])`**: List of `Attachment`s for the `Message`

**raises:**
- `APIParameterError` 


### `Bot.destroy`
Destroys the `Bot`. Returns the status code of the request to destroy the `Bot`.
    
**raises:**
- `UnexpectedStatusCodeError` 