## `User`
---
### `User.__init__`
Constructor for `User`.
    
**params:**
- **`id (str)`**: User ID of the user.
- **`name (str)`**: Name of the user.
- **`created_at (int)`**: Time (Unix time) that the user was created.
- **`updated_at (int)`**: Time (Unix time) that the user was last updated.
- **`image_url (str)`** *optional*: URL to the user's profile picture.
- **`zip_code (str)`** *optional*: Zip code of the user.
- **`phone_number (str)`** *optional*: Phone number of the user.
- **`email (str)`** *optional*: Email of the user.
- **`sms (bool)`** *optional*?: If the user is using SMS mode for GroupMe.


### `User.from_dict`
Returns a `User` object initialized using the `user_dict` parameter.
    
**params:**
- **`user_dict (dict)`**: Used to initialize the returned 'User` object.
Must contain keys and values corresponding to the parameters in `User.__init__`


### `User._me`
Return a `User` object containing information from your account
    
**raises:**
- `UnexpectedStatusCodeError`


### `User._update_me`
Update your user information.
    
**params:**
- **`avatar_url (str)`** *optional*: URL to your new profile picture.
- **`name (str)`** *optional*: New name for your profile.
- **`email (str)`** *optional*: New email for your profile.
- **`zip_code (str)`** *optional*: New zip code for your profile.

**raises:**
- `UnexpectedStatusCodeError`
