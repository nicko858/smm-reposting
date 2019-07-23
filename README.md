# Smm-reposting

Using this script, you can make automatic posting at the same time to the next services:
 - [facebook](https://www.facebook.com)
 - [vk.com](https://vk.com)
 - [telegram](https://telegram.org/)
 

The script uses following external API's: 
- [facebook-api](https://graph.facebook.com")
- [vk-api](https://api.vk.com)
- [telegram-api](https://api.telegram.org)

If everything is fine, you'll see a new post in your `vk` ,`facebook` and `telegram` groups: 

![1.png](https://github.com/nicko858/smm-reposting/blob/master/screenshots/1.png)
## How to install
Python3 should be already installed.
```bash
$ git clone https://github.com/nicko858/smm-reposting.git
$ cd smm-reposting
$ pip install -r requirements.txt
```
- Create file `.env` in the script directory

### VK instructions
- Create account on the [vk.com](https://vk.com), or use existing
- Create fan-group where you are going to post - [vk group management](https://vk.com/groups?tab=admin)
- Register new application following this [link](https://vk.com/apps?act=manage)
- Make sure, that application is turned on and remember it's `application_id`:
![023.png](https://github.com/nicko858/comics_publisher/blob/master/screenshots/%D0%92%D1%8B%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5_023.png)
- Link application with group created on the previous step:
![024.png](https://github.com/nicko858/comics_publisher/blob/master/screenshots/%D0%92%D1%8B%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5_024.png)
- Get `access_token` using [Implicit Flow](https://vk.com/dev/implicit_flow_user):

![025.png](https://github.com/nicko858/comics_publisher/blob/master/screenshots/%D0%92%D1%8B%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5_025.png)

and remember it

- Add the following records to the `.env-file`:  

   ```bash
   client_id=Your application_id
   access_token=Your access token
   vk_group_id=Your vk_group_id
  ```

### Telegram instructions
You have to create telegram-channel, telegram-bot and get access-token.
[This arcticle](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/) will helps you to do all of this things.
If everything is fine, you'll get `telegram_bot_token`, `telegram_bot_url` and  `telegram_channel_name`.  
Add the following records to the `.env-file`:  

   ```bash
telegram_bot_token=Your bot token
telegram_bot_url=Your bot address
telegram_channel_name=Your telegram channel
  ```

### Facebook instructions
- Create account on the [facebook](https://www.facebook.com), or use existing
- Create fan-group where you are going to post - ![2.png](https://github.com/nicko858/smm-reposting/blob/master/screenshots/2.png)
- Register as a [developer](https://developers.facebook.com/)
- Create a new application - ![3.png](https://github.com/nicko858/smm-reposting/blob/master/screenshots/3.png)
- Using [Facebook Graph API Explorer](https://developers.facebook.com/tools/explorer/), get access token with `publish_to_groups` - permission: ![4.png](https://github.com/nicko858/smm-reposting/blob/master/screenshots/4.png)
- Add the following records to the `.env-file`:  

  ```bash
    facebook_token=Your Facebook token
    facebook_group=Your Facebook group id
  ```

## How to run

```bash
    python reposting.py <path_to_img file> <post message>
 ```


### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
