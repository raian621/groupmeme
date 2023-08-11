# groupmeme.api.errors
## `UnexpectedStatusCodeError`
Raised whenever a request to the GroupMe API fails.

### `UnexpectedStatusCodeError.__init__`
**params**:
- **`code (int)`**: The status code that was returned from the GroupMe API
- **`expected (int)`**: The status code that should have been returned from the GroupMe API

## `APIParameterError`
### `APIParameterError.__init__`
Raised when an API parameter violates some GroupMe defined rule (ex. the `text` parameter in the function that sends a message can't be longer than 1000 characters)

**params**:
- **`param_name (str)`**:
- **`message (str)`**: