# `Like`
## `Like._like`
Like a message. Returns the status code of the response from the GroupMe API
server.

**params:**
- **`conversation_id (str)`**: The ID of the conversation that the message you want
like is in.
- **`message_id (str)`**: The ID of the message you want to like

**raises:**
- `UnexpectedStatusCodeError`


## `Like._unlike`
Unlike a message. Returns the status code of the response from the GroupMe API
server.

**params:**
- **`conversation_id (str)`**: The ID of the conversation that the message you want unlike is in.
- **`message_id (str)`**: The ID of the message you want to unlike.

**raises:**
- `UnexpectedStatusCodeError`