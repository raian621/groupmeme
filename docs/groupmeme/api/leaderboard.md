# `Leaderboard`
## `Leaderboard._likes`
Returns a list of the liked messages in the group for a given time period.
    
**params:**
- **`group_id (str)`**: The ID of the group you wish to query liked messages from.
- **`period (str)`**: The time period for which you want to query liked messages from. Possible values are 'day', 'week', or 'month', corresponding to liked liked messaged from the last day, last week, and last month respectively.

**raises:**
- `UnexpectedStatusCodeError`


## `Leaderboard._my_likes`
Returns a list of the messages you've liked in the group with ID `group_id`.
    
**params:**
- **`group_id (str)`**: The ID of the group you'd like to query your the messages you've liked from.

**raises:**
- `UnexpectedStatusCodeError`


## `Leaderboard._my_hits`
Returns a list of your messages that have been liked in the group with ID
`group_id`.

**params:**
- **`group_id (str)`**: The ID of the group you'd like to query your liked
messages from.

**raises:**
- `UnexpectedStatusCodeError`